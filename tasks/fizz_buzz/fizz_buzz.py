# Вывести на экран числа от 1 до 100
# Если число кратное 3-м заменить его на Fizz
# Если число кратное 5-и заменить его на Buzz
# Если число кратное 15-и заменить его на FizzBuzz

for i in range(1, 100):
    res = ''
    res += '' if i % 3 else 'Fizz'
    res += '' if i % 5 else 'Buzz'
    print(res if res else i)
