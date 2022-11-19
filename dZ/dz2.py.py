import random
a = []
n = 50
g = 0
ch = []
nech = []
pol = []
otr = []
while g < n:
    rn = random.randint(-100, 100)
    a.append(rn)
    g = g + 1
for i in range(len(a)):
    if a[i] % 2 == 0:
        o = a[i]
        ch.append(a[i])
    if a[i] % 2 != 0:
        o = a[i]
        nech.append(a[i])
    if a[i] < 0:
        o = a[i]
        pol.append(a[i])
    if a[i] > 0:
        o = a[i]
        otr.append(a[i])
print("список целых четные:" , ch, "список целых нечетные:", nech , "список целых отрицательные числа:", pol, "список целых не отрицательные числа:", otr)