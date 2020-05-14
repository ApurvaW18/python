'''
Q.5. Given a two list.
Create a third list by picking an odd-index element from the first list
and even index elements from second.
For Example:
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
Expected Output:
Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]
Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
'''
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
odd=list1[1::2]
print(odd)
even=list2[::2]
print(even)
print(odd+even)


