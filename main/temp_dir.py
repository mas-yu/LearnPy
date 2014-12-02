#!/home/vagrant/anaconda/bin/python
# -*- coding: utf-8 -*-

u"""
Description of this file.
"""
__auther__ = "masaaki"
__version__ = "0.00"
__date__ = "03 12月 2014"

from sys import argv
import os
import tempfile
import shutil

##### Class template ################


class temp_dir(object):
    u"""
    Description of this class.
    """
    def __init__(self):
        pass

    def my_method(self, arg):
        u"""
        @param  arg Description of arg.
        @return Description of return value.
        """
        return arg

########################################
if __name__ == "__main__":
    print "\"argv[0]\" is running."

    fo = tempfile.mkdtemp()
    print fo
    os.makedirs('{fo}/2014/10/15/20/15'.format(fo=fo))
    os.makedirs('{fo}/2014/10/15/20/16'.format(fo=fo))
    os.makedirs('{fo}/2014/10/15/20/17'.format(fo=fo))

    # shutil.rmtree(fo)
