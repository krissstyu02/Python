#ЛР11 (является ли предком(родителем))

def check(chil, paren):
    if chil == paren:
        return True
    while chil in p_tree:
        chil = p_tree[chil] #перебираем предков
        if chil == paren:
            return True
    return False


p_tree = dict()
n = int(input('Введите количество строк='))
input('Введите строки:')
for i in range(n):
    child, parent = input().split() #ребенок родитель
    p_tree[child] = parent

m = int(input('Введите количество строк для проверки='))
for i in range(m):
    first, second = input().split()
    if check(second, first):
        print(1)  #1ый родитель 2го
    elif check(first, second):
        print(2) #второй родитель первого
    else:
        print(0)
