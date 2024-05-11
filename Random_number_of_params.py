# Random number of parameters:
def test_rand(*params):
    print(params)
    print(*params)


test_rand(5, 'parameter', 2-1j, [4, 5, 6], ('ONE', 'TWO'), { 'cat', 'dog'})


# Recursion:
def factorial(n):
    if n < 0:
        return 'Ошибка'
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


for number in range(-1, 6):
    print("Факториал", number, "=", factorial(number))


