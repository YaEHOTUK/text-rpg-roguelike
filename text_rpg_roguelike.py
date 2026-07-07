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
    hero_energy = 60
elif choice == "2":
    name = 'Голодный ЕНОТ'
    hp = 60
    atk = 25
    hero_energy = 80
else:
   print("\n⚠️ Ошибка детекции IQ! Обнаружен скрытый класс...") 
   name = 'Дурачонок'
   hp = 20
   atk = 6
   hero_energy = 140
print(f"{name}, здоровье =  {hp}, атака = {atk} ")

import random

max_energy = hero_energy
current_energy = hero_energy
print(f"⚡ Текущая энергия Енота: {current_energy}/{max_energy}")


backpack = []
while current_energy >= 0:
    print("🦝🦝🦝 Енот отправляется в данж 'Помойка'...🦝🦝🦝")
    print(f"⚡ Вход оплачен! Остаток энергии: {current_energy}")
    item_type = random.randint(1, 3)
    current_energy = current_energy - 20
    if item_type == 1:
        loot_hp = random.randint(-10, -1)
        loot_atk = random.randint(10, 20)
        item_name = (f"Круассан с шоколадом (хп: {loot_hp}, атака: {loot_atk})")
    elif item_type == 2:
        loot_hp = random.randint(15, 30)
        loot_atk = random.randint(-10, -5)
        item_name = (f"Упаковка бекона (хп: {loot_hp}, атака: {loot_atk})")
    else:
        loot_hp = random.randint(-25, -15)
        loot_atk = random.randint(-20, -10)
        item_name = (f"Разложившийся кусок пиццы (хп: {loot_hp}, атака: {loot_atk})")

    backpack.append(item_name)
    print(item_name)
    print(f"\n 🟢 Содержимое сумки: {backpack}")
    action = input("\n🤔 Надеть этот артефакт? (1 — Да, 2 — Выбросить):")
    if action == "1":
        hp = hp + loot_hp
        atk = atk + loot_atk
        backpack.append(item_name)
        print(f"✅ Надето! Текущие статы {name}: hp={hp}, atk={atk}")
    else:
        print("🗑️ ЗАЧЕМ ВЫБРАСЫВАТЬ ЕДУ????? ТЫ ЧТО, 'Дурачонок'?")
