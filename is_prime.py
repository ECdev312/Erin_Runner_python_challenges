def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(2))   # Output: True
print(is_prime(4))   # Output: False
print(is_prime(17))  # Output: True
print(is_prime(20))  # Output: False
print(is_prime(1))   # Output: False
print(is_prime(0))   # Output: False
print(is_prime(-5))  # Output: False
print(is_prime(29))  # Output: True
