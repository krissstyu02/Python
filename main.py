#ЛР 1
n=int(input('Количество минут= '))
x=0
y=0
if n<60 :
    y+=n
else :
    x+=n//60 # целая часть
    y+=n%60 #остаток

print("Полученное время")
print(x,y,sep=':')

#ЛР2
a=int(input('Введите 1 координату первой точки='))
b=int(input('Введите 2 координату первой точки='))
c=(a,b)
d=int(input('Введите 1 координату второй точки='))
e=int(input('Введите 2 координату второй точки='))
f=(d,e)
if int(c[1])+2==int(f[1]) and int(c[0])-1==int(f[0]) :
    print('True')
elif int(c[1])+2==int(f[1]) and int(c[0])+1==int(f[0]) :
    print('True')
elif int(c[1])-2==int(f[1]) and int(c[0])+1==int(f[0]) :
    print('True')
elif int(c[1])-2==int(f[1]) and int(c[0])-1==int(f[0]) :
    print('True')
else : print('False')

#ЛР 3
h=input('Введите высоту шеста=')
h=input('Введите высоту шеста=')
h=input('Введите высоту шеста=')

