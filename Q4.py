'''
Q.4. Given a string, return the sum and average of the digits that
appear in the string, ignoring all other characters
For Example: –  sumAndAverage
("English = 78 Science = 83 Math = 68 History = 65")= sum 294 Percentage is 73.5
Solution: import r
'''
import re
s=("English = 78 Science = 83 Math = 68 History = 65")
print(s)
a = [int(num) for num in re.findall(r'\d+',s)]
#a=re.findall(r'\d+',s)
#print(" ".join(a))
print(a)
sum1=0
for i in a:
    sum1=sum1+i
print(sum1)
p=sum1/len(a)
print(p)
