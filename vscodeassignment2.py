def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * 2, n + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime

def super_primes(n):
    is_prime = sieve_of_eratosthenes(n)
    primes = [i for i, prime in enumerate(is_prime) if prime]
    super_primes = []
    for prime in primes:
        if is_prime[len(super_primes) + 1]:  # Check if the position is also prime
            super_primes.append(prime)
    return super_primes

n = 241
super_primes_list = super_primes(n)
print("Super-Primes less than or equal to", n, "are:", super_primes_list)
