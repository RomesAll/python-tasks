import math

s = input()
width = int(input())
group = math.ceil((len(s) / width))

for i in range(0, len(s), width):
    print(s[i:i+width])