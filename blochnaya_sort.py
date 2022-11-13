a = int(input('Введите количество чисел в массиве: '))
b = [0]*a
for p in range(a):
    b[p] = int(input('Введите число: '))
print(b, ' - ваш массив')
def vstavka_sort(c):
    for i in range (1, len (c)):
        var = c[i]
        j = i - 1
        while (j >= 0 and var < c[j]):
            c[j + 1] = c[j]
            j = j - 1
        c[j + 1] = var
def blochnaya_sort(b):
    maxznach = max(b)
    size = maxznach / len(b)
    bloki = []
    for x in range(len(b)):
        bloki.append([])
    for i in range(len(b)):
        j = int(b[i] / size)
        if j != len(b):
            bloki[j].append(b[i])
        else:
            bloki[len(b) - 1].append(b[i])
    for z in range(len(b)):
        vstavka_sort(bloki[z])
    rezult = []
    for x in range(len(b)):
        rezult = rezult + bloki[x]
    return rezult
print(blochnaya_sort(b), ' - отсортированный массив')
