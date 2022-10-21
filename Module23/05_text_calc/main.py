def operations_calc(operation_list):
    if operation_list[1] == '+':
        result = int(operation_list[0]) + int(operation_list[2])
    if operation_list[1] == '-':
        result = int(operation_list[0]) - int(operation_list[2])
    if operation_list[1] == '*':
        result = int(operation_list[0]) * int(operation_list[2])
    if operation_list[1] == '/':
        result = int(operation_list[0]) / int(operation_list[2])
    if operation_list[1] == '//':
        result = int(operation_list[0]) // int(operation_list[2])
    if operation_list[1] == '%':
        result = int(operation_list[0]) % int(operation_list[2])
    return result

def error_handling(operations_list):
    operands = {'+', '-', '*', '/', '//', '%'}
    if operations_list[1] not in operands or not operations_list[0].isdigit() or not operations_list[2].isdigit() or len(operations_list) != 3:
        raise SyntaxError


def text_calculator(file_calc):
    with open(file_calc, 'r', encoding='utf8') as file_calc:
        total_amount = 0
        for operation in file_calc:
            if '\n' in operation:
                operation = operation[: len(operation) - 1]
            operation_list = operation.split()
            try:
                error_handling(operation_list)
                total_amount += operations_calc(operation_list)
            except (SyntaxError, ZeroDivisionError):
                question = input('Обнаружена ошибка в строке: {}    Хотите исправить? '.format(operation)).lower()
                if question == 'да':
                    operation_list = input('Введите исправленную строку: ').split()
                    total_amount += operations_calc(operation_list)
        print('Сумма результатов: {}'.format(total_amount))


text_calculator('calc.txt')