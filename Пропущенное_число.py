def missing_number(nums):
    return  len(nums)*(len(nums)+1)//2 - sum(nums)


# Чтение входных данных
nums = [3, 0, 1]
result = missing_number(nums)
print(result)