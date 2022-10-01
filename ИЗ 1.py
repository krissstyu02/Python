# #Задание 7. В файле записана последовательность натуральных чисел.
# Гарантируется, что все числа различны. Из этой последовательности нужно
# выбрать три числа, чтобы их сумма делилась на 3 и была наименьшей. Какую
# наименьшую сумму можно при этом получить?
# Входные данные: Даны два входных файла: файл A (7a.txt) и файл B
# (7b.txt), каждый из которых содержит в первой строке количество чисел 𝑁
# (1 ≤ 𝑁 ≤ 100000). Каждая из следующих 𝑁 строк содержит одно натуральное
# число, не превышающее 108

A = open('7a.txt',"r")
B = open('7b.txt',"r")

s = A.readlines()
n = int(s[0])
m0 = [ 1 for i in range(4)]
m1 = [1 for i in range(4)]
m2 = [1 for i in range(4)]
for i in range(1, 4):
    m0[i] = 100000000
    m1[i] = 100000000
    m2[i] = 100000000
for i in range(1, n + 1):
    x = int(s[i])
    if x % 3 == 0:
        if x < m0[1]:
            m0[3] = m0[2]
            m0[2] = m0[1]
            m0[1] = x
        elif x < m0[2]:
            m0[3] = m0[2]
            m0[2] = x
        elif x > m0[3]: m0[3] = x
    elif x % 3 == 1:
        if x < m1[1]:
            m1[3] = m1[2]
            m1[2] = m1[1]
            m1[1] = x
        elif x < m1[2]:
            m1[3] = m1[2]
            m1[2] = x
        elif x < m1[3]: m1[3] = x
    elif x % 3 == 2:
        if x < m2[1]:
            m2[3] = m2[2]
            m2[2] = m2[1]
            m2[1] = x
        elif x < m2[2]:
            m2[3] = m2[2]
            m2[2] = x
        elif x > m2[3]: m2[3] = x
sum0 = m0[1] + m0[2] + m0[3]
sum1 = m1[1] + m1[2] + m1[3]
sum2 = m2[1] + m2[2] + m2[3]
sum12 = m0[1] + m1[1] + m2[1]
if (sum0 < sum1) and (sum0 < sum2) and (sum0 < sum12): print(sum0)
elif (sum1 < sum0) and (sum1 < sum2) and (sum1 < sum12): print(sum1)
elif (sum2 < sum1) and (sum2 < sum0) and (sum2 < sum12): print(sum2)
else: print('Сумма элементов файла А=',sum12)

s = B.readlines()
n = int(s[0])
m0 = [1 for i in range(4)]
m1 = [1 for i in range(4)]
m2 = [1 for i in range(4)]
for i in range(1, 4):
    m0[i] = 100000000
    m1[i] = 100000000
    m2[i] = 100000000
for i in range(1, n + 1):
    x = int(s[i])
    if x % 3 == 0:
        if x < m0[1]:
            m0[3] = m0[2]
            m0[2] = m0[1]
            m0[1] = x
        elif x < m0[2]:
            m0[3] = m0[2]
            m0[2] = x
        elif x > m0[3]: m0[3] = x
    elif x % 3 == 1:
        if x < m1[1]:
            m1[3] = m1[2]
            m1[2] = m1[1]
            m1[1] = x
        elif x < m1[2]:
            m1[3] = m1[2]
            m1[2] = x
        elif x < m1[3]: m1[3] = x
    elif x % 3 == 2:
        if x < m2[1]:
            m2[3] = m2[2]
            m2[2] = m2[1]
            m2[1] = x
        elif x < m2[2]:
            m2[3] = m2[2]
            m2[2] = x
        elif x > m2[3]: m2[3] = x
sum0 = m0[1] + m0[2] + m0[3]
sum1 = m1[1] + m1[2] + m1[3]
sum2 = m2[1] + m2[2] + m2[3]
sum12 = m0[1] + m1[1] + m2[1]
if (sum0 < sum1) and (sum0 < sum2) and (sum0 < sum12): print(sum0)
elif (sum1 < sum0) and (sum1 < sum2) and (sum1 < sum12): print(sum1)
elif (sum2 < sum1) and (sum2 < sum0) and (sum2 < sum12): print(sum2)
else: print('Сумма элементов файла B=',sum12)