# Місія 1: Детектор Отрути
loot_list = ["Меч", "Отруйне зілля", "Щит", "Зілля життя", "Лук"]

for item in loot_list:
    if item == "Отруйне зілля":
        print(f"{item}: ☠️ НЕ ПИТИ!")
    else:
        print(f"{item}: ✅ Безпечно")

print()

# Місія 2: Аукціонер Золота
loot = ["Монета", "Рубін", "Монета", "Меч", "Монета"]
coins = loot.count("Монета")
earnings = coins * 10
print("Кількість монет:", coins)
print("Загальний заробіток:", earnings, "золотих")

print()

# Місія 3 (Pro): Фільтр Легендарок
chest_items = ["Легендарний меч", "Дерев'яний щит", "Легендарний лук", "Зілля HP", "Легендарний шолом"]
legendary_vault = []

for item in chest_items:
    if "Легендарний" in item:
        legendary_vault.append(item)

print("Сейф легендарок:", legendary_vault)

print()

# Місія 4 (Hard): Сортувальник Інвентарю та Гаманець
chest = ["Монета", "Зілля життя", "Отруйне зілля", "Монета", "Легендарний шолом"]
hero = {"gold": 0, "hp": 100, "inventory": []}

for item in chest:
    if item == "Монета":
        hero["gold"] += 15
    elif "Отруйне" in item:
        hero["hp"] -= 20
        print(f"💀 Обережно! {item} забрало 20 HP!")
    else:
        hero["inventory"].append(item)

print("Герой:", hero)

print()

# Місія 5 (Boss): Оцінка Луту з Проклятими Предметами
loot = ["Срібний меч", "Проклятий перстень", "Золота чаша", "Отруйний клин", "Щит"]
prices = {"Срібний меч": 80, "Золота чаша": 120, "Щит": 50}
total_profit = 0

for item in loot:
    if "Проклятий" in item or "Отруйний" in item:
        print(f"⚠️ {item} проклятий/отруйний! Торговець його не купує.")
    elif item in prices:
        price = prices[item]
        total_profit += price
        print(f"Продано {item} за {price} монет.")

print("Підсумковий заробіток героя:", total_profit, "монет")