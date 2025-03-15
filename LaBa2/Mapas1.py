MAP_SIZE = 10
WALL = '#'
PLAYER = 'P'
ENEMY = 'E'
ITEM = 'I'
EMPTY = ' '
class GameMap:
    def __init__(self, player_pos, enemy_pos, items):
        self.player_pos = player_pos
        self.enemy_pos = enemy_pos
        self.items = items

    def render(self):
        for y in range(MAP_SIZE + 2):  # +2 для границ
            for x in range(MAP_SIZE + 2):  # +2 для границ
                if x == 0 or x == MAP_SIZE + 1 or y == 0 or y == MAP_SIZE + 1:
                    print(WALL, end=' ')  # Границы
                else:
                    if (x - 1, y - 1) == self.player_pos:
                        print(PLAYER, end=' ')
                    elif (x - 1, y - 1) == self.enemy_pos:
                        print(ENEMY, end=' ')
                    elif (x - 1, y - 1) in self.items:
                        print(ITEM, end=' ')
                    else:
                        print(EMPTY, end=' ')
            print()