Capitals={
    'India':'New Delhi'
}
print (Capitals)
while True:
    user=int(input("1. Add, 2. Rename value, 3. Print All, 4. Delete, 5. Exit"))
    if user==1:
        key=input("Enter country name:")
        value=input ("Enter capital name:")
        Capitals [key] = value
    elif user==2:
        key=input("Enter country name replacement:")
        if key in Capitals:
            value=input("Enter  capital name replacement:")
            Capitals [key] = value
    elif user==3:
        print (Capitals)
    elif user==4:
        user=input("Which country would you like to remove from the dictionary?")
        if user in Capitals:
            del (Capitals [user])
    elif user==5:
        break
    