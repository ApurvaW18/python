'''
1.Write a Python program to sort a list of elements using the bubble sort                                
Algorithm.
'''
def bubble_sort(a):
    for i in range(len(a)):
        swap=False
        j=0
        while j<(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swap=True
            j=j+1
    
    print(a)
bubble_sort([4,5,4,6,7,8,1,2,3,1])

def b(a):
    for i in range (len(a)):
        for j in range(len(a)):
            
