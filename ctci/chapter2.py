#!/usr/bin/python
# Chapter 2 Linked Lists
import timeit
import numpy
import time


class Node(object):
    """
    Node as part of a linked list.
    """

    def __init__(self, data=None, next_node=None):
        """
        Constructor
        :param data: data stored as part of the node.
        :param next_node: pointer to the next node in the list.
        """
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next_node = new_next


def question1(head, follow_up=False):
    """
    Remove Dups: Write code to remove duplicates from an unsorted linked list.
    FOLLOW UP
    How would you solve this problem if a temporary buffer is not allowed?
    :param head: Node that represents the first node in a linked list
    :param follow_up: True if the FOLLOW UP implementation should be used or not
    :return: head node of a linked list with nodes containing duplicate data removed
    """
    new_head = Node(data=head.get_data(), next_node=None)
    current_node = head
    new_node = None
    dataset = {head.get_data()}
    while current_node.get_next() is not None:
        if current_node.get_next().get_data() not in dataset:
            if new_node is None:
                new_node = Node(data=current_node.get_next().get_data(), next_node=None)
            else:
                new_node.set_next(Node(data=current_node.get_next().get_data(), next_node=None))
                new_node = new_node.get_next()
            if new_head.get_next() is None:
                new_head.set_next(new_node)
            dataset.add(current_node.get_next().get_data())
        current_node = current_node.get_next()
    return new_head


def question2(head, k):
    """
    Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
    :param head: Node that represents the first node in a linked list
    :param k: integer representing the k in kth to the last element
    :return: Node
    """
    length = 1
    current_node = head
    while current_node.get_next() is not None:
        length += 1
        current_node = current_node.get_next()

    node_index = length - k
    current_node = head
    while node_index != 0:
        node_index -= 1
        current_node = current_node.get_next()

    return current_node


def question3(middle_node):
    """
    Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
    the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
    that node.
    EXAMPLE
    Input: the node c from the linked list a->b->c->d->e->f
    Result: nothing is returned, but the new linked list looks like a->b->d->e->f
    :return: middle node
    """
    middle_node.set_data(middle_node.get_next().get_data())
    middle_node.set_next(middle_node.get_next().get_next())
    return middle_node


def question4(head):
    """
    Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
    before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
    to be after the elements less than x (see below). The partition element x can appear anywhere in the
    "right partition"; it does not need to appear between the left and right partitions.
    EXAMPLE
    Input: 3->5->8->5->10->2->1 [partition = 5]
    Output: 3->1->2->5->10->5->8
    :param head: head node of the input linked list
    :return: linked list
    """
    pass


def question5(head_one, head_two):
    """
    Sum Lists: You have two numbers represented by a linked list, where each node contains a single
    digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a
    function that adds the two numbers and returns the sum as a linked list.
    EXAMPLE
    Input: (7->1->6) + (5->9->2). That is, 617 + 295.
    Output: 2->1->9. That is, 912.
    FOLLOW UP
    Suppose the digits are stored in forward order. Repeat the above problem.
    EXAMPLE
    Input: (6->1->7) + (2->9->5). That is, 617 + 295.
    Output: 9->1->2. That is 912.
    :param head_one: head node of the first input linked list
    :param head_two: head node of the second input linked list
    :return: linked list representing the sum of the two input linked lists
    """
    pass


def question6():
    """
    Palindrome: Implement a function to check if a linked list is a palindrome.
    :return:
    """
    pass


def question7():
    """
    Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
    intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth
    node of the first linked list is the exact same node (by reference) as the jth node of the second
    linked list, then they are intersecting.
    :return:
    """
    pass


def question8():
    """
    Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
    beginning of the loop.
    DEFINITION
    Circular linked list: A (corrupt) linked list in which a node's next point points to an earlier node, so
    as to make a loop in the linked list.
    EXAMPLE
    Input: A->B->C->D->E->C (the same C as earlier)
    Output: C
    :return:
    """
    pass

