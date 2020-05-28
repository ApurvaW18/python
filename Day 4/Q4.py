'''
4.Create a function showStudent() in such a way that it should accept student id,
name, and it’s college name  and if the id and
college name is missing in function call it should
show it as by default id is 1 and college name  is VITA.
'''
def showStudent(name,cllg="VITA",id=1,):
    print(name,cllg,id)
showStudent("apu","kvm",5)
showStudent("shru")
showStudent("app","VITA")

     
