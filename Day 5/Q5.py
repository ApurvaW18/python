'''
5.Iterate a given list and check if a given element already exists in a
dictionary as a key’s value if not delete it from the list.
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sampledict = {“John”:47,”Peter”:64,”Mahi”:37,”Maria”:76}
'''
r = [47, 64, 69, 37, 76, 83, 95, 97]
s= {'John':47,'Peter':64,'Mahi':37,'Maria':76}
a=[]
'''for i in r:
    for j in s.values():
        if i==j:
            r.remove(i)
print(r)
'''
for i in s.values():
    for j in r:
        if i==j:
            a.append(i)
            r.remove(j)


print(a)
print(r)

