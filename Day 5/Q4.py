'''
4.Write a python program to concatenate two lists index-wise.
List1 = [“M”,”na”,”i”,”lak”]
List2 = [“y”,”me”,”s”,”han”]
Expected output:
[“My”,”name”,”is”,”lakhan”]
'''
l1 = ['m','na','i','lak']
l2=['y','me','s','han']

l3=[]
for (i,j) in zip(l1,l2):
    l3.append(i+j)
print(l3)


s=[i+j for i,j in zip(l1,l2)]
print(s)
