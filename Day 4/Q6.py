'''
6.Write a program to obtain the sum of the first and last digit of this number
2 user defined functions
1st for first digit
2nd for last digit
Example:
 Input:  5424
Output: 9
'''

def sum_a(n):
    a=n%10
    #print(a)
    while n!=0:
        b=n%10
        n=n//10
        
    #print(b)
    print(a+b)


sum_a(100)   
sum_a(5424)
sum_a(51)

