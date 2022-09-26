# Write a Python program using Sieve of Eratosthenes method for computing primes up to a specified number.
# Note: In mathematics, the sieve of Eratosthenes,one of a number of prime number sieves,
# is a simple, ancient algorithm for finding all prime numbers up to any given limit.


def sieve_of_eratosthenes(n):
    not_prime_numbers = []
    for i in range(2, n+1):
        if i not in not_prime_numbers:
            print(i)
            for j in range(i*i, n+1, i):
                not_prime_numbers.append(j)


print(sieve_of_eratosthenes(20))
