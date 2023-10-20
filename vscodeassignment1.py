def printsuperprimes(n, isPrime):
    isPrime[0] = isPrime[1] = False
    p = 2
    while p * p <= n:
        if isPrime[p]:
            for i in range(p * 2, n + 1, p):
                isPrime[i] = False
        p += 1

def superPrimes(n):
    isPrime = [True] * (n + 1)
    sieve_of_eratosthenes(n, isPrime)
    
    primes = []
    j = 0
    for p in range(2, n + 1):
        if isPrime[p]:
            primes.append(p)
            j += 1
    
    super_primes = []
    for k in range(j):
        if isPrime[k + 1]:
            super_primes.append(primes[k])

    return super_primes

n = 241
super_primes_list = superPrimes(n)
print("Super-Primes less than or equal to", n, "are:", super_primes_list)
