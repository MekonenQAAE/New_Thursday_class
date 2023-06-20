'''
Below The Arithmetical Mean
When given a list, the program should return a list of all the elements below the original list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]
'''

def below_rithmetical_mean(list_1):
    list_sum = 0
    below_mean = []
    for elem in list_1:
        list_sum += elem
    mean = list_sum / len(list_1)
    for elem in list_1:
        if elem < mean:
            below_mean.append(elem)

    return below_mean


my_list = [1, 3, 5, 6, 4, 10, 2, 3]
print(below_rithmetical_mean(my_list))


'''
Two Lowest Elements
When given a list of elements, find the two lowest elements.
They can be equal to each other or different.
Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
'''
def two_lowest_elements(list_1):
    list_1.sort()
    return f'{list_1[0]}, {list_1[1]}'


my_list_2 = [198, 3, 4, 9, 10, 9, 2]
print(two_lowest_elements(my_list_2))
