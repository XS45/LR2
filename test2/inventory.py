class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
        print(f"Предмет {item.name} добавлен в инвентарь.")

    def show_items(self):
        if not self.items:
            print("Инвентарь пуст.")
        else:
            print("Инвентарь:")
            for idx, item in enumerate(self.items, 1):
                print(f"{idx}. {item.name}")
