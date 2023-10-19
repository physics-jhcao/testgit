#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhou jiyang
@contact: zjy777@mail.ustc.edu.cn
@file: 01.注释-注解-docstring.py
@time: 2022/10/23/0023 11:37:00
@desc:
'''
import pandas as pd
import numpy as np


def test(x:int)->int:
    # this is the demonstration of notes,
    # notes is best to put at the start of functions or classes,
    # but it's recommended to use docstrings.
    # the annotation for function's params and returns are not defined but only noted,
    # this means if you send a string or a float param in this test function,
    # it will not cause errors.
    '''
    This function is only a test to demonstrate docstrings, the docstrings must put closed to the
    name of functions or classes

    :param x: any string to demonstrate
    :return: return test
    '''
    return x*2

#输出对应函数的docstring
print(test.__doc__)
#输出对应函数的注解
print(test.__annotations__)