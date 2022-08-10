# while <condition>:
#   <statement>
#   <statement>

#infinite loop
while True:
    print('SAWADIKHAPP')
    print('Kapunkhap')
    break

# update variabel
i = 0
while i < 5:
    print(i)
    i = i+1
print('====================')

i = 1
j = 1 
while i <= 10:
    print(f'perkalian {i}')
    while j <= 10:
        print(f'{i} x {j} = {i*j}')
        j = j + 1
    print('-' * 50)
    i = i + 1
    # j dibawah untuk mengkondisikan nilai j yg awalnya 10 jika dtmbh dgn j yg dbwah j = 11
    j = 1