def count_vowels(s):
    counter = 0
    for char in s.lower():
        if char in ['a', 'e', 'i', 'o', 'u']:
            counter += 1
    return counter

s = 'Hello world'
result = count_vowels(s)
print(result, s)