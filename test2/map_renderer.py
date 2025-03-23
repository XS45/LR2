class MapRenderer:
    def __init__(self, location, player, enemy):
        self.location = location
        self.player = player
        self.enemy = enemy

    def render(self):
        display_map = [row[:] for row in self.location.map_data]

        if self.enemy is not None:
            if (0 <= self.enemy.y < len(display_map)) and (0 <= self.enemy.x < len(display_map[0])):
                display_map[self.enemy.y][self.enemy.x] = "E"

        if (0 <= self.player.y < len(display_map)) and (0 <= self.player.x < len(display_map[0])):
            display_map[self.player.y][self.player.x] = "Ы"
        for row in display_map:
            print(" ".join(row))

