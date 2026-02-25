import math

def is_happy_number(number):
    len_number = int(math.log10(number)) + 1
    first_group, second_group = 1, 1
    if len_number % 2 != 0:
        return False
    for i in range(len_number):
        digit = (number // 10**i) % 10
        if i < len_number // 2:
            first_group *= digit
        else:
            second_group *= digit
    return first_group == second_group

number = 6261
result = is_happy_number(number)
print(result)