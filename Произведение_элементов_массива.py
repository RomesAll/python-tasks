from functools import reduce
from operator import mul

numbers = list(map(int, input().split()))
result = reduce(mul, numbers)
print(result)

numbers = list(map(int, input().split()))
result = 1
for number in numbers:
    result *= number
print(result)