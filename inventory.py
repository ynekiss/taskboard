# Місія 1: «Спорядження Героя»

inventory = []
inventory.append("Меч")
inventory.append("Щит")
inventory.append("Зілля HP")
inventory.append("Слоповий факел")

print("Вміст інвентарю:", inventory)
print("Всього предметів:", len(inventory))

# Місія 2: «Апгрейд у Коваля»
inventory[0] = "Алмазний меч"
print("Оновлений інвентар:", inventory)

# Місія 3: «Використання ресурсу»
inventory.remove("Зілля HP")
print("Після бою:", inventory)
print("Залишилося предметів:", len(inventory))

# Місія 4 (Бонус): «Система переповнення Рюкзака»
max_capacity = 5

if len(inventory) > max_capacity:
    print("⚠️ Рюкзак переповнений! Викиньте зайве!")
else:
    print("✅ Є вільне місце")