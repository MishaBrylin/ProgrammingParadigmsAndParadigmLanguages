class SortStrategy:
    def sort(self, numbers):
        pass


class BubbleSortStrategy(SortStrategy):
    def sort(self, numbers):
        sorted_numbers = numbers[:]
        n = len(sorted_numbers)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if sorted_numbers[j] > sorted_numbers[j+1]:
                    sorted_numbers[j], sorted_numbers[j+1] = sorted_numbers[j+1], sorted_numbers[j]
        return sorted_numbers


class SelectionSortStrategy(SortStrategy):
    def sort(self, numbers):
        sorted_numbers = numbers[:]
        n = len(sorted_numbers)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if sorted_numbers[j] < sorted_numbers[min_idx]:
                    min_idx = j
            sorted_numbers[i], sorted_numbers[min_idx] = sorted_numbers[min_idx], sorted_numbers[i]
        return sorted_numbers



numbers = [5, 2, 8, 1, 9, 3]


bubble_sort = BubbleSortStrategy()
sorted_numbers = bubble_sort.sort(numbers)
print(sorted_numbers)

selection_sort = SelectionSortStrategy()
sorted_numbers = selection_sort.sort(numbers)
print(sorted_numbers)