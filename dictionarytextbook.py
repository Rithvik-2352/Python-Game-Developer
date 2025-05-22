Textbooks={
    'Math':'$100', 'Physics':'$20','History':'$120'
}
Textbooks ['Physics'] =' $25'
q1=input("What is the textbook that you would like to add?")
q2=input("What is the price of the first textbook that you would like to add?")
Textbooks [q1] = q2
q3=input("What is the next textbook that you would like to add?")
q4=input("What is the price of the second textbook that you would like to add?")
Textbooks [q3] = q4
print (q2)
print (q4)
print (Textbooks)
q5=input("What is a textbook you would like to find the price of?")
print (Textbooks [q5]) 

