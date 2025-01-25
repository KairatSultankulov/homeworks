def buble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1 ):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def binary_search(val, lst):
    first = 0
    last = len(lst) - 1
    result_ok = False
    pos = -1
    while first <= last and not result_ok:
        mid = (first + last) // 2
        if lst[mid] == val:
            result_ok = True
            pos = mid
        elif lst[mid] < val:
            first = mid + 1
        else:
            last = mid - 1
    if result_ok:
        print(f'Элемент {val} найден')
    else:
        print(f'Элемент {val} не найден')



unsorted_list = [5, 4, 12, 32, 1, 9, 78, 90]
sorted_list = buble_sort(unsorted_list)
print('Sorted list:',sorted_list)

print('--------------------')
list_1 = [6, 4 ,7, 12, 44, 36, 87, 54, 24]
element_to_find = 4
binary_search(element_to_find, list_1)
element_to_find = 100
binary_search(element_to_find, list_1)


