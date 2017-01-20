n,k=input().split()
n,k=[int(n),int(k)]
costList=list(map(int,input().split()))
payed=int(input())
costList.pop(k)
actual=sum(costList)/2
if actual ==payed:
    print('Bon Appetit')
else:
    print(int(payed-actual))
