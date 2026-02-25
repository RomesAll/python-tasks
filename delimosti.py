import math

def is_divisible_by_digits(num):
    size = int(math.log10(num)) + 1
    for i in range(0, size):
        digits = (num // 10**i) % 10
        if digits != 0 and not(num % digits == 0):
            return False
    return True

number = 260
result = is_divisible_by_digits(number)
print(str(result))