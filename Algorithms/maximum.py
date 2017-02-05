a=[1,2,3,4,5]
def maximum(a,l,r):
    if(r-l)==0:
        return a[r-1]
    lmax=maximum(a,l,(l+r)/2)
    rmax = maximum(a,((l + r) / 2)+1,r)
    print (rmax,lmax)
    if rmax<lmax:
        return lmax
    else:
        return rmax
print (maximum(a,1,5))