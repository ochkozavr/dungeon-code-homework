class Boss:
    def __init__(self):
        self.name = "Темный дракон"
        self.health = 200
        self.attack = 20

    def is_alive(self):
        return self.health > 0