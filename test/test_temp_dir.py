#!/home/vagrant/anaconda/bin/python
# -*- coding: utf-8 -*-

u"""
Description of this file.
"""
__auther__  = "masaaki"
__version__ = "0.00"
__date__    = "03 12月 2014"

from sys import argv
import unittest
from temp_dir import *

##### Unittet template ################
class temp_dirTest(unittest.TestCase):
    u"""
    Description of this TestCases.
    """
     
    def setup(self):
        pass

    def test_myMethod(self):
        foo = temp_dir()
        actual = foo.my_method(1)
        expected = 1
        self.assertEqual(actual, expected)

    def tearDown(self):
        pass

########################################
if __name__ == "__main__":
    unittest.main()  

