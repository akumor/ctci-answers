#!/usr/bin/env python
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from ctci import chapter2
import unittest
import timeit
import numpy
import logging
import time

class Chapter2Test(unittest.TestCase):

    def setUp(self):
        """
        Prepare to run test.
        """
        pass

    def tearDown(self):
        """
        Clean up after running test.
        """
        pass

    def test_question1(self):
        """
        2.1 p.94
        """
        log = logging.getLogger("Chapter2Test.test_question1")
        node1 = chapter2.Node(data=1)
        node2 = chapter2.Node(data=2, next_node=node1)
        node3 = chapter2.Node(data=2, next_node=node2)
        node4 = chapter2.Node(data=3, next_node=node3)
        node5 = chapter2.Node(data=1)
        node6 = chapter2.Node(data=2, next_node=node5)
        node7 = chapter2.Node(data=3, next_node=node6)
        start_time = time.time()
        removed_dupes = chapter2.question1(node4, follow_up=False)
        end_time = time.time()
        execution_time = end_time - start_time
        assert removed_dupes.get_data() is node7.get_data()
        assert removed_dupes.get_next().get_data() is node6.get_data()
        assert removed_dupes.get_next().get_next().get_data() is node5.get_data()
        assert removed_dupes.get_next().get_next().get_next() is None
        log.info("Question 1 remove dupes time: %s seconds." % format(execution_time, '.2f'))
        start_time = time.time()
        removed_dupes = chapter2.question1(node4, follow_up=True)
        end_time = time.time()
        execution_time = end_time - start_time
        assert removed_dupes.get_data() is node7.get_data()
        assert removed_dupes.get_next().get_data() is node6.get_data()
        assert removed_dupes.get_next().get_next().get_data() is node5.get_data()
        assert removed_dupes.get_next().get_next().get_next() is None
        log.info("Question 1 remove dupes follow up time: %s seconds." % format(execution_time, '.2f'))

    def test_question2(self):
        """
        2.2 p.94
        """
        log = logging.getLogger("Chapter2Test.test_question2")
        node7 = chapter2.Node(data=7)
        node6 = chapter2.Node(data=6, next_node=node7)
        node5 = chapter2.Node(data=5, next_node=node6)
        node4 = chapter2.Node(data=4, next_node=node5)
        node3 = chapter2.Node(data=3, next_node=node4)
        node2 = chapter2.Node(data=2, next_node=node3)
        node1 = chapter2.Node(data=1, next_node=node2)
        start_time = time.time()
        kth_node = chapter2.question2(node1, 1)
        end_time = time.time()
        execution_time = end_time - start_time
        log.debug('kth_node data: ' + str(kth_node.get_data()))
        assert kth_node.get_data() is 7
        log.info("Question 2 kth node time: %s seconds." % format(execution_time, '.2f'))
        kth_node = chapter2.question2(node1, 2)
        log.debug('kth_node data: ' + str(kth_node.get_data()))
        assert kth_node.get_data() is 6
        kth_node = chapter2.question2(node1, 3)
        log.debug('kth_node data: ' + str(kth_node.get_data()))
        assert kth_node.get_data() is 5
        kth_node = chapter2.question2(node1, 4)
        log.debug('kth_node data: ' + str(kth_node.get_data()))
        assert kth_node.get_data() is 4
        kth_node = chapter2.question2(node1, 5)
        log.debug('kth_node data: ' + str(kth_node.get_data()))
        assert kth_node.get_data() is 3
        kth_node = chapter2.question2(node1, 6)
        log.debug('kth_node data: ' + str(kth_node.get_data()))
        assert kth_node.get_data() is 2
        kth_node = chapter2.question2(node1, 7)
        log.debug('kth_node data: ' + str(kth_node.get_data()))
        assert kth_node.get_data() is 1

    def test_question3(self):
        """
        2.3 p.94
        """
        log = logging.getLogger("Chapter2Test.test_question3")
        node7 = chapter2.Node(data=7)
        node6 = chapter2.Node(data=6, next_node=node7)
        node5 = chapter2.Node(data=5, next_node=node6)
        node4 = chapter2.Node(data=4, next_node=node5)
        node3 = chapter2.Node(data=3, next_node=node4)
        node2 = chapter2.Node(data=2, next_node=node3)
        node1 = chapter2.Node(data=1, next_node=node2)
        start_time = time.time()
        node2 = chapter2.question3(node2)
        end_time = time.time()
        execution_time = end_time - start_time
        assert node2.get_data() == 3
        assert node2.get_next() is node4
        log.info("Question 3 Delete Middle Node time: %s seconds." % format(execution_time, '.2f'))
        node3 = chapter2.question3(node3)
        assert node3.get_data() == 4
        assert node3.get_next() is node5
        node4 = chapter2.question3(node4)
        assert node4.get_data() == 5
        assert node4.get_next() is node6
        node5 = chapter2.question3(node5)
        assert node5.get_data() == 6
        assert node5.get_next() is node7
        node6 = chapter2.question3(node6)
        assert node6.get_data() == 7
        assert node6.get_next() is None

    def test_question4(self):
        """
        2.4 p.94
        """
        log = logging.getLogger("Chapter2Test.test_question4")
        node7 = chapter2.Node(data=1)
        node6 = chapter2.Node(data=2, next_node=node7)
        node5 = chapter2.Node(data=10, next_node=node6)
        node4 = chapter2.Node(data=5, next_node=node5)
        node3 = chapter2.Node(data=8, next_node=node4)
        node2 = chapter2.Node(data=5, next_node=node3)
        node1 = chapter2.Node(data=3, next_node=node2)
        start_time = time.time()
        new_head = chapter2.question4(node1, 5)
        end_time = time.time()
        execution_time = end_time - start_time
        reached_second_partition = False
        current_node = new_head
        while current_node.get_next() is not None:
            if current_node.get_data() >= 5 and not reached_second_partition:
                reached_second_partition = True
            if reached_second_partition:
                assert current_node.get_data() >= 5
            else:
                assert current_node.get_data() < 5
            current_node = current_node.get_next()
        assert current_node.get_data() >= 5
        log.info("Question 4 partition: %s seconds." % execution_time)

    def test_question5(self):
        """
        TODO 2.5 p.95
        """
        node1 = chapter2.Node(data=1)
        node2 = chapter2.Node(data=2, next_node=node1)
        node3 = chapter2.Node(data=2, next_node=node2)
        node4 = chapter2.Node(data=3, next_node=node3)
        node5 = chapter2.Node(data=1)
        node6 = chapter2.Node(data=2, next_node=node5)
        node7 = chapter2.Node(data=3, next_node=node6)

        is_one_away = chapter2.question5('pale', 'ple')
        assert is_one_away is True
        t = timeit.Timer(stmt='question5("pale", "ple")', setup='from ctci.chapter2 import question5')
        print "Question 5 one away True1: %s seconds." % t.timeit(5)
        is_one_away = chapter2.question5('pales', 'pale')
        assert is_one_away is True
        t = timeit.Timer(stmt='question5("pales", "pale")', setup='from ctci.chapter2 import question5')
        print "Question 5 one away True2: %s seconds." % t.timeit(5)
        is_one_away = chapter2.question5('pale', 'bale')
        assert is_one_away is True
        t = timeit.Timer(stmt='question5("pale", "bale")', setup='from ctci.chapter2 import question5')
        print "Question 5 one away True3: %s seconds." % t.timeit(5)
        is_one_away = chapter2.question5('pale', 'bake')
        assert is_one_away is False
        t = timeit.Timer(stmt='question5("pale", "bake")', setup='from ctci.chapter2 import question5')
        print "Question 5 one away False: %s seconds." % t.timeit(5)

    def test_question6(self):
        """
        TODO 2.6 p.95
        """
        node1 = chapter2.Node(data=1)
        node2 = chapter2.Node(data=2, next_node=node1)
        node3 = chapter2.Node(data=2, next_node=node2)
        node4 = chapter2.Node(data=3, next_node=node3)
        node5 = chapter2.Node(data=1)
        node6 = chapter2.Node(data=2, next_node=node5)
        node7 = chapter2.Node(data=3, next_node=node6)

        compressed_string = chapter2.question6('aa')
        assert compressed_string == 'aa'
        t = timeit.Timer(stmt='question6("aa")', setup='from ctci.chapter2 import question6')
        print "Question 6 uncompressed string: %s seconds." % t.timeit(5)
        compressed_string = chapter2.question6('aabcccccaaa')
        assert compressed_string == 'a2b1c5a3'
        t = timeit.Timer(stmt='question6("aabcccccaaa")', setup='from ctci.chapter2 import question6')
        print "Question 6 compressed string: %s seconds." % t.timeit(5)

    def test_question7(self):
        """
        TODO 2.7 p.95
        """
        node1 = chapter2.Node(data=1)
        node2 = chapter2.Node(data=2, next_node=node1)
        node3 = chapter2.Node(data=2, next_node=node2)
        node4 = chapter2.Node(data=3, next_node=node3)
        node5 = chapter2.Node(data=1)
        node6 = chapter2.Node(data=2, next_node=node5)
        node7 = chapter2.Node(data=3, next_node=node6)

        x = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
        y = numpy.array([[3, 6, 9, 12], [2, 5, 8, 11], [1, 4, 7, 10]])
        x_rot = chapter2.question7(x)
        assert numpy.array_equal(x_rot, y) is True
        t = timeit.Timer(stmt='question7(numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))',
                         setup='import numpy; from ctci.chapter2 import question7')
        print "Question 7 rotated matrix: %s seconds." % t.timeit(5)

    def test_question8(self):
        """
        TODO 2.8 p.95
        """
        node1 = chapter2.Node(data=1)
        node2 = chapter2.Node(data=2, next_node=node1)
        node3 = chapter2.Node(data=2, next_node=node2)
        node4 = chapter2.Node(data=3, next_node=node3)
        node5 = chapter2.Node(data=1)
        node6 = chapter2.Node(data=2, next_node=node5)
        node7 = chapter2.Node(data=3, next_node=node6)

        x = numpy.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
        y = numpy.array([[0, 0, 0], [0, 4, 5], [0, 7, 8], [0, 10, 11]])
        x_zero = chapter2.question8(x)
        assert numpy.array_equal(x_zero, y) is True
        t = timeit.Timer(stmt='question8(numpy.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]))',
                         setup='import numpy; from ctci.chapter2 import question8')
        print "Question 8 zero matrix: %s seconds." % t.timeit(5)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout)
    logging.getLogger("Chapter2Test.test_question1").setLevel(logging.DEBUG)
    logging.getLogger("Chapter2Test.test_question2").setLevel(logging.DEBUG)
    logging.getLogger("Chapter2Test.test_question3").setLevel(logging.DEBUG)
    logging.getLogger("Chapter2Test.test_question4").setLevel(logging.DEBUG)
    logging.getLogger("Chapter2Test.test_question5").setLevel(logging.DEBUG)
    logging.getLogger("Chapter2Test.test_question6").setLevel(logging.DEBUG)
    logging.getLogger("Chapter2Test.test_question7").setLevel(logging.DEBUG)
    logging.getLogger("Chapter2Test.test_question8").setLevel(logging.DEBUG)
    logging.getLogger("Chapter2Test.test_question9").setLevel(logging.DEBUG)
    logging.getLogger("Chapter2Test.setUp").setLevel(logging.DEBUG)
    logging.getLogger("Chapter2Test.tearDown").setLevel(logging.DEBUG)
    unittest.main()