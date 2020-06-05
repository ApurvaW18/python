'''
1.Python program to Swap Keys and Values in Dictionary.
'''


d={"Kiran":"Python","Shivani":"SQL","Kalyani":"Java","Swara":"AWS"}
print(d)
a={val:key for key,val in d.items()}
print(a)


di={}
d1=d.keys()
print(d1)
d2=d.values()
print(d2)
d1,d2=d2,d1
print(d1)
print(d2)
di[d1]=d2
print(di)



dict={}
for keys,values in d.items():
    dict[values]=keys
print(dict)
