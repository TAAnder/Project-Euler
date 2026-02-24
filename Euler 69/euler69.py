# From 1-10, bests:
best_n = 6
best_phi_ratio = 3

# Calculate all of the primes up to 1000000
primes = [2,3]
for i in range(5,1000000,2):
    p = True
    for prime in primes:
        if prime > i**.5:
            break
        if i%prime == 0:
            p = False
            break
    if p:
        primes.append(i)

# Convert to a set for quick prime checking
prime_set = set(primes)
# The set contains 78498 items.


# Test only numbers that do not appear in the primes list for the totient.  check "if i in prime_set..."

# I think I need to prime factorize each number I test.  Run through up to root n checking primes from the list. (order is important so need the LIST not SET)

# Then I need some kind of seive of eratosthenes list structure up to length n.  Run through it with all of the prime factors of n.

prime_dict = {}

for n in range(2,1000000):
    if n%10000 ==0:
        print(n)
    if n not in prime_set:
        prime_factors = []
        for p in primes:
            if p > n**.5:
                break
            if n%p == 0:
                prime_factors.append(p)
        # print(f'The primes of {n} are {prime_factors}')
        rp = n-1
        for i in range(2,n):
            for p in prime_factors:
                if p > i:
                    break
                if i%p == 0:
                    rp -=1
                    break
        if n/rp > best_phi_ratio:
            best_n = n
            best_phi_ratio = n/rp
            print(f"new best {n=} with a ratio of {best_phi_ratio}")
        