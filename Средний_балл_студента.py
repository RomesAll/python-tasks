from math import inf

# n = int(input())
# students = {}
# for _ in range(n):
#     line = input().split()
#     name = line[0]
#     marks = list(map(float, line[1:]))
#     students[name] = marks
#
# student_name = input()
marks = [1.0, 2.0, 3.0] #students.get(student_name)
result = round(sum(marks)/len(marks))
print(f'{result:.2f}')