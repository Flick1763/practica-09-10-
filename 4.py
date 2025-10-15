import time
import random

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


data = sorted(random.sample(range(1, 1000), 100))
target = random.choice(data)

start_time = time.time()
index = binary_search(data, target)
end_time = time.time()
print(f'Index: {index}, Time: {end_time - start_time:.6f} seconds')
print("Работу выполнил Брагин Артём")
#Пояснение
#binary_search реализует алгоритм бинарного поиска.
#Генерируются случайные данные, чтобы протестировать функцию поиска.
#Во время выполнения замеряется время, чтобы оценить эффективность.