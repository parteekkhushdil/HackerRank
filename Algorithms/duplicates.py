def duplicate(a):
    dictionary={}
    for i in a:
        if i in dictionary:
            print(i)

        else:
            dictionary[i] = i
duplicate([1,2,1,2,3])