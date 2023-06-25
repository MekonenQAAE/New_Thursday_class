'''
Even First
Your input is a list of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input list).
Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]
'''

def even_first(list_1):
    insert_index = 0
    for i in range(len(list_1)):
        if list_1[i] % 2 == 0:
            list_1[insert_index], list_1[i] = list_1[i], list_1[insert_index]
            insert_index += 1

    return list_1

list_example = [2, 7, 3, 5, 6, 4, 10, 3, 2]
print(even_first(list_example))

'''
Increment a Number
Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and updates the list to represent the integer D + 1.
For example, if the input is [1, 2, 9] then you should update the list to [1, 3, 0].
'''

def increment_a_number(list_1):
    factor = 1
    add_digs = 0
    for i in range(len(list_1)):
        add_digs += factor * list_1[len(list_1) - 1 - i]
        factor *= 10

    new_num = add_digs + 1

    for j in range(len(list_1)):
        list_1[len(list_1) - 1 - j] = new_num % 10
        new_num = new_num // 10

    return list_1

my_list_1 = [0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9]
print(increment_a_number(my_list_1))