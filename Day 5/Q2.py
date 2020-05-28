'''
2.Write a Python program for sequential search (Linear search).

'''

def linear_search(a,x):
    for i in range(len(a)):
        if a[i]==x:
            return i
    


a=[1,5,4,2,8,7,9,3]
x=5
print(linear_search(a,x))
if linear_search(a,x):
    print("found")
else:
    print("Not Found")
    
