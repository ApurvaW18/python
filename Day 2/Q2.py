'''
2. Write a Python program to count the number of even and odd numbers from                     a series of numbers.
Sample numbers :
 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Output :
Number of even numbers : 4
Number of odd numbers : 5
'''

n=[1, 2, 3, 4, 5, 6, 7, 8, 9]
e=0
o=0
for i in n:
    
    if i%2==0:
        e=e+1
  
    else:
        o=o+1
        

print("Number of even numbers:",e)
print("Number of odd numbers:",o)
