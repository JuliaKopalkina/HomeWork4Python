# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

N = int(input('Введите число: '))

def factorize(n):
    factors = []
    i = 2
    while i * i <= n: 
        while n % i == 0: 
            n //= i 
            factors.append(i)
        i += 1
    if n > 1:
        factors.append(n)
    return factors

print (factorize(N))