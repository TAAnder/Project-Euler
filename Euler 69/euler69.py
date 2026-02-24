from collections import defaultdict

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

# This dictionary contains the prime factorization of each number.
prime_dict = defaultdict(set)
for p in primes:
    for i in range(p,1000000,p):
        prime_dict[i].add(p)

# I should be able to run throught the values 1 to 1 million now and use the prime factorizations to figure out phi.
# A sample test -- 100.  I start by figuring out there are 100/2 = 50 relative non-primes that contain a 2.
# I then figure out there are 100/5 = 20 relative nonprimes that contain a 5.  Half of those are already taken care of with the 2, so I add 10. (5, 15, 25, 35...)
# Combining together, I have 60 relative non-primes and 40 relative primes.  

# Let's try a more complicated example like 30.  It contains primes 2, 3, 5.  30/2 = 15.  30/3 = 10/2 = 5.   30/5 = 6/3 = 2/2 = 1.  
# 30 should contain 15+5+1 relative non-primes.  That's 21 relative non-primes and 9 relative primes.  Now let's see:
# 2,4,6,8,10,12,14,16,18,20,22,24,26,28,30
# 3,6,9,12,15,18,21,24,27,30.  Subtract out half of these and the oens that remain are 3,9,15,21,27
# 5,10,15,20,25,30.  Get rid of half: 5,15,25.  Get rid of 1 more. 5, 25
# The complete list is 22 long... FAIL


# for n in range(2,1000):
#     if n%10000 ==0:
#         print(n)
#     if n not in prime_set:
#         prime_factors = []
#         n_test = n
#         i = 0
#         while primes[i] <= n_test:
#             if n_test%primes[i] == 0:
#                 prime_factors.append(primes[i])
#                 while n_test%primes[i] == 0:
#                     n_test /= primes[i]
#             i += 1
#         prime_dict[n] = prime_factors

# print(prime_dict)
                
        # print(f'The primes of {n} are {prime_factors}')
        # rp = n-1
        # for i in range(2,n):
        #     for p in prime_factors:
        #         if p > i:
        #             break
        #         if i%p == 0:
        #             rp -=1
        #             break
        # if n/rp > best_phi_ratio:
        #     best_n = n
        #     best_phi_ratio = n/rp
        #     print(f"new best {n=} with a ratio of {best_phi_ratio}")
        