import itertools

def is_tautology(expr, variables):
    # Проверка, является ли выражение тавтологией
    for values in itertools.product([False, True], repeat=len(variables)):
        context = dict(zip(variables, values))
        if not eval(expr, {}, context):
            return False
    return True

def is_contradiction(expr, variables):
    # Проверка, является ли выражение противоречием
    for values in itertools.product([False, True], repeat=len(variables)):
        context = dict(zip(variables, values))
        if eval(expr, {}, context):
            return False
    return True

def is_satisfiable(expr, variables):
    # Проверка, является ли выражение выполнимым
    for values in itertools.product([False, True], repeat=len(variables)):
        context = dict(zip(variables, values))
        if eval(expr, {}, context):
            return True
    return False

def check_expression(expr):
    variables = sorted(set(filter(str.isalpha, expr)))  # Извлечение переменных
    result = {
        "Tautology": is_tautology(expr, variables),
        "Contradiction": is_contradiction(expr, variables),
        "Satisfiable": is_satisfiable(expr, variables),
    }
    return result

#я зае********************
expression = "A or (not A)"  # Ввод лог выражения 
result = check_expression(expression)

print(f"Expression: {expression}")
print(f"Tautology: {result['Tautology']}")
print(f"Contradiction: {result['Contradiction']}")
print(f"Satisfiable: {result['Satisfiable']}")
print("Работу выполнил Брагин Артём")
#Пояснение
#is_tautology, is_contradiction и is_satisfiable проверяют разные аспекты логического выражения.
#Результаты показывают, является ли выражение всегда истинным, всегда ложным или хотя бы в одной комбинации истинным.