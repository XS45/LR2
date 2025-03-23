from map_renderer import MapRenderer
from character import Player, Enemy
from quest import QuestManager
from locations import location_village, location_forest, location_dungeon, location_mountain, location_sicrett
from inventory import Inventory
class Game:
    def __init__(self):
        self.locations = {
            "vil": location_village.LocationVillage(),
            "for": location_forest.LocationForest(),
            "dun": location_dungeon.LocationDungeon(),
            "moun": location_mountain.LocationMountain(),
            "aboba": location_sicrett.LocationSicrett()
        }
        self.current_location_key = "vil"
        self.current_location = self.locations[self.current_location_key]

        self.player = Player(x=5, y=5)
        self.enemy = Enemy(x=3, y=3)

        self.player.inventory = Inventory()
        self.renderer = MapRenderer(self.current_location, self.player, self.enemy)
        self.quest_manager = QuestManager(self.player)
        self.enemy_alive = True

    def main_menu(self):
        print("Добро пожаловать в демо-игру!")
        print("1. Обучение")
        print("2. Начать игру")
        choice = input("Выберите режим (1/2): ").strip()
        if choice == "1":
            self.tutorial_mode()
        else:
            self.start()

    def tutorial_mode(self):
        print("\nРежим обучения:")
        print("Выполняются простые команды для знакомства с управлением:")
        print("  - перемещение: W (вверх), A (влево), S (вниз), D (вправо)")
        print("  - атака врага: F")
        print("  - взаимодействие с предметами: E")
        print("  - просмотр инвентаря: I")
        print("  - переход между локациями (если вы на '@'): M")
        print("  - выход из игры: Q")
        print("Нажмите любую клавишу для начала обучения...")
        input()
        self.start()

    def start(self):
        done = False
        while not done:
            print("\nЛокация: " + self.current_location.name)
            self.renderer.render()
            self.quest_manager.show_active_quests()

            print("\nКоманды:")
            print("W - вверх, S - вниз, A - влево, D - вправо")
            print("F - Атака (если рядом враг)")
            print("E - Взаимодействие (с предметами) ")
            print("I - инвентарь")
            print("M - переход между локациями (если на '@')")
            print("Q - выход")

            command = input("Введите команду: ").upper().strip()

            if command == "Q":
                done = True
            elif command in ["W", "A", "S", "D"]:
                self.move_player(command)
            elif command == "F":
                self.attack()
            elif command == "E":
                self.interact()
            elif command == "I":
                self.player.inventory.show_items()
            elif command == "M":
                self.change_location()
            else:
                print("Непонятная команда!")

    def move_player(self, direction):
        new_x, new_y = self.player.x, self.player.y
        if direction == "W":
            new_y -= 1
        elif direction == "S":
            new_y += 1
        elif direction == "A":
            new_x -= 1
        elif direction == "D":
            new_x += 1

        if self.current_location.is_walkable(new_x, new_y):
            self.player.x, self.player.y = new_x, new_y
        else:
            print("Нельзя туда ходить!")

    def attack(self):
        if self.enemy_alive and self.are_adjacent(self.player, self.enemy):
            print(f"{self.player.name} атакует {self.enemy.name}!")
            damage = int(self.player.DMG * (100 / (100 + self.enemy.ARM)))
            self.enemy.HP -= damage
            print(f"Нанесено урона: {damage}. Остаток HP врага: {self.enemy.HP}")
            if self.enemy.HP <= 0:
                print(f"{self.enemy.name} побежден!")
                self.enemy_alive = False
                self.renderer.enemy = None
            else:
                print(f"{self.enemy.name} готовится к ответной атаке!")
        else:
            print("Врага рядом нет!")

    def interact(self):
        obj = self.current_location.get_object_at(self.player.x, self.player.y)
        if obj:
            print(f"Вы подобрали предмет: {obj.name}")
            self.player.inventory.add_item(obj)
            self.current_location.remove_object(self.player.x, self.player.y)
        else:
            print("Нечего подбирать или взаимодействовать в данной точке.")

    def are_adjacent(self, char1, char2):
        dx = abs(char1.x - char2.x)
        dy = abs(char1.y - char2.y)
        return (dx <= 1) and (dy <= 1)

    def change_location(self):
        if self.current_location.get_tile(self.player.x, self.player.y) == "@":
            print("Переход между локациями.")
            print("Доступные локации:")
            for key, loc in self.locations.items():
                print(f"{key}: {loc.name}")
            new_loc = input("Введите ключ локации: ").lower().strip()
            if new_loc in self.locations:
                self.current_location = self.locations[new_loc]
                self.current_location_key = new_loc
                self.player.x, self.player.y = self.current_location.start_pos
                self.renderer.location = self.current_location
                self.renderer.enemy = self.enemy
                self.enemy_alive = True
            else:
                print("Неверный ключ локации.")
        else:
            print("Вы не на переходной точке ('@').")
