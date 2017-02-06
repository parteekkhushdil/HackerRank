#!/bin/python3

import sys

n = int(input().strip())
binary = []
while n > 0:
    remainder = int(n % 2)
    # print (remainder)
    n = int(n / 2)
    binary.append(remainder)
current = 0
longest = 0
# print(binary)
for i in binary:
    if i == 1:
        current += 1
    else:
        longest = max(current, longest)
        current = 0
print(max(current, longest))
