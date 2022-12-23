# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N
N = 2387

def prime_check(x):
    k = 0
    for i in range(2, int(x**0.5) +1):
        if (x % i == 0):
            k = k+1
    if k == 0:
        return True
    else:
        return False

for i in range(1, N+1):
    if N % i == 0:
        if prime_check(i):
            print(i)

