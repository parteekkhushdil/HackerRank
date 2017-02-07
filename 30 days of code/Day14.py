class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    maximumDifference = 0

    def computeDifference(self):
        a.sort()
        Difference.maximumDifference = a[len(a) - 1] - a[0]
        # print('hi'+str(maximumDifference))
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)