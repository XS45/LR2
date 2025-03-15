from LaBa2.Pers import Character
from LaBa2.Mapas1 import GameMap
from LaBa2.Mapas1 import MAP_SIZE

class Game:
    def __init__(self):
        self.player = Character("Tbl", 100, 50, 5, 10)
        self.enemy = Character("Vrag", 50, 0, 2, 8)
        self.map = GameMap((1, 1), (8, 8), {(3, 3): "Health", (5, 5): "Mana"})
        self.inventory = []

    def move_player(self, direction):
        x, y = self.map.player_pos
        if direction == 'w' and y > 0:  # вверх
            y -= 1
        elif direction == 's' and y < MAP_SIZE - 1:  # вниз
            y += 1
        elif direction == 'a' and x > 0:  # влево
            x -= 1
        elif direction == 'd' and x < MAP_SIZE - 1:  # вправо
            x += 1

        # Проверка на столкновение с врагом
        if (x, y) == self.map.enemy_pos:
            return (self.map.player_pos, True)  # Возвращаем старую позицию и флаг столкновения
        return ((x, y), False)

    def pick_item(self):
        if self.map.player_pos in self.map.items:
            item = self.map.items.pop(self.map.player_pos)
            self.inventory.append(item)
            print(f"Вы подобрали {item}.")
        else:
            print("Здесь нет предметов.")

    def main(self):
        while self.player.is_alive() and self.enemy.is_alive():
            self.map.render()
            action = input("Введите действие (w/a/s/d для движения, 'e' для атаки, 'pick' для подбора предмета, 'q' для выхода): ")

            if action in ['w', 'a', 's', 'd']:
                new_pos, collision = self.move_player(action)
                if not collision:
                    self.map.player_pos = new_pos
                else:
                    print("Вы не можете пройти через врага!")
            elif action == 'e':  # Атака
                if (abs(self.map.player_pos[0] - self.map.enemy_pos[0]) <= 1 and
                        abs(self.map.player_pos[1] - self.map.enemy_pos[1]) <= 1):
                    self.player.attack(self.enemy)
                    if self.enemy.is_alive():
                        self.enemy.attack(self.player)
                else:
                    print("Враг слишком далеко!")
            elif action == 'pick':
                self.pick_item()
            elif action == 'q':  # Выход из игры
                print("Вы вышли из игры.")
                break
            else:
                print("Неверная команда. Пожалуйста, попробуйте снова.")

            # Проверка на атаку врага
            if self.enemy.is_alive() and self.map.player_pos == self.map.enemy_pos:
                self.enemy.attack(self.player)

        if self.player.is_alive():
            print("Вы победили врага!")
        else:
            print("Вы погибли...")

if __name__ == "__main__":
    game = Game()
    game.main()