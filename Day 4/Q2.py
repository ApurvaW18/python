'''
2.Write a Python program to detect the number of
local variables declared in a function.
'''
def local_funt():
    x = 10
    y = 2.5
    z="local"
    

print(local_funt.__code__.co_nlocals)
local_funt()
def local_funt():
    x = 10
    y = 2.5
    z="local"
    print(len(locals()))
local_funt() 
