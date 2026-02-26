from datetime import datetime, timedelta

date_str = input().strip()  # YYYY-MM-DD
offset = int(input().strip())  # может быть отрицательным

# Выведите дату в формате YYYY-MM-DD после добавления offset дней

result = datetime.strptime(date_str, '%Y-%m-%d').date() + timedelta(offset)

print(result)