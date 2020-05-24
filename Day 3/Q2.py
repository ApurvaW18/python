'''
2.From a list containing ints, strings and floats,make three lists to store
them separately.
'''
l=['aa','bb','cc',1,2,3,1.45,14.51,2.3]
ints=[]
strings=[]
floats=[]

for i in l:
    if (type(i))==int:
        ints.append(i)
    elif (type(i))==float:
        floats.append(i)
    else:
        strings.append(i)
print(ints)
print(strings)
print(floats)
