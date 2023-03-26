from random import sample

lst = sample(range(1, 11), 10)


def bubble_sort(ls):  # O(n**2)
    for i in range(len(ls) - 1):
        for j in range(len(ls) - i - 1):
            if ls[j] > ls[j + 1]:
                s_lst = ls[j]
                ls[j] = ls[j + 1]
                ls[j + 1] = s_lst


bubble_sort(lst)
print(lst)


def binary_search(val, ls):  # find val in ls
    position = 0
    first = 0
    last = len(ls) - 1
    result_ok = False

    while first <= last and not result_ok:
        middle = (first + last) // 2
        if ls[middle] == val:
            result_ok = True
            position = middle
        else:
            if val < ls[middle]:
                last = middle - 1
            else:
                first = middle + 1

    else:
        if result_ok:
            print('Element was found!')
            print(f'Elements index position is {position}')
        else:
            print(f'Element {val} was not found in this list (.')


binary_search(9, lst)
