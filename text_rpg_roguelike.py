import os
os.system("clear")
print("===========================================")
print(" ⚔️  EHOT VS CROISSANT: TEXT ROGUELIKE  ⚔️ ")
print("===========================================")


STRICT_MODE = True

print('"ЕНОТ"(Характеристики: hp = 100, atk = 15)')
print('"Голодный ЕНОТ"(Характеристики: hp = 60, atk = 25)')

choice = input("👉 Введите номер выбранного енота (1 или 2): ")

if choice == "1":
    name = 'ЕНОТ'
    hp = 100
    atk = 15
elif choice == "2":
    name = 'Голодный ЕНОТ'
    hp = 60
    atk = 25
else:
   print("\n⚠️ Ошибка детекции IQ! Обнаружен скрытый класс...") 
   name = 'Дурачонок'
   hp = 20
   atk = 6
print(f"{name}, здоровье =  {hp}, атака = {atk} ")