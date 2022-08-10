# nilai
# A:[80-100]
# B:[70-80]
# C:[60-70]
# D:[40-60]
# E:[0-40]
x = int(input('Masukkan nilai : '))
if  0 <= x <= 100:
    print('Nilai yang dimasukkan harus 0 - 100')
    if x >= 80 and  x <= 100:
        print(f"Skor {x} GRADE A")
    elif x >= 70 and x <= 80:
        print(f'Skor {x} GRADE B')
    elif x >= 60 and x <= 70:
        print(f'Skor {x} GRADE C')
    elif x >= 40 and x <= 60:
        print(f'Skor {x} GRADE D')
    else:
        print(f'Skor {x} GRADE E')