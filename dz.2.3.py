name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# new_list = name_list.pop()
# print(' '.join(new_list.split(' ')[-1::]))
# print(name_list)
# name_2 = name_list.pop()
# print(' '.join(name_2.split(' ')[-1::]))
# name_3 = name_list.pop()
# print(' '.join(name_3.split(' ')[-1::]))
# #name_list_1 =
# print(f'Привет {new_list}!')
for i in name_list:
    print(f"Привет, {i.split()[-1].title()}!")
