'''
2.Write program to implement Selection sort.
'''

a = [16, 19, 11, 15, 10, 12, 14]

i = 0
while i<len(a):
    s=min(a[i:])
    print(s)
    j=a.index(s)
    a[i],a[j] = a[j],a[i]
    i=i+1
print(a)

def selectionSort(array, size):

    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
