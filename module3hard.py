# Этот код и приведенный в задании ответ не учитывают числа,
# содержащиеся внутри строк. Если учитывать - ответ будет 101.
# Планирую написать функцию, которая будет считать сумму чисел,
# содержащихся внутри произвольных строк. С ходу не получилось:(

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
        elif isinstance(args[i], int):
            count += args[i]
        elif isinstance(args[i], dict):
            calculate_structure_sum(*args[i].items())
        else:
            calculate_structure_sum(*args[i])
#     return count
#
#
# result = calculate_structure_sum(data_structure)
# print(result) так по условиям задания, но при использовании global возврат не нужен


calculate_structure_sum(data_structure)
print(count)
