
def fizz_buzz() -> None:
    """Выводит числа от 1 до 100, заменяя кратные
    3 на Fizz, 5 на Buzz, 3 и 5 на FizzBuzz
    """

    for i in range(1, 100):
        res = ''
        res += '' if i % 3 else 'Fizz'
        res += '' if i % 5 else 'Buzz'
        print(res if res else i)


if __name__ == '__main__':
    fizz_buzz()
