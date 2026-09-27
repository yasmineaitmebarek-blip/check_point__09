def binary_search(list, number):
    first = 0
    last = len(list) - 1
    while first <= last:
        middle = (first + last) // 2
        if list[middle] == number:
            return True
        elif list[middle] < number:
            first = middle + 1
        else:
            last = middle - 1
    return False
print(binary_search([1, 2, 3, 5, 8], 6))
print(binary_search([1, 2, 3, 5, 8], 5))
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)
print(power(3, 4))
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list
list = [29, 13, 22, 37, 52, 49, 46, 71, 56]
print(bubble_sort(list))
def merge_sort(list):
    if len(list) <= 1:
        return list
    middle = len(list) // 2
    left = list[:middle]
    right = list[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    result = result + left[i:]
    result = result + right[j:]
    return result
list = [29, 13, 22, 37, 52, 49, 46, 71, 56]
print(merge_sort(list))
def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    left = []
    right = []
    for i in range(1, len(list)):
        if list[i] < pivot:
            left.append(list[i])
        else:
            right.append(list[i])
    return quick_sort(left) + [pivot] + quick_sort(right)
list = [29, 13, 22, 37, 52, 49, 46, 71, 56]
print(quick_sort(list))