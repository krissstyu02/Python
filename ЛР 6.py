#Минимальный делитель. Дано целое число, не меньшее 2.
#Выведите его наименьший натуральный делитель, отличный от 1
#ЛР 6
x=int(input('x= '))
i = 1
while i <= x:
    i = i + 1
    if x % i == 0 and i<=9:
        print(i)
        break
else:
    print('Таких делителей не существует')



