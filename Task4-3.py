 # Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

 # импорт модуля рандомизатора
from random import randint

# функция герерирования случайного списка из n элементов в диапазоне от -10 до 10
def generate_list(n):
    generated_list = []
    for _ in range(n):
        generated_list.append(randint(-10,10))
    return generated_list

def main():
    my_list = generate_list(13)
    my_set = set(my_list)

    print(*my_list)
    print(*my_set)

if __name__ == "__main__":
    main()