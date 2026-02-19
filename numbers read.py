numbers = []
filepath = 'numbers.txt'
def read_numbers():
    global numbers
    file = open (filepath,'r')
    for content in file:
        numbers.append (int(content.strip()))
    file.close ()
read_numbers()
print (numbers)
total = 0
for num in numbers:
    total += num
print(total)