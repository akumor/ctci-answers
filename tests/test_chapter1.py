#!/usr/bin/env python
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from ctci import chapter1
import unittest
import timeit
import numpy
import logging


class Chapter1Test(unittest.TestCase):

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
        1.1 p.90
        """
        is_unique = chapter1.question1('thisstring')
        assert is_unique is False
        t = timeit.Timer(stmt='question1("thisstring")', setup='from ctci.chapter1 import question1')
        print "Question 1 not unique execution time: %s seconds." % t.timeit(5)
        is_unique = chapter1.question1('orig')
        assert is_unique is True
        t = timeit.Timer(stmt='question1("orig")', setup='from ctci.chapter1 import question1')
        print "Question 1 unique execution time: %s seconds." % t.timeit(5)

    def test_question2(self):
        """
        1.2 p.90
        """
        is_permutation = chapter1.question2('this', 'fkdaljka')
        assert is_permutation is False
        t = timeit.Timer(stmt='question2("this", "fkdaljka")', setup='from ctci.chapter1 import question2')
        print "Question 2 not permutation execution time: %s seconds." % t.timeit(5)
        is_permutation = chapter1.question2('this', 'hits')
        assert is_permutation is True
        t = timeit.Timer(stmt='question2("this", "hits")', setup='from ctci.chapter1 import question2')
        print "Question 2 permutation execution time: %s seconds." % t.timeit(5)

    def test_question3(self):
        """
        1.3 p.90
        """
        urlified = chapter1.question3("Mr John Smith")
        assert urlified == "Mr%20John%20Smith"
        t = timeit.Timer(stmt='question3("Mr John Smith")', setup='from ctci.chapter1 import question3')
        print "Question 3 urlified: %s seconds." % t.timeit(5)

    def test_question4(self):
        """
        1.4 p.91
        """
        is_perm_of_palindrome = chapter1.question4('Theramin')
        assert is_perm_of_palindrome is False
        t = timeit.Timer(stmt='question4("Theramin")', setup='from ctci.chapter1 import question4')
        print "Question 4 not permutation of palindrome: %s seconds." % t.timeit(5)
        is_perm_of_palindrome = chapter1.question4('Tact Coa')
        assert is_perm_of_palindrome is True
        t = timeit.Timer(stmt='question4("Tact Coa")', setup='from ctci.chapter1 import question4')
        print "Question 4 permutation of palindrome: %s seconds." % t.timeit(5)

    def test_question5(self):
        """
        1.5 p.91
        """
        is_one_away = chapter1.question5('pale', 'ple')
        assert is_one_away is True
        t = timeit.Timer(stmt='question5("pale", "ple")', setup='from ctci.chapter1 import question5')
        print "Question 5 one away True1: %s seconds." % t.timeit(5)
        is_one_away = chapter1.question5('pales', 'pale')
        assert is_one_away is True
        t = timeit.Timer(stmt='question5("pales", "pale")', setup='from ctci.chapter1 import question5')
        print "Question 5 one away True2: %s seconds." % t.timeit(5)
        is_one_away = chapter1.question5('pale', 'bale')
        assert is_one_away is True
        t = timeit.Timer(stmt='question5("pale", "bale")', setup='from ctci.chapter1 import question5')
        print "Question 5 one away True3: %s seconds." % t.timeit(5)
        is_one_away = chapter1.question5('pale', 'bake')
        assert is_one_away is False
        t = timeit.Timer(stmt='question5("pale", "bake")', setup='from ctci.chapter1 import question5')
        print "Question 5 one away False: %s seconds." % t.timeit(5)

    def test_question6(self):
        """
        1.6 p.91
        """
        compressed_string = chapter1.question6('aa')
        assert compressed_string == 'aa'
        t = timeit.Timer(stmt='question6("aa")', setup='from ctci.chapter1 import question6')
        print "Question 6 uncompressed string: %s seconds." % t.timeit(5)
        compressed_string = chapter1.question6('aabcccccaaa')
        assert compressed_string == 'a2b1c5a3'
        t = timeit.Timer(stmt='question6("aabcccccaaa")', setup='from ctci.chapter1 import question6')
        print "Question 6 compressed string: %s seconds." % t.timeit(5)

    def test_question7(self):
        """
        1.7 p.91
        """
        x = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
        y = numpy.array([[3, 6, 9, 12], [2, 5, 8, 11], [1, 4, 7, 10]])
        x_rot = chapter1.question7(x)
        assert numpy.array_equal(x_rot, y) is True
        t = timeit.Timer(stmt='question7(numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))',
                         setup='import numpy; from ctci.chapter1 import question7')
        print "Question 7 rotated matrix: %s seconds." % t.timeit(5)

    def test_question8(self):
        """
        1.8 p.91
        """
        x = numpy.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
        y = numpy.array([[0, 0, 0], [0, 4, 5], [0, 7, 8], [0, 10, 11]])
        x_zero = chapter1.question8(x)
        assert numpy.array_equal(x_zero, y) is True
        t = timeit.Timer(stmt='question8(numpy.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]))',
                         setup='import numpy; from ctci.chapter1 import question8')
        print "Question 8 zero matrix: %s seconds." % t.timeit(5)

    def test_question9(self):
        """
        1.9 p.91
        """
        assert chapter1.question9("waterbottle", "erbottlewat") is True
        t = timeit.Timer(stmt='question9("waterbottle", "erbottlewat")', setup='from ctci.chapter1 import question9')
        print "Question 9 rotated string: %s seconds." % t.timeit(5)
        assert chapter1.question9("watertbottle", "erbotttlewat") is False
        t = timeit.Timer(stmt='question9("watertbottle", "erbotttlewat")',
                         setup='from ctci.chapter1 import question9')
        print "Question 9 non-rotated string: %s seconds." % t.timeit(5)

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout)
    logging.getLogger("Chapter1Test.test_question1").setLevel(logging.DEBUG)
    logging.getLogger("Chapter1Test.test_question2").setLevel(logging.DEBUG)
    logging.getLogger("Chapter1Test.test_question3").setLevel(logging.DEBUG)
    logging.getLogger("Chapter1Test.test_question4").setLevel(logging.DEBUG)
    logging.getLogger("Chapter1Test.test_question5").setLevel(logging.DEBUG)
    logging.getLogger("Chapter1Test.test_question6").setLevel(logging.DEBUG)
    logging.getLogger("Chapter1Test.test_question7").setLevel(logging.DEBUG)
    logging.getLogger("Chapter1Test.test_question8").setLevel(logging.DEBUG)
    logging.getLogger("Chapter1Test.test_question9").setLevel(logging.DEBUG)
    logging.getLogger("Chapter1Test.setUp").setLevel(logging.DEBUG)
    logging.getLogger("Chapter1Test.tearDown").setLevel(logging.DEBUG)
    unittest.main()