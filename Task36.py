# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows= 6, num_columns= 6):
    num = [[operation(x, y) for x in range (1, num_rows + 1)] for y in range(1, num_columns + 1)]
    operation_table = []
    for i in num:
        operation_table.append(num)
        print ([str(x) for x in i])

print (print_operation_table(lambda x, y: x * y))
