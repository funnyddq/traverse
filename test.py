#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
import sys


GAMMA = '\x14\x0f\x0f\x10\x11\xb5"=yXw\x17\xff\xd9\xec:'

def dec(i):
    return i - 1


a = []
for i in range(0, 16):
    a.append(random.randint(1, 100))
b = []
for i in range(0, 16):
    b.append(random.randint(1, 100))

# zipped = zip(GAMMA, a)
# print zipped
z = map('{:02x}'.format, [int(x, 16) + y for (x, y) in zip(GAMMA, a)])
print z
xx = ''.join(z)
print xx
