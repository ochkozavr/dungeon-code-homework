
import random


class Hero:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def special(self):
        return self.attack

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получил {damage} урона!")

    def is_alive(self):
        return self.health > 0


class Archer(Hero):
    def __init__(self, name):
        super().__init__(name, 120, 25)

    def special(self):
        print(f"{self.name} использует меткий выстрел!")
        return self.attack * 2

    def attack_enemy(self):
        damage = self.attack

        if random.random() < 0.25:
            damage *= 2
            print("КРИТИЧЕСКИЙ УДАР!")

        return damage


class Paladin(Hero):
    def __init__(self, name):
        super().__init__(name, 160, 20)

    def special(self):
        print(f"{self.name} использует священный удар!")
        return self.attack * 3
