# Задача: Перевірка властивостей відсортованого масиву
#
# Нехай A = [a₁, a₂, a₃, ..., aₙ] — масив цілих чисел.
# Напишіть програму, яка буде перевіряти такі властивості цього масиву:
#
# • масив відсортовано за зростанням: ∀i ∈ [1..n−1] : aᵢ < aᵢ₊₁
# • масив відсортовано за спаданням: ∀i ∈ [1..n−1] : aᵢ > aᵢ₊₁
# • масив відсортовано за неспаданням: ∀i ∈ [1..n−1] : aᵢ ≤ aᵢ₊₁
# • масив відсортовано за незростанням: ∀i ∈ [1..n−1] : aᵢ ≥ aᵢ₊₁
# • всі елементи масиву однакові: ∀i ∈ [1..n−1] : aᵢ = aᵢ₊₁


# Функція для перевірки властивостей масиву
def check_array(arr):
    # Перевірка на строге зростання: кожен наступний елемент більший за попередній
    increasing = all(arr[i] < arr[i+1] for i in range(len(arr)-1))

    # Перевірка на строге спадання: кожен наступний елемент менший за попередній
    decreasing = all(arr[i] > arr[i+1] for i in range(len(arr)-1))

    # Перевірка на нестроге зростання: наступний елемент не менший за попередній
    non_decreasing = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

    # Перевірка на нестроге спадання: наступний елемент не більший за попередній
    non_increasing = all(arr[i] >= arr[i+1] for i in range(len(arr)-1))

    # Перевірка, що всі елементи однакові
    all_same = all(arr[i] == arr[0] for i in range(1, len(arr)))

    # Вивід відповідного результату залежно від властивостей
    if increasing:
        return "The array is sorted in increasing order"
    elif decreasing:
        return "The array is sorted in decreasing order"
    elif all_same:
        return "All elements in the array are the same"
    elif non_decreasing:
        return "The array is sorted in non-decreasing order"
    elif non_increasing:
        return "The array is sorted in non-increasing order"
    else:
        return "The array is unsorted"


# Зчитування кількості тестів (k) — скільки масивів потрібно перевірити
k = int(input())

# Цикл на k масивів
for _ in range(k):
    # Зчитування кількості елементів у поточному масиві
    n = int(input())

    # Зчитування самого масиву: введення через пробіл, перетворення у список цілих чисел
    arr = list(map(int, input().split()))

    # Вивід результату перевірки масиву
    print(check_array(arr))

