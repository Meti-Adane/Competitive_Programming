#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    sum = 0
    for i in bill:
        if i != bill[k]:
            sum += i
    if (sum//2) <= b:
        print("Bon Appetit")
    else:
        print(b - (sum // 2))
nk = input().rstrip().split()

n = int(nk[0])

k = int(nk[1])

bill = list(map(int, input().rstrip().split()))

b = int(input().strip())

bonAppetit(bill, k, b)