# 2.1 p.94
node1 = Node(data=1)
node2 = Node(data=2, next_node=node1)
node3 = Node(data=2, next_node=node2)
node4 = Node(data=3, next_node=node3)
node5 = Node(data=1)
node6 = Node(data=2, next_node=node5)
node7 = Node(data=3, next_node=node6)
start_time = time.time()
removed_dupes = question1(node4, follow_up=False)
end_time = time.time()
execution_time = end_time - start_time
assert removed_dupes.get_data() is node7.get_data()
assert removed_dupes.get_next().get_data() is node6.get_data()
assert removed_dupes.get_next().get_next().get_data() is node5.get_data()
assert removed_dupes.get_next().get_next().get_next() is None
print "Question 1 remove dupes time: %s seconds." % format(execution_time, '.2f')
start_time = time.time()
removed_dupes = question1(node4, follow_up=True)
end_time = time.time()
execution_time = end_time - start_time
assert removed_dupes.get_data() is node7.get_data()
assert removed_dupes.get_next().get_data() is node6.get_data()
assert removed_dupes.get_next().get_next().get_data() is node5.get_data()
assert removed_dupes.get_next().get_next().get_next() is None
print "Question 1 remove dupes follow up time: %s seconds." % format(execution_time, '.2f')
# 2.2 p.94
start_time = time.time()
kth_node = question2(node7, 1)
end_time = time.time()
execution_time = end_time - start_time
assert kth_node.get_data() is node6.get_data()
assert kth_node.get_next() is node6.get_next()
print "Question 2 kth node time: %s seconds." % format(execution_time, '.2f')
# 2.3 p.94
node1 = Node(data=1)
node2 = Node(data=2, next_node=node1)
node3 = Node(data=2, next_node=node2)
node4 = Node(data=3, next_node=node3)
node5 = Node(data=1)
node6 = Node(data=2, next_node=node5)
node7 = Node(data=3, next_node=node6)
start_time = time.time()
node3 = question3(node3)
end_time = time.time()
execution_time = end_time - start_time
assert node3.get_data() == 3
assert node3.get_next() is None
print "Question 3 Delete Middle Node time: %s seconds." % format(execution_time, '.2f')
# 2.4 p.94
is_perm_of_palindrome = question4('Theramin')
assert is_perm_of_palindrome is False
t = timeit.Timer(stmt='question4("Theramin")', setup='from interview_questions import question4')
print "Question 4 not permutation of palindrome: %s seconds." % t.timeit(5)
is_perm_of_palindrome = question4('Tact Coa')
assert is_permutation is True
t = timeit.Timer(stmt='question4("Tact Coa")', setup='from interview_questions import question4')
print "Question 4 permutation of palindrome: %s seconds." % t.timeit(5)
# 2.5 p.95
is_one_away = question5('pale', 'ple')
assert is_one_away is True
t = timeit.Timer(stmt='question5("pale", "ple")', setup='from interview_questions import question5')
print "Question 5 one away True1: %s seconds." % t.timeit(5)
is_one_away = question5('pales', 'pale')
assert is_one_away is True
t = timeit.Timer(stmt='question5("pales", "pale")', setup='from interview_questions import question5')
print "Question 5 one away True2: %s seconds." % t.timeit(5)
is_one_away = question5('pale', 'bale')
assert is_one_away is True
t = timeit.Timer(stmt='question5("pale", "bale")', setup='from interview_questions import question5')
print "Question 5 one away True3: %s seconds." % t.timeit(5)
is_one_away = question5('pale', 'bake')
assert is_one_away is False
t = timeit.Timer(stmt='question5("pale", "bake")', setup='from interview_questions import question5')
print "Question 5 one away False: %s seconds." % t.timeit(5)
# 2.6 p.95
compressed_string = question6('aa')
assert compressed_string == 'aa'
t = timeit.Timer(stmt='question6("aa")', setup='from interview_questions import question6')
print "Question 6 uncompressed string: %s seconds." % t.timeit(5)
compressed_string = question6('aabcccccaaa')
assert compressed_string == 'a2b1c5a3'
t = timeit.Timer(stmt='question6("aabcccccaaa")', setup='from interview_questions import question6')
print "Question 6 compressed string: %s seconds." % t.timeit(5)
# 2.7 p.95
x = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
y = numpy.array([[3, 6, 9, 12], [2, 5, 8, 11], [1, 4, 7, 10]])
x_rot = question7(x)
assert numpy.array_equal(x_rot, y) is True
t = timeit.Timer(stmt='question7(numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))',
                 setup='import numpy; from interview_questions import question7')
print "Question 7 rotated matrix: %s seconds." % t.timeit(5)
# 2.8 p.95
x = numpy.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
y = numpy.array([[0, 0, 0], [0, 4, 5], [0, 7, 8], [0, 10, 11]])
x_zero = question8(x)
assert numpy.array_equal(x_zero, y) is True
t = timeit.Timer(stmt='question8(numpy.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]))',
                 setup='import numpy; from interview_questions import question8')
print "Question 8 zero matrix: %s seconds." % t.timeit(5)
