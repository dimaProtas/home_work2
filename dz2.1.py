list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# new_list = ' '.join(list_1)
# print(new_list)

# print(list_1.index('5'))
# print(list_1.index('17'))
# print(list_1.index('+5'))
#
#
# list_1.insert(list_1.index('5'), '"')
# list_1.insert(list_1.index('5') + 1, '"')
# list_1.insert(list_1.index('17'), '"')
# list_1.insert(list_1.index('17') + 1, '"')
# list_1.insert(list_1.index('+5'), '"')
# list_1.insert(list_1.index('+5') + 1, '"')
# new_list = ' '.join(list_1)
# print(new_list)
# print(new_list.title())
# for i in filter( str.isdigit , new_list) :
list_2 = []
for i in list_1:
    if i.isdigit() == True:
        list_2.extend(['"', f'{int(i):02}', '"'])
    elif i.startswith('+') or i.startswith('-'):
        if i[1:].isdigit():
            list_2.extend(['"', f'{i[0]}{int(i[1]):2}', '"'])
        else:
            list_2.append(i)
    else:
        list_2.append(i)
    print(list_2)
list_2 = ' '.join(list_2)
print(list_2)



