i,j,k=input().split(' ')
i,j,k=[int(i),int(j),int(k)]
number=0
for i in range(i,j+1):
    if (abs(i-int(str(i)[::-1]))%k)==0:
        number+=1
print(number)