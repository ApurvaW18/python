'''
4.Accept data in two 3*3  matrix and calculate the sum of the matrices.
'''
a=[[10,20,30],[40,50,60],[70,80,90]]
b=[[90,80,70],[60,50,40],[30,20,10]]
t=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        t[i][j]=a[i][j]+b[i][j]
for k in t:
    print(k)

