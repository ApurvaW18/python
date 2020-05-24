'''
5.Write a Python program to check whether a given number is a narcissistic number
or not.
For example, 371 is a narcissistic number; it has three digits,
and if we cube each digits  33 + 73 + 13 the sum is 371.
Other 3-digit narcissistic numbers are
153 = 13 + 53 + 33
370 = 33 + 73 + 03
407 = 43 + 03 + 73.
There are also 4-digit narcissistic numbers,
some of which are 1634, 8208, 9474 since
1634 = 14+64+34+44
8208 = 84+24+04+84
9474 = 94+44+74+44
'''
n=(input())
s=0
q=len(n)
t=int(n)
for i in range(q):
    a=int(n[i])**len((n))
    s=s+a
    
if t==s:
     print("number is narcissistic",s)
        #break
else:
    print("number is not narcissistic",s)
    
