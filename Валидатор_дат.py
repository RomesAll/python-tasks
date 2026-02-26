from datetime import datetime

date_str = '2024/11/1'  # произвольная строка
fmt = '%Y-%m-%d'     # например: %Y-%m-%d, %d.%m.%Y, %m/%d/%Y

# Если строка соответствует формату, выведите OK, иначе ERROR
try:
    result = 'OK' if datetime.strptime(date_str, fmt).date() else 'ERROR'
except:
    result = 'ERROR'