
import random
import time

# 1. СПИСОК ПРЕДМЕТОВ

items = [
    {"name": "Iron Sword", "rarity": "common", "power": 10},
    {"name": "Golden Shield", "rarity": "rare", "power": 35},
    {"name": "Magic Staff", "rarity": "legendary", "power": 90},
    {"name": "Wooden Bow", "rarity": "common", "power": 15},
    {"name": "Dragon Armor", "rarity": "legendary", "power": 100},
    {"name": "Silver Ring", "rarity": "rare", "power": 40},
    {"name": "Health Potion", "rarity": "common", "power": 5},
    {"name": "Dark Sword", "rarity": "rare", "power": 60},
    {"name": "Old Helmet", "rarity": "common", "power": 8},
    {"name": "Crystal Blade", "rarity": "legendary", "power": 85}
]


# 2. ФИЛЬТР РЕДКИХ ПРЕДМЕТОВ

rare_items = list(filter(
    lambda item: item["rarity"] in ["rare", "legendary"],
    items
))

print("=== РЕДКИЕ ПРЕДМЕТЫ ===")
for item in rare_items:
    print(item["name"], "-", item["rarity"])


# 3. ТОП-5 ПРЕДМЕТОВ

top_items = sorted(
    items,
    key=lambda item: item["power"],
    reverse=True
)[:5]

top_names = [item["name"] for item in top_items]

print("\n=== ТОП-5 ПРЕДМЕТОВ ===")
for item in top_items:
    print(item["name"], "-", item["power"])

print("Названия:", top_names)


# 4. ГЕНЕРАТОР ЛУТА

def loot_generator():
    while True:
        yield random.choice(items)


print("\n=== 10 СЛУЧАЙНЫХ ПРЕДМЕТОВ ===")

loot = loot_generator()

for i in range(10):
    print(next(loot)["name"])


# 5. ДЕКОРАТОР ЛОГИРОВАНИЯ

def log_action(func):
    def wrapper(*args, **kwargs):
        print("[LOG] Выполняется действие:", func.__name__)
        result = func(*args, **kwargs)
        print("[LOG] Действие завершено!")
        return result

    return wrapper


@log_action
def attack(enemy):
    print("Герой атакует врага:", enemy)
    return "Атака выполнена"


print("\n=== БОЙ ===")
attack("Goblin")
attack("Dragon")
attack("Skeleton")


# 6. БОНУС: ДЕКОРАТОР TIMER

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print("Время выполнения:", end - start, "секунд")

        return result

    return wrapper


@timer
def explore_dungeon():
    print("Герой исследует подземелье...")
    time.sleep(1)
    print("Подземелье исследовано!")


print("\n=== ИССЛЕДОВАНИЕ ПОДЗЕМЕЛЬЯ ===")
explore_dungeon()

print("\n=== DUNGEON CODE v1.0 ===")
print("Все задания выполнены!")
