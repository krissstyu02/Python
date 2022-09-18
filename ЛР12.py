#ЛР 12(наиболее часто встречающиеся)
folder = "BabyNames\\"
IterBoy = "_BoysNames.txt"
IterGirl = "_GirlsNames.txt"

a=int(input('Введите начало диапазона='))
b=int(input('Введите конец диапазона='))
man = dict()
woman=dict()
while(a!=b) :
    file = open(folder + str(a) + IterBoy, "r")
    file2 = open(folder + str(a) + IterGirl, "r")
    lines = file.readlines()
    for line in lines:
        name,count = line.split()
        man[name] = man.get(name, 0) + int(count)
    lines2 = file2.readlines()
    for line in lines2:
        name2, count2 = line.split()
        woman[name] = woman.get(name, 0) + int(count)
    a+=1;
maxcount=0;
for key in man:
    if man[key]>maxcount:
        maxcount=man[key]
        manName=key
maxcount=0;
for key in woman:
    if woman[key]>maxcount:
        maxcount=woman[key]
        womanName=key

print('Наиболее часто встречающиеся имена=',manName,womanName)




