def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result

print(caesar_cipher("Hello, World!", 3))  # Output: Khoor, Zruog!
print(caesar_cipher("abcXYZ", 2))          # Output: cdeZAB
print(caesar_cipher("Python 3.8", 5))      # Output: Udymts 3.8
print(caesar_cipher("Caesar Cipher!", -3)) # Output: Xxbpvo Zfmebo!
