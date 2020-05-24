'''
5.Write python program to print the pattern given below
Note: Take input from user
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''

a=int(input())

for i in range(a):
    for j in range(i):
        print(i,end=' ')
    print(" ")
