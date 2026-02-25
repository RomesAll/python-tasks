def score_of_string(s):
    scope = 0
    for i, v in enumerate(s, start=0):
        if i == len(s) - 1:
            break
        scope += abs(ord(v) - ord(s[i+1]))
    return scope

# Чтение входных данных
s = 'hello'
result = score_of_string(s)
print(result)