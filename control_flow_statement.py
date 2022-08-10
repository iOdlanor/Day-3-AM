# continue
i = 0
while i <=10:
    i += 1      # sama dengan i = i + 1
    if i in [7,8,9]:
        continue
    print(i)
print('=' *50)
# break
i = 0
while i <=10:
    i += 1      # sama dengan i = i + 1
    print(i)    # letak print mempengaruhi nilai output
    if i == 8:
        break
print('=' *50)
x=0
while x <=10:
    x += 1      # sama dengan i = i + 1
    if x == 8:
        break
    print(x)    # letak print mempengaruhi nilai output