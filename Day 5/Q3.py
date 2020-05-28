
'''
3.Write a Python program for Binary search.
'''
a=[10,20,40,50,70,80,90,100,40,60,30]
def binary_search(a,x):
    l=0
    u=len(a)-1
    while l<=u:
        m=(l+u)//2
        if a[m]==x:
           
            return True
        else:
            if a[m]<x:
                l=m
            else:
                u=m

x=10
print(binary_search(a,x))

if binary_search(a,x):
    print("found")
else:
    print("Not Found")



