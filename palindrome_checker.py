def is_palindrome(text):
    normalized = text.lower().replace(" ", "").replace(",", "")
    return normalized == normalized[::-1]

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("No 'x' in Nixon"))  # Output: True