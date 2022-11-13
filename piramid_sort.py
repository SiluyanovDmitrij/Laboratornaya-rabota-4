a = int(input('Введите количество чисел в массиве: '))
b = [0] * a
for q in range(a):
    b[q] = int(input('Введите число: '))
print(b, ' - заданный массив')
def hhh(nums, hsize, index):
    l = index
    left = (2 * index) + 1
    right = (2 * index) + 2
    if left < hsize and nums[left] > nums[l]:
        l = left
    if right < hsize and nums[right] > nums[l]:
        l = right
    if l != index:
        nums[index], nums[l] = nums[l], nums[index]
        hhh(nums, hsize, l)
def piramidka (nums):
    n = len(nums)
    for i in range(n, -1, -1):
        hhh(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        hhh(nums, i, 0)
piramidka(b)
print(b, ' - отсортированный массив')