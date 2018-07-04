from unittest import TestCase


def bytes_to_str(b, encoding='ascii'):
    '''Returns a string version of the bytes'''
    raise NotImplementedError


def str_to_bytes(s, encoding='ascii'):
    '''Returns a bytes version of the string'''
    raise NotImplementedError


def little_endian_to_int(b):
    '''little_endian_to_int takes byte sequence as a little-endian number.
    Returns an integer'''
    # use the from_bytes method of int
    raise NotImplementedError


def int_to_little_endian(n, length):
    '''endian_to_little_endian takes an integer and returns the little-endian
    byte sequence of length'''
    # use the to_bytes method of n
    raise NotImplementedError