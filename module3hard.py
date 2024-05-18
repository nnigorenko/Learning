# Добавлена функция numbers_sum_in_string, вычисляющая
# сумму чисел, содержащихся внутри произвольных строк.
# В итоге получился правильный ответ - 101. В ответе,
# приведенном в задании, не учтено число 2 в строке 'Urban2'.
# Для ответа 99 - закомментировать строку 36.
def numbers_sum_in_string(line):
    numbers_sum = 0
    sample = ''
    for i in range(len(line)):
        if line[i].isdigit():
            sample += line[i]
        else:
            if sample != '':
                numbers_sum += int(sample)
            sample = ''
    if sample != '':
        numbers_sum += int(sample)
    return numbers_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
count = 0


def calculate_structure_sum(*args):
    global count
    for i in range(len(args)):
        if isinstance(args[i], str):
            count += len(args[i])
            count += numbers_sum_in_string(args[i])  # Если закомментировать, ответ будет 99
        elif isinstance(args[i], int):
            count += args[i]
        elif isinstance(args[i], dict):
            calculate_structure_sum(*args[i].items())
        else:
            calculate_structure_sum(*args[i])
    return count


result = calculate_structure_sum(data_structure)
print(result)

