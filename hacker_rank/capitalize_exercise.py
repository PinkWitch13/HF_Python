#!/bin/python3

import math
import os
import random
import re
import sys

"""Given a full name, your task is to capitalize 
    the name appropriately.  """

s = 'chris alan'

def solve(s):
    s_to_change = s.split(' ')
    print(s_to_change)
    correct_s =[]
    for name in s_to_change:
        correct_s.append(name.capitalize())
    return ' '.join(correct_s)
    

print(solve(s))