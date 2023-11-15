from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculatesquareroot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Проверка числа."""
    if your_number <= 0:
        return
        message = ('Мы вычислили квадратный корень из'
                   ' введённого вами числа. Это будет:')
        print(f' {message} {calculatesquareroot(your_number)}')


calc(25.5)
