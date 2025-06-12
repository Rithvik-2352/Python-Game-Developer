rgb=(255,255,255)
#packing ^
print (rgb [0])
#rgb [0] = 120 Cannot change a tuple
rgb=(220,255,213)
#only possible way to change data (redclare or reassign items) ^
rgb = 220,215,213
#pack ^
r,g,b=rgb
#unpacking ^
print (r)
tuple_1 = ((1,2,3),[4,5,6],"seven", "eight" ,"nine")
#make nested items in tuple
print ([tuple_1[1:3]])
print(tuple_1[2][2])
#access their index ^
tuple_1[1][1]=10
if "eight" in tuple_1:
    print ("yes")
else:
    print ("no")
for data in tuple_1:
    print (data)