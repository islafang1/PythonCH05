def is_prime(n):
    if n <= 1:
        return False
    for div in range(2, int(n**0.5) + 1):
        if n % div == 0:
            return False
    return True

def print_primes(n):
    for num in range(2, n):
        if is_prime(num):
            print(num)

def get_primes(n):
    plist = []
    for num in range(2, n):
        if is_prime(num):
            plist.append(num)
    return plist