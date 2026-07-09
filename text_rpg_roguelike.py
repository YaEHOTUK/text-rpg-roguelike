import os, time
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
   hp = 80
   atk = 6
   hero_energy = 140
print(f"{name}, здоровье =  {hp}, атака = {atk} ")

import random

max_energy = hero_energy
current_energy = hero_energy
print(f"⚡ Текущая энергия {name}: {current_energy}/{max_energy}")


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

def show_header(title):
    print("===============")
    print(title)
    print("===============")

def critial_chance():
    random.randint(1, 100)
    if random.randint(1, 100) <= 10:
        return 2.5
    else:
        return 1.0

def calculate_crit(base_atk, critical_multiplier, critical_chance):
    final_damage = base_atk * critical_chance
    return final_damage

def attak():
    base_atk = atk
    critical_multiplier = 2.5
    critical_hit = base_atk * critical_multiplier
    common_hit = base_atk
    
    critical_chance = critial_chance()
    total_damage = calculate_crit(base_atk, critical_multiplier, critical_chance)
    
    # show_header("🔥 ТЕСТ КРИТА ЕНОТА 🔥")
    # print(f"💥 Должно быть больно: {total_damage} урона!!!")
    return total_damage



boss_name = 'Мусорщик'
boss_hp = 300
boss_atk = 10

print(f"\n❗ {name} спокойно рылся в мусонрном баке, пока не приехал {boss_name}! (❤️ HP: {boss_hp} | ⚔️ ATK: {boss_atk})")

while hp > 0 or boss_hp > 0:
    damage = attak()
    bar_enot = "█" * int(hp // 20) + "░" * int(10 - (hp // 20))
    bar_boss = "█" * int(boss_hp // 30) + "░" * int(10 - (boss_hp // 30))
    
    hp = hp - boss_atk
    boss_hp = boss_hp - damage
    
    print(f"\r🦝 {name}: \033[32m[{bar_enot}]\033[0m {hp} HP ({name} укусил на: {damage})| 🗑️ {boss_name}: \033[31m[{bar_boss}]\033[0m {boss_hp} HP ({boss_name} нанес урон: {boss_atk})", end="", flush=True)
    time.sleep(3)
    if hp <=0:
            print("\n🪦 GAME OVER!")
            break
    if boss_hp <= 0:
        print(f"\n🏆 Теперь {name} БОСС ЭТОЙ ПОМОЙКИ! {boss_name} садится в свой мусоровоз и уезжает!")
        break