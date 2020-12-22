#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
print(*arr[::-1])
"""reversed_array = []
for i in range(n) :
    reversed_array.append(arr[n-i-1])

#outputstring = ''
#for i in range(len(reversed_array)):
 #   outputstring += str(reversed_array[i]) + ' '
#print(outputstring)
    
#print(' '.join(str(i) for i in reversed_array))
"""
