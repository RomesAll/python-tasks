from math import inf

n = int(input())
scores = list(map(int, input().split()))
max_numbers = [-inf, ]
for number in scores:
    if max_numbers[-1] == number:
        continue
    if max_numbers[-1] < number:
        max_numbers.append(number)
        continue
    if max_numbers[-2] < number < max_numbers[-1]:
        max_numbers.insert(-1, number)
        continue
print(max_numbers[-2])