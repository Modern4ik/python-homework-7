# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def get_value_from_user(message: str) -> int:
    flag = True

    while flag:
        try:
            user_value = int(input(message))

            if user_value < 1:
                raise ValueError
            else:
                flag = False
        except ValueError:
            print('Введите целое число, большее или равное 1!')
    
    return user_value

def print_operation_table(operation, rows: int, columns: int) -> None:
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            print(operation(i, j), end = ' ')

        print('\n')

###################################################################################

rows_numb = get_value_from_user('Введите кол-во строк: ')
columns_numb = get_value_from_user('Введите кол-во столбцов: ')

print_operation_table(lambda i, j: i * j, rows_numb, columns_numb)