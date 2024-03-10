from datetime import datetime # Імпортуємо класи datetime для роботи з датами і часом

current_date = datetime.today() # Отримуємо поточну дату

def get_days_from_today(date): # Функція для знаходження різниці між датами

    while True:
        try:
            date_object = datetime.strptime(date, "%Y-%m-%d") # Перетворюємо рядок дати в об'єкт datetime
            difference = current_date.toordinal() - date_object.toordinal() # Розраховуємо різницю між поточною та заданою датою

        except ValueError: # Обробка винятків
            print("Необхідно ввести дату у форматі 'РРРР-ММ-ДД'. Спробуйте ще раз...") # Виводимо повідомлення про помилку
            return get_days_from_today(input("Введіть дату у форматі 'РРРР-ММ-ДД' ")) # Викликаємо функцію знов

        return difference # Повертаємо різницю у днях як ціле число

print(get_days_from_today(input("Введіть дату у форматі 'РРРР-ММ-ДД' "))) # Виводимо різницю між заданою датаю і поточною у вигляді цілого числа