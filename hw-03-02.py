import random # Імпортуємо клас random для роботи з випадковими числами

lottery_numbers = set() # Створення порожньої множини

def get_numbers_ticket(min, max, quantity): # Створення функції з трьома параметрами
    if min > 0 and max < 1001 and quantity >= min and quantity <= max: # Перевірка валідності 

        while len(lottery_numbers) < quantity: # Поки кількість чисел у множині не буде відповідати параметру quantity
            number = int(random.uniform(min, max)) # Створення випадкового числа в діапазоні min, max
            lottery_numbers.add(number) # Додаємо число у множину
        
    return sorted(lottery_numbers) # Повернення відсортованого списку чисел множини
    
print(get_numbers_ticket(1, 20, 8)) # Виведення відсортованого списку чисел множини