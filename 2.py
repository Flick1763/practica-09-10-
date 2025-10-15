import itertools
def truth_table(expr):
    variables = list(set(filter(str.isalpha, expr)))
    table = []

    for values in itertools.product([False, True], repeat=len(variables)):
        context = dict(zip(variables, values))
        result = eval(expr, {}, context)
        table.append((*values, result))

    return variables, table

variables, table = truth_table('A or (B and not C)')
print(variables)
for row in table:
    print(row)  
print("Работу Выполнил Брагин Артём.")
#Пояснение
#truth_table принимает логическое выражение в виде строки.
#Использует itertools.product для генерации всех комбинаций истинностных значений переменных.
#Для каждой комбинации вычисляется результат выражения и формируется таблица истинности.