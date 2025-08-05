# Нехай A = [(p₁, q₁), (p₂, q₂), ..., (pₙ, qₙ)] — масив пар цілих чисел.
# Кожна пара задає дріб pᵢ/qᵢ. Потрібно відсортувати масив дробів за неспаданням.
# Якщо в масиві є однакові дроби, то після сортування вони мають зберегти відносний порядок (стабільне сортування).
#

from fractions import Fraction  # Імпортуємо клас для точного представлення дробів

def sort_key(fraction_entry):
    frac_value, original_index, _, _ = fraction_entry
    # Ключ сортування: перше — саме значення дробу, друге — індекс (для стабільності)
    return (frac_value, original_index)  

n = int(input())  # Зчитуємо кількість дробів
fractions = []    # Список для зберігання кортежів: (значення дробу, індекс, чисельник, знаменник)

for i in range(n):
    numerator, denominator = map(int, input().split())  # Зчитуємо чисельник і знаменник
    frac = Fraction(numerator, denominator)             # Створюємо об'єкт Fraction
    fractions.append((frac, i, numerator, denominator))  # Додаємо до списку з індексом для стабільності

# Сортуємо за значенням дробу (і за індексом, щоб зберігати порядок для однакових дробів)
fractions.sort(key=sort_key)

# Виводимо відсортовані чисельники і знаменники
for _, _, numerator, denominator in fractions:
    print(numerator, denominator)
