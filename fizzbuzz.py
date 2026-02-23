def fizzbuzz(n: int) -> list:
    result = []
    for i in range(1, n+1):
        if not (i % 3 == 0 or i % 5 == 0):
            result.append(str(i))
            continue
        temp = ''
        if i % 3 == 0:
            temp += "Fizz"
        if i % 5 == 0:
            temp += "Buzz"
        result.append(temp)
    return result

n = 15
result = fizzbuzz(n)
print(result)