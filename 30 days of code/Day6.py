number=int(input().strip())

for i in range(number):
    even=''
    odd=''
    string=input().strip()
    for j in range(len(string)):
        if(j%2==0):
            even+=string[j]
        else:
            odd+=string[j]
    print(even+' '+odd)