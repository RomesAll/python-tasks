def flat(arr):
    result = []
    for i in arr:
        result.extend(i)
    return result

import ast
input_str = input().strip()
arr = ast.literal_eval(input_str)
result = flat(arr)
print(result)