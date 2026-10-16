# Вариант 17.
# Дано трехзначное число. Вывести число, полученное при прочтении исходного числа справа налево.

def is_invalid_number(n: int) -> bool:
    return n > 999 or n < 100

while True:
    try:
        number = int(input("Введите трёхзначное число: "))

        if is_invalid_number(number):
            print("Некорректный ввод! По заданию нужно ввести положительное трехзначное число! Попробуйте снова!")
            continue

        first_symbol = number // 100
        second_symbol = number % 100 // 10
        third_symbol = number % 10

        # В Варианте 17 собираем число наоборот (единицы -> сотни, сотни -> единицы)
        result = (third_symbol * 100
                  + second_symbol * 10
                  + first_symbol)

        print(result)
        break  # Завершаем цикл после успешного решения

    except ValueError:
        print("Ошибка! Введите целочисленное число!")