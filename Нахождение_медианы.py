
def find_median_even(data: list):
    middle = len(data)//2
    median = (data[middle] + data[middle-1]) / 2
    if median % 2 == 0:
        return int(median)
    return median

def find_median_odd(data: list):
    return data[len(data)//2]

mapping = {
    0: find_median_even,
    1: find_median_odd
}

input_string = '4 1 8 5'
input_list = sorted(map(int, input_string.split()))
result = mapping.get(len(input_list) % 2)(input_list)
print(result)