
class Item:
    def __init__(self, name):
        self.name = name


class Sword(Item):
    def __init__(self):
        super().__init__("Легендарный меч")
        self.attack_bonus = 15


class HealthPotion(Item):
    def __init__(self):
        super().__init__("Большое лечебное зелье")
        self.heal_amount = 50
