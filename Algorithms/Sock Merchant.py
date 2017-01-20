
import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
d=set(c)
number=0
for i in d:
    number+=c.count(i)//2
print(number)