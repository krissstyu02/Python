
#ЛР2(ход конем)
a=int(input('Введите координату первой точки по вертикали='))
b=int(input('Введите координату первой точки по горизонтали='))
d=int(input('Введите координату второй точки по вертикали='))
e=int(input('Введите  координату второй точки по горизонтали='))
if a+2==d and b-1==e :
    print('True')
elif a+2==d and b+1==e :
    print('True')
elif a-2==d and b+1==e :
    print('True')
elif a-2==d and b-1==e :
    print('True')
else : print('False')



