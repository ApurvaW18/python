'''Q.1. Given a number count the total number of digits in a number For example:
    The number is 75869, so the output should be
    Reverse the following list using for loop
    list1 = [10, 20, 30, 40, 50]
    Expected output:
    50
    40
    30
    20
    10 

code:
'''

list1=[10,20,30,40,50]
a=list1.count(10)
print('count of list',a)
print('Original List:',list1)

for i in reversed(list1):
    print(i)
