'''1. Selection Sort
Implement the selection sort algorithm that is sorting in descending order.
'''
def selection_Sort_descending(list_1):

    for i in range(len(list_1)):
        max_val_index = i
        for j in range(i, len(list_1)):
            if list_1[max_val_index] < list_1[j]:
                max_val_index = j
        list_1[i], list_1[max_val_index] = list_1[max_val_index], list_1[i]

    return list_1


'''
Bubble Sort
Implement the bubble sort algorithm that is sorting in descending order.
'''
def bubble_sort_descending(list_1):
    for i in range(len(list_1)):
        for j in range(1, len(list_1) - i):
            if list_1[j] > list_1[j - 1]:
                list_1[j - 1], list_1[j] = list_1[j], list_1[j-1]

    return list_1


'''
Insertion Sort
Implement the insertion sort algorithm that is sorting in descending order.
'''
def insertion_sort_descending(list_1):
    for i in range(len(list_1) - 1):
        copied_val = list_1[i + 1]
        j = i
        while j >= 0 and copied_val > list_1[j]:
            list_1[j + 1] = list_1[j]
            j -= 1
        list_1[j + 1] = copied_val

    return list_1

'''
Merge Sort
Implement the merge sort algorithm that is sorting in descending order.
'''
def merge_sort(list_1):
    if len(list_1) <= 1:
        return list_1
    mid_index = len(list_1) // 2

    return sorted_lists_merger(merge_sort(list_1[:mid_index]), merge_sort(list_1[mid_index:]))

def sorted_lists_merger(list_1, list_2):
    merged_list = []
    i = j = 0

    while i < len(list_1) or j < len(list_2):
        if len(list_1) == i:
            merged_list.append(list_2[j])
            j += 1
            continue
        if len(list_2) == j:
            merged_list.append(list_1[i])
            i += 1
            continue

        if list_1[i] > list_2[j]:
            merged_list.append(list_1[i])
            i += 1
        else:
            merged_list.append(list_2[j])
            j += 1

    return merged_list


my_list_1 = [2, 6, 4, 7, 7, 7, 3, 4, 5]
my_list_2 = [0, 0, 0, 0, 0, 0]
my_list_3 = []
my_list_4 = [1]
my_list_5 = [1, 2, 3, 4, 5, 6, 7, 8]
my_list_6 = [8, 7, 6, 5, 4, 3, 2, 1, 0]
my_list_7 = [5, 1]

# print(selection_Sort_descending(my_list_1))
# print(selection_Sort_descending(my_list_2))
# print(selection_Sort_descending(my_list_3))
# print(selection_Sort_descending(my_list_4))
# print(selection_Sort_descending(my_list_5))
# print(selection_Sort_descending(my_list_6))
# print(selection_Sort_descending(my_list_7))

# print(bubble_sort_descending(my_list_1))
# print(bubble_sort_descending(my_list_2))
# print(bubble_sort_descending(my_list_3))
# print(bubble_sort_descending(my_list_4))
# print(bubble_sort_descending(my_list_5))
# print(bubble_sort_descending(my_list_6))
# print(bubble_sort_descending(my_list_7))

# print(insertion_sort_descending(my_list_1))
# print(insertion_sort_descending(my_list_2))
# print(insertion_sort_descending(my_list_3))
# print(insertion_sort_descending(my_list_4))
# print(insertion_sort_descending(my_list_5))
# print(insertion_sort_descending(my_list_6))
# print(insertion_sort_descending(my_list_7))

print(merge_sort(my_list_1))
print(merge_sort(my_list_2))
print(merge_sort(my_list_3))
print(merge_sort(my_list_4))
print(merge_sort(my_list_5))
print(merge_sort(my_list_6))
print(merge_sort(my_list_7))

