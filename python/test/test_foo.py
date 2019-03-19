from unittest import TestCase

from src.foo import foo


class TestFoo(TestCase):
    def test_foo(self):
        self.assertEqual(foo(), True)
