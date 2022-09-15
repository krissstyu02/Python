#ЛР9
#Поменять столбцы.
def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]

n=int(input('Введите кол-во строк='))
a = [[int(y) for y in input().split()] for l in range(n)]
i=int(input('Введите номер первого столбца для замены='))
j=int(input('Введите номер второго столбца для замены='))
swap_columns(a, i, j)
for row in a:
    print(' '.join([str(elem) for elem in row]))


