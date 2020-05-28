'''
5.Write a Python function that takes a list and returns a
new list with unique elements of the first list.
Sample List : [11,22,22,33,33,33,44,55,55,66]
Unique List : [11, 22,33, 44, 55,66]

code:

1.using set
def list_unique(l):
    list_sample=set(l)
    
    unique=(list(list_sample))
    print(unique)
list_unique([11,22,22,33,33,33,44,55,55,66])


2.using append
'''
def list_unique(l):
    a=[]
    for i in l:
        if i not in a:
            a.append(i)

    return a
print(list_unique([11,22,22,33,33,33,44,55,55,66]))

