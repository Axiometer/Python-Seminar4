# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

# Определяем функцию поиска простых множителей
def prime_check(x):
    # счетчик
    k = 0
    # нам достаточно проверить числа от 2 до sqrt(x)
    for i in range(2, int(x**0.5)+1):
        # если число делится на любое из чисел до sqrt(x),  это не простой множитель
        if (x % i == 0):
            k = k+1
    # Возвращаем либо да, либо нет
    if k == 0:
        return True
    else:
        return False

def main():
    # Пусть N будет такое
    N = 2387

    # Собственно идем по циклу до N, сли есть простой множитель, то выводим его
    print(f"Простые множители числа {N}:")
    for i in range(1, N+1):
        if N % i == 0:
            if prime_check(i):
                print(i, end=' ')

if __name__ == "__main__":
    main()