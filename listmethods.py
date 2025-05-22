Numbers = ['1','2','3','4','5','6','7']
Numbers [4] = '6'
while True:
    user=int(input("1. Add, 2. Rename value, 3. Print All, 4. Delete, 5. Exit"))
    if user==1:
        user1=input ("What number would you like to add?")
        Numbers.append (user1)
        print (Numbers)
    elif user==2:
        user2=int(input ("Which position would you like to replace?"))
        if user2 in range (1,len(Numbers)+1):
            user3=int(input ("Which number would you like to replace it with?"))
            Numbers [user2-1]= user3
            print (Numbers)
        else:
            user6=input (f"This number is not in the range of the list. Please input range between 1 through {len(Numbers)}" )
            Numbers [user2-1]= user3
            print (Numbers)
    elif user==3:
        print (Numbers)
    elif user==4:
        user4=input("Which number would you like to remove?")
        if user4 in Numbers:
            Numbers.remove (user4)
            print (Numbers)
        else:
            print ("This number was not on the list please pick again.")    
    elif user==5:
        break