N = int(input())
sum = 0
for i in range(N+1):
    if i % 3 == 0 or i % 7 == 0:
        continue
    sum += i
print(sum)