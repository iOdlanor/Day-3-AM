
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69 , 113, 166]
runs = 0
odd = []


while runs <=5:
    for i in num_list:
        if i % 2 == 0:
            odd.append(i)
            runs += 1
print(odd)