
s=input('Введите имя исходного файла=')
s1=input('Введите имя целевого файла=')
outf = open(s1 + '.txt', "w")


file = open( s + '.txt', "r")
lines = file.readlines()
k=0
for line in lines:
    k+=1
    w=str(k) + ': '+line
    outf.write(w)


