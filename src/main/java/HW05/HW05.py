def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_prime_numbers(start, end):
    prime_numbers = []
    for number in range(start, end + 1):
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers

start = int(input("Введите начальное число диапазона: "))
end = int(input("Введите конечное число диапазона: "))

prime_numbers = find_prime_numbers(start, end)
print("Простые числа в заданном диапазоне:", prime_numbers)

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)

def merge(left_half, right_half):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1
    merged.extend(left_half[left_index:])
    merged.extend(right_half[right_index:])
    return merged

numbers = [6, 45, 23, 67, 12, 9, 34, 77]
sorted_numbers = merge_sort(numbers)
print("Отсортированный список чисел:", sorted_numbers)