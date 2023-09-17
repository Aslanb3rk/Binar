def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid  # Элемент найден, возвращаем его индекс
        elif arr[mid] < target:
            left = mid + 1  # Искать справа от mid
        else:
            right = mid - 1  # Искать слева от mid

    return -1  # Элемент не найден

# Пример использования:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5

result = binary_search(arr, target)

if result != -1:
    print(f"Элемент {target} найден в позиции {result}.")
else:
    print(f"Элемент {target} не найден.")