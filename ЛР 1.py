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