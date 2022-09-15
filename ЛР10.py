#ЛР 10
n,k = [int(x) for x in input('Введите кол-во дней и партий=').split()]
days = set()
input('Введите значения a b')
for i in range(k):
    begin,step = [int(x) for x in input().split()]
    days |= {x for x in range(begin,n+1,step) if x%7 not in [0,6]}  #объединение
print(len(days))
