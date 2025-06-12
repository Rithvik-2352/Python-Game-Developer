Numbers = [5, 12, -3, 8, 0, 19, -7]

min_num = Numbers[0]
max_num = Numbers[0]

for num in Numbers:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print("Minimum number:", min_num)
print("Maximum number:", max_num)