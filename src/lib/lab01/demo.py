from model import Apartment

House1 = Apartment(20_000_000, 80_000, "Крымская 15 к. 1 п.3 ", 100, True)
House2 = Apartment(15_000_000, 80_000, "Крымская 17 к. 1 п.3 ", 70, False)

# Демонстрация __repr__
print(House1)

# Проверка __eq__
print(House1 == House2)

# Проверка __repr__
print(repr(House1))

# # Ошибка типа
# House3 = Apartment("15_000_000", 80_000, "Крымская 17 к. 1 п.3 ", 70, False)

# # Ошибка логики
# House3 = Apartment(-200, 80_000, "Крымская 17 к. 1 п.3 ", 70, False)

# Проверка бизнес методов
House1.buy(10**10)
House1.rent(2, 10**10)

# Смена св-ва через seter
print(House1.price)
House1.price = 10_000_000
print(House1.price)