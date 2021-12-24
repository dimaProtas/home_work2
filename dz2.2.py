list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

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



