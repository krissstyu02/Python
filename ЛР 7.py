#ЛР7(на каком месте будет Петя)
input('Введите рост учеников')
a = [int(s) for s in input().split()]
x = int(input('Введите рост Пети='))
num = 0
while num < len(a) and a[num] >= x:
    num+=1
print(num + 1)
