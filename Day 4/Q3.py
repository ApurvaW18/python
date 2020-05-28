
'''
3.Write a recursive function to calculate the sum of numbers from 0 to 10
Expected output: 55
'''
def recur_sum(n):
    if n==0:
        return 0
    else:
        return n+recur_sum(n-1)
print(recur_sum(20))
    
