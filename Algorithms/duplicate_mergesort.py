def duplicate(a):
    a.sort()
    i=0
    while i <len(a)-1:
        if a[i]==a[i+1]:
            print(a[i])
            i=i+1
        else:
            i=i+1
duplicate([1,2,1,2,2,3])
