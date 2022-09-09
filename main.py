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

