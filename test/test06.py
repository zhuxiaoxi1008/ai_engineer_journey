def is_odd(num):
    return num % 2 == 1

# print(list(filter(is_odd,  range(20)))  )
# print([ i for i in range(20) if i % 2 == 1])    


def gen_primes():
    for num in range(2, 100):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            yield num

print(list(gen_primes()))


def gen_primes_2(limit=100):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1

    for num in range(2, limit + 1):
        if is_prime[num]:
            yield num

print(list(gen_primes_2()))
