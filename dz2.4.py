prices = [57.8, 46.51, 97, 12.45, 89.4]

rubl_kop = []
for i in prices:
    rubl = int(i)
    kop = round((i - rubl) * 100)
    rubl_kop.append(f'{rubl} рублей {kop:02d} копеек')
print(' , '.join(rubl_kop))
print(sorted(rubl_kop))
print(id(rubl_kop))
print(id(prices))


