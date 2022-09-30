#python "ЛР 12.6.py" input2.txt
import sys
import re
#исключение
if len(sys.argv) != 2:
    print("Error!Имя файла необходимо передать в качестве аргумента.")
    quit()
#имя файла из командной строки
inf = open(sys.argv[1], "r")
frequence = dict()
line = inf.readline()
while line != "":
    line = line.replace("."," ")
    line = line.replace(",", " ")
    line = line.replace(":", " ")
    line = line.replace("!", " ")
    line = line.replace("?", " ")
    line = line.replace(" ", "")
    line = re.sub(r'|[\d]+',"", line)#регулряное выражение для удаления всех цифр
    line = line.lower() #регистр
    line = line.rstrip() # удаляет пробелы
    for letter in line:
        if letter in frequence:
            frequence[letter] += 1
        else:
            frequence[letter] = 1
    line = inf.readline()
inf.close()
for key in frequence:
    print(key, ":", frequence[key])
