from functools import reduce


def chinese_remainder_theorem(m, a):
    sum = 0
    prod = reduce(lambda acc, b: acc * b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


residues = [1890, 923943128, 9700140639, 30034828954, 81893600223, 7453544462]
primes = [2137, 1000000007, 10000000019, 100000000003, 100000000019, 100000000057]
flag_int = chinese_remainder_theorem(primes, residues)
print(flag_int)
print(int.to_bytes(flag_int, (flag_int.bit_length() + 7) // 8, 'big'))
