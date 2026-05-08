# Part 1

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Part 2

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# Part 3

def compareTo(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 0
    if len(s1) == 0:
        return -1
    if len(s2) == 0:
        return 1
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    return compareTo(s1[1:], s2[1:])

print(fibonacci(5))
print(gcd(48, 18))
print(compareTo("abc", "abd"))