#ЛР 3(улитка)
import math
h=int(input('Введите высоту шеста='))
a=int(input('Введите высоту поднятия='))
b=int(input('Введите высоту спуска='))
c=math.ceil((h - a - 1) / (a - b) + 2)
print('Улитка доползет на  ', c,' день')

