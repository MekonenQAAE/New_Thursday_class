# Algorithms HW-1 : Ricky Mekonen, June 7, 20203


# Question #1 A function that compute the sum of digits in all numbers from 1 to n.
def sum_n_digits(n):
    result = 0
    original_n = n
    while n > 0:
        result += n
        n -= 1

    return f'The sum of digits from 1 to {original_n} is {result}.'

print(sum_n_digits(5))


# Question #2 Finding the max number from 3 values
def max_num_3_values(num1, num2, num3):
    max_num = num1
    if num2 > num1:
        max_num = num2
    elif num3 > num1:
        max_num = num3

    return f'The max number from {num1}, {num2} and {num3} is {max_num}.'

print(max_num_3_values(20,150,50))


# Question #3 counting odd and even digits of the whole number.
def count_odd_and_even(n):
    orginal_n = n
    even_count = 0
    odd_count = 0
    last_dig = n % 10
    while n > 0:
        if last_dig % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        n = n // 10
        last_dig = n % 10

    return f"In the whole number {orginal_n} there are {even_count} even and {odd_count} odd numbers."

print(count_odd_and_even(34560))