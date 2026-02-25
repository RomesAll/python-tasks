def is_palindrome(text):
    format_text = text.lower()
    return format_text == format_text[::-1]

input_text = input().strip()
result = is_palindrome(input_text)
print(result)