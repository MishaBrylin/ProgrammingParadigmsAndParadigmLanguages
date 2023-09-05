# Императивное решение будет состоять из конструкции, где мы объявляем переменную для хранения суммы, 
# а затем проходим по каждому элементу списка, добавляя его к сумме. Например, в 
# Python это может выглядеть следующим образом:

def sum_imperative(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# Декларативное решение будет состоять из одной функции, 
# которая описывает, что нам нужно сделать, но не определяет, как это сделать.
# В данном случае, мы можем использовать функцию `sum()` в Python, которая суммирует все элементы списка. Пример декларативного решения:

def sum_declarative(numbers):
    return sum(numbers)


x = [1, 2, 3, 4, 5]

print(sum_imperative(x))
print(sum_declarative(x))