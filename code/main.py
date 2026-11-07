from hero import Archer, Paladin
from inventory import Inventory
from items import Sword, HealthPotion
from boss import Boss


hero = Archer("Леголас")

inventory = Inventory()
sword = Sword()
potion = HealthPotion()

inventory.add_item(sword)
inventory.add_item(potion)
inventory.show_items()

hero.attack += sword.attack_bonus

boss = Boss()

print("\n⚔️ БИТВА С БОССОМ!")
print(f"{hero.name} против {boss.name}")

while hero.is_alive() and boss.is_alive():

    damage = hero.attack_enemy()
    boss.health -= damage

    print(f"\nГерой нанес {damage} урона!")
    print(f"Здоровье босса: {max(0, boss.health)}")

    if boss.is_alive():
        hero.take_damage(boss.attack)
        print(f"Здоровье героя: {hero.health}")

if hero.is_alive():
    print("\n🏆 ПОБЕДА! Дракон повержен!")
else:
    print("\n💀 Герой проиграл!")