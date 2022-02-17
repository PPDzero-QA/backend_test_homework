"""Импорт sqrt из math."""
from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """
    Выводит текст с вычисленым квадратным корнем.

    Если значение <=0, выводится только message.
    """
    root = calculate_square_root(your_number)
    if your_number <= 0:
        return
    text = ('Мы вычислили корень квадратный из введенного вами числа.'
            ' Это будет: ')

    print(f'{text}{root}')


print(message)
calc(25.5)
