#ЛР8
#ОФункция степени
def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


a=float(input('Введите число='))
n=int(input('Введите степень числа='))
print('a^n=',int(power(a,n)))
