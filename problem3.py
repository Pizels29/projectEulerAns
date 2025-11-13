def prime(limit):
    num = 2
    primes = [2]
    while num<limit:
        if num % 2 == 0:
            num = num + 1
            continue #any even number other than 2 is not prime
        is_prime = True
        for p in primes:
            if num % p == 0:
                is_prime = False
                break
        if is_prime == True:
            primes.append(num)
        num = num + 1
    return primes

def primeFactors(n):
    pf = []
    primes = prime(n)
    i = 0
    while i < len(primes):
        p = primes[i]
        if n % p == 0:
            pf.append(p)
            n = n / p
        else:
            i = i + 1
    return pf
print(primeFactors(600851475143))

        