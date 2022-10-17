list_1 = [int(digit) for digit in input()]

list_2 = list_1[:1]

for i in range(1, len(list_1)):
    total = list_2[i - 1] + list_1[i]
    # print(total)
    list_2.append(total)

print(list_2)
