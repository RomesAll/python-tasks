from unittest import case

str_my = 'www.Python-Academy.org'
res = []

def get_upper_char(char: str):
    return char.upper()

def get_lower_char(char: str):
    return char.lower()

mapping_upper = {
    True: get_lower_char,
    False: get_upper_char
}

for char in str_my:
    if not char.isalpha():
        res.append(char)
        continue
    res.append(mapping_upper.get(char.isupper())(char))

print(''.join(res))