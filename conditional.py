if True :
    print('hello')
    print('how are you?')
print('===================')
x = 50
if x == 35:
    print(f'angka {x} sama dengan 35')
elif x > 35:
    print(f'{x} besar dari 35')
else:
    print("angka yang anda masukkan bukan 35")
print('===================')

cities = ['padang', 'jakarta', 'semarang', 'depok']
kota = 'padang'

if kota in cities:
    print(f'kota {kota} termasuk dalam list cities ')