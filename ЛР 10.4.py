#Проверить есть ли эл в мн-ве
print('Введите значения:')
a=list(map(int,input().split()))
s=set()
for i in range(len(a)):
    if a[i] in s:
        print('YES')
    else:
        s.add(a[i])
        print('NO')
