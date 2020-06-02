#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    open_paren = set('([{')
    matches = [ ('(',')'), ('[',']'), ('{','}') ]
    stack = []

    for p in s:
        if p in open_paren:
            stack.append(p)
        else:
            if len(stack) == 0:
                return "NO"
            last_open = stack.pop()
            if (last_open,p) not in matches:
                return "NO"

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"