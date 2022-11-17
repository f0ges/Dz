import random
a = []
i = int(input("Введите длинну массива"))
dl = 0
pol = 0
otr = 0
nul = 0
while dl < i:
    rn = random.randint(-1000, 1000)
    a.append(rn)
    dl += 1
for i in range(len(a)):
    if a[i] < 0:
        otr  += 1
    elif a[i] > 0:
        pol += 1
    elif a[i] == 0:
        nul += 1
print(f"В данном массиве: {pol} положительных, {otr} отрицательных, {nul} нулей.")
print("Максимальное число массива", max(a))
print("Минимальное число массива", min(a))
print("Массив:", a)
