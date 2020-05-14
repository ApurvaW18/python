'''
Q.3.Arrange String characters such that lowercase letters should come first
Given input String of combination of the lower and upper case arrange
characters in such a way that all lowercase letters should come first.
Expected Output:  input_String = PyNaTive
arranging characters giving precedence to lowercase letters
aeiNPTvy
arranging characters giving precedence to lowercase letters:  yaivePNT 
 '''
s=input("enter the string")
a=s.split()
lower=[]
upper=[]
for i in s:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
print("".join(lower+upper))