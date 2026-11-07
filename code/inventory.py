class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Получен предмет: {item.name}")

    def show_items(self):
        print("\nИнвентарь:")
        for item in self.items:
            print("-", item.name)