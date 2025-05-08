Student={
    'Name':'Rithvik','Age':'13','Favorite Color':'Blue'
}
print (Student)
print (Student.keys ())
print (Student.values ())
print (Student['Age'])
#Update
Student ['Favorite Color'] = 'Green'
#Add
Student ['Hair Color'] = 'Black'
#Delete
del (Student ['Hair Color'])
print (Student)
print (Student['Favorite Color'])
#print (Student['favorite food']) | If key does not exist inside dictionary, it will output a key error.
print (len(Student))
if 'Names' in Student:
    print (Student['Name'])
#elif 'Name' not in Student:
else:
    print (Student['Age'])
for i in Student:
    print (i)
    print (Student[i])
for key,value in Student.items ():
    print (key,value)