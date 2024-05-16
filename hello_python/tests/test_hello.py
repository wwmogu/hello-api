# import unittest
# import sys
# import os

# # Add src directory to the system path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# from hello import hello

# class TestHello(unittest.TestCase):

#     def test_hello(self):
#         self.assertEqual(hello("world"), "Hello from Python, world!")
#         self.assertEqual(hello("Dong"), "Hello from Python, Dong!")

# if __name__ == '__main__':
#     unittest.main()

import pytest
from hello import hello

def test_hello():
    assert hello("world") == "Hello from Python, world!"
    assert hello("Dong") == "Hello from Python, Dong!"