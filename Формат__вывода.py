a = '122231122'
len_str = len(a)
count_repeat = 1

for i, v in enumerate(a, 0):
    if i+1 < len_str and v == a[i+1]:
        count_repeat += 1
        continue
    print((count_repeat, int(v)), end=' ')
    count_repeat = 1
