
'''
1.Python Program to Read a Number n And Print the Series “1+2+…..+n= “
sample:
Case 1:Enter a number: 4
1 + 2 + 3 + 4 = 10 
Case 2:
Enter a number: 5
1 + 2 + 3 + 4 + 5 = 15
'''
a=int(input())
s=0
for i in range(1,a+1):
    s=s+i

print(s)
