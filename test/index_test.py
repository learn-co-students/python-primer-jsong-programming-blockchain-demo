from unittest import TestCase, TestSuite, TextTestRunner
from ipynb.fs.full.index import *

class HelperTest(TestCase):

    def test_bytes(self):
        b = b'hello world'
        s = 'hello world'
        self.assertEqual(b, str_to_bytes(s))
        self.assertEqual(s, bytes_to_str(b))

    def test_little_endian_to_int(self):
        h = bytes.fromhex('99c3980000000000')
        want = 10011545
        self.assertEqual(little_endian_to_int(h), want)
        h = bytes.fromhex('a135ef0100000000')
        want = 32454049
        self.assertEqual(little_endian_to_int(h), want)

    def test_int_to_little_endian(self):
        n = 1
        want = b'\x01\x00\x00\x00'
        self.assertEqual(int_to_little_endian(n, 4), want)
        n = 10011545
        want = b'\x99\xc3\x98\x00\x00\x00\x00\x00'
        self.assertEqual(int_to_little_endian(n, 8), want)
