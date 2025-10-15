def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def IMPLIES(a, b):
    return not a or b

def EQUIVALENT(a, b):
    return a == b

print(AND(True, False))  # ложь
print(OR(True, False))   # правда
print(NOT(True))         #  ложь
print(IMPLIES(True, False))  # ложь
print(EQUIVALENT(True, True))  # правда
print("Работу выполнил Брагин Артём")
#Пояснение
#AND возвращает True, если оба операнда истинны.
#OR возвращает True, если хотя бы один операнд истинный.
#NOT инвертирует значение.
#IMPLIES реализует логическую импликацию.
#EQUIVALENT проверяет, равны ли значения двух операндов.