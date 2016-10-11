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


def question4(head, partition):
    """
    Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
    before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
    to be after the elements less than x (see below). The partition element x can appear anywhere in the
    "right partition"; it does not need to appear between the left and right partitions.
    EXAMPLE
    Input: 3->5->8->5->10->2->1 [partition = 5]
    Output: 3->1->2->5->10->5->8
    :param head: head node of the input linked list
    :param partition: value to partition the linked list by
    :return: head node of a new partitioned linked list
    """
    head_one = Node(data=head.get_data()) if head.get_data() < partition else None
    head_two = Node(data=head.get_data()) if head.get_data() >= partition else None
    tail_one = None
    tail_two = None
    current_node = head
    while current_node.get_next() is not None:
        if current_node.get_next().get_data() < partition:
            if head_one is None:
                head_one = Node(data=current_node.get_next().get_data())
            elif tail_one is None:
                tail_one = Node(data=current_node.get_next().get_data())
                head_one.set_next(tail_one)
            else:
                new_node = Node(data=current_node.get_next().get_data())
                tail_one.set_next(new_node)
                tail_one = new_node
        elif current_node.get_next().get_data() >= partition:
            if head_two is None:
                head_two = Node(data=current_node.get_next().get_data())
            if tail_two is None:
                tail_two = Node(data=current_node.get_next().get_data())
                head_two.set_next(tail_two)
            else:
                new_node = Node(data=current_node.get_next().get_data())
                tail_two.set_next(new_node)
                tail_two = new_node
        current_node = current_node.get_next()

    if head_two is not None:
        tail_one.set_next(head_two)
    return head_one


def question5(head_one, head_two, forward_order=False):
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
    :param forward_order: True if lists should be treated with the ordering of numbers being in forward order instead of
    reverse.
    :return: linked list representing the sum of the two input linked lists
    """
    if not forward_order:
        head_sum = None
        tail_sum = None
        current_one = head_one
        current_two = head_two
        carry = 0
        # While there are more significant digits
        while current_one.get_next() is not None and current_two.get_next() is not None:
            if head_sum is None:
                head_sum = Node(data=(current_one.get_data() + current_two.get_data()) % 10)
            else:
                if head_sum.get_next() is None:
                    tail_sum = Node(data=(current_one.get_data() + current_two.get_data() + carry) % 10)
                    head_sum.set_next(tail_sum)
                else:
                    new_node = Node(data=(current_one.get_data() + current_two.get_data() + carry) % 10)
                    tail_sum.set_next(new_node)
            carry = (current_one.get_data() + current_two.get_data() + carry) / 10
            current_one = current_one.get_next()
            current_two = current_two.get_next()

        # Handle the most significant digit
        if head_sum is None:
            head_sum = Node(data=(current_one.get_data() + current_two.get_data()) % 10)
        elif head_sum.get_next() is None:
            tail_sum = Node(data=(current_one.get_data() + current_two.get_data() + carry) % 10)
            head_sum.set_next(tail_sum)
        else:
            new_node = Node(data=(current_one.get_data() + current_two.get_data() + carry) % 10)
            tail_sum.set_next(new_node)
        carry = (current_one.get_data() + current_two.get_data() + carry) / 10
        if carry > 0:
            new_node = Node(data=carry)
            tail_sum.set_next(new_node)
        return head_sum
    else:
        return _question5_recursive_forward_order(head_one, head_two)[0]


def _question5_recursive_forward_order(head_one, head_two):
    """
    See question 5.
    :param head_one: head node of the first input linked list
    :param head_two: head node of the second input linked list
    :param forward_order: True if lists should be treated with the ordering of numbers being in forward order instead of
    reverse.
    :return: linked list representing the sum of the two input linked lists and a number to be carried over into the more significant digit
    """
    # Base Case
    if head_one.get_next() is None and head_two.get_next() is None:
        sum_node = Node(data=(head_one.get_data() + head_two.get_data()) % 10)
        return sum_node, ((head_one.get_data() + head_two.get_data()) / 10)
    else:
        new_node, carry = _question5_recursive_forward_order(head_one.get_next(), head_two.get_next())
        head_sum = Node(data=(head_one.get_data() + head_two.get_data() + carry) % 10, next_node=new_node)
        return head_sum, ((head_one.get_data() + head_two.get_data()) / 10)


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

