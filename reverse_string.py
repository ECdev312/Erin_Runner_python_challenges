def reverse_string(text):
    return text[::-1]

def reverse_string_loop(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

print(reverse_string("Hello, World!"))  # Output: !dlroW ,olleH
print(reverse_string_loop("Hello, World!"))  # Output: !dlroW ,olleH
print(reverse_string("Python"))  # Output: nohtyP
print(reverse_string_loop("Python"))  # Output: nohtyP