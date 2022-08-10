# for <temporary variabel> in <set of value>:
#   <statement>
#   <statement>
cities = ['padang', 'jakarta', 'semarang', 'depok']
cities = cities + ['Bandung', 'Bogor']
print(cities)
print('=' *50)
for nama_kota in cities:
    print(nama_kota)
    print('-'* 50)

# range (start, stop, step)
# perkalian 5 x 10
for x in range(1,11):
    print(f'5 x {x} = {5 * x}')
print('-'* 50)
# perkalian 1 - 10
for i in range(1,11):
    for j in range(1,11):
        print(f'{i} x {j} = {i * j}')
    print('-'* 50)