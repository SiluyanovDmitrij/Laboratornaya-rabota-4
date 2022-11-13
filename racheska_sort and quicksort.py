import timeit
a = int(input('Введите количество чисел в массиве: '))
n = [0]*a
for i in range(a):
    n[i] = int(input('Введите число: '))
print(n)
q = input('Выберите метод сортировки из представленных: быстрая сортировка, сортировка "расчёской": ')
if q == 'сортировка "расчёской"':
    import rascheska_sort_module as rs
    rs.rascheska(n)
    print(n, ' - отсортированный массив')
    print('Время выполнения команды: ', timeit.timeit())
elif q == 'быстрая сортировка':
    import quicksort_module as qs
    qs.quicksort(n)
    print(n, ' - отсортированный массив')
    print('Время выполнения команды: ', timeit.timeit())
else:
    while q not in ['быстрая сортировка', 'сортировка "расчёской"']:
        q = input('Введенного метода сортировки нет в списке. Выберите метод сортировки из списка выше: ')