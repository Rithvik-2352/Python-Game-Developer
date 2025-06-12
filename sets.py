Set1={1,2,3,4,5,6}
print (len(Set1))
Set1.add (7)
print (Set1)
Set1.update([10,12])
print (Set1)
#Set1.remove (15)
print (Set1)
Set1.discard (111)
print (Set1)
print (Set1.pop())
print (Set1.clear())
print (Set1)
#Set operations
#Union |
#Intersection &
#Difference -
#Symmetric Difference ^
Set1 = {1,2,3,4,5}
Set2 = {3,4,5,6,7,8}
print (Set1|Set2)
print (Set1&Set2)
print (Set2-Set1)
print (Set1^Set2)