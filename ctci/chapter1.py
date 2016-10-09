#!/usr/bin/python
# Chapter 1 Arrays and Strings
import numpy


def question1(s):
    """
    Is Unique: Implement an algorithm to determine if a string has all unique
    characters. What if you cannot use additional structures?
    :param s: string to test for all unique characters.
    :return: True if all characters are unique and False otherwise.
    """
    for char in s:
        count = 0
        for char_two in s:
            if char_two == char:
                count += 1
        if count > 1:
            return False
    return True


def question2(s_one, s_two):
    """
    Check Permutation: Given two strings, write a method to decide if one is a
    permutation of the other.
    :param s_one: string to compare
    :param s_two: string to compare
    :return: True if strings are permutations of each other
    """
    if len(s_one) != len(s_two):
        return False
    else:
        if sorted(s_one) == sorted(s_two):
            return True
        else:
            return False


def question3(s):
    """
    URLify: Write a method to replace all spaces in a string with '%20'. You
    may assume that the string has sufficient space at the end to hold the
    additional characters, and that your are given the "true" length of the
    string.
    :param s: string to "URLify"
    :return: string with spaces replaced with '%20'
    """
    return s.replace(' ', '%20')


def question4(s):
    """
    Palindrome Permutation: Given a string, write a function to check if it is
    a permutation of a palindrome. A palindrome is a word or phrase that is the
    same forwards and backwards. A permutation is a rearrangement of letters.
    The palindrome does not need to be limited to just dictionary words.
    :param s: string to check if it is a permutation of a palindrome
    :return: True if string is a permutation of a palindrome, else False.
    """
    test_string = s.replace(' ', '')
    test_string = test_string.lower()
    char_count = {c: test_string.count(c) for c in test_string}
    found_single = False
    for key in char_count.keys():
        if char_count[key] % 2 == 1 and found_single:
            return False
        elif char_count[key] % 2 == 1:
            found_single = True
    return True


def question5(s_one, s_two):
    """
    One Away: There are three types of edits that can be performed on strings:
    insert a character, remove a character, or replace a character. Given two
    strings, write a function to check if they are one edit (or zero edits)
    away.
    :param s_one:
    :param s_two:
    :return: True if the two strings are one or zero edits away from each other.
    """
    # Test equivalence
    if s_one == s_two:
        return True
    # Test lengths that make this impossible
    if (len(s_one) - len(s_two)) > 1 or (len(s_two) - len(s_one)) > 1:
        return False
    # Test add/remove
    s_one_char_count = {c: s_one.count(c) for c in s_one}
    s_two_char_count = {c: s_two.count(c) for c in s_two}
    found_diff = False
    if len(s_one_char_count.keys()) > len(s_two_char_count.keys()):
        for key in s_one_char_count.keys():
            if key not in s_two_char_count.keys() and found_diff:
                return False
            elif key not in s_two_char_count.keys():
                found_diff = True
    else:
        for key in s_two_char_count.keys():
            if key not in s_one_char_count.keys() and found_diff:
                return False
            elif key not in s_one_char_count.keys():
                found_diff = True
    return True


def question6(s):
    """
    String Compression: Implement a method to perform basic string compression
    using the counts of repeated characters. For example, the string
    aabcccccaaa would become a2b1c5a3. If the "compressed" string would not
    become smaller than the original string, your method should return the
    original string. You can assume the string has only uppercase and
    lowercase letters (a-z).
    :param s: string to compress
    :return: compressed string
    """
    if len(s) == 1:
        return s
    comp = ""
    count = 0
    for i, c in enumerate(s):
        if count == 0:
            comp += c
            count += 1
            last = c
        else:
            if c == last:
                count += 1
            else:
                comp += str(count)
                comp += c
                count = 1
                last = c
    if count > 1:
        comp += str(count)
    if len(comp) >= len(s):
        return s
    else:
        return comp


def question7(m):
    """
    Rotate Matrix: Given an image represented by an NxN matrix, where each
    pixel in the image is 4 bytes, write a method to rotate the image by 90
    degrees. Can you do this in place?
    :param m: numpy matrix of int
    :return:
    """
    return numpy.rot90(m)


def question8(m):
    """
    Zero Matrix: Write an algorithm such that if an element in an MxN matrix is
    0, its entire row and column are set to 0.
    :param m: numpy matrix of int
    :return:
    """
    i = 0
    n = numpy.zeros(m.shape)
    while i < m.shape[0]:
        j = 0
        while j < m.shape[1]:
            if 0 not in m[i, :] and 0 not in m[:, j]:
                n[i, j] = m[i, j]
            j += 1
        i += 1
    return n


def question9(s_one, s_two):
    """
    String Rotation: Assume you have a method isSubstring which checks if one
    word is a substring of another. Given two strings, s1 and s2, write code to
    check if s2 is a rotation of s1 using only one call to isSubstring
    (e.g., "waterbottle" is a rotation of "erbottlewat").
    :param s_one: string one
    :param s_two: string two
    :return: True is s_two is a rotation of s_one and False otherwise.
    """
    for i, c in enumerate(s_one):
        rotated = s_one[i:] + s_one[:i]
        if rotated == s_two:
            return True
    return False
