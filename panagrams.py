alphabet={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
while True: 
    q1=input("What is the phrase would you like to check to see if it is a panagram (type exit to stop)?").lower()
    if q1=="exit":
        break
    input_letters=set(q1)

    if alphabet-input_letters==set():
        print ("This is a panagram!")
    else: 
        print ("This isn't a panagram!")