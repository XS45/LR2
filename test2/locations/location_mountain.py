from test2.locations.location_base import LocationBase
from test2.item import Item

class LocationMountain(LocationBase):
    def __init__(self):
        super().__init__(name="Горыыыыыыыыыыыыыы", width=15, height=15, start_pos=(2,7))
        self.add_border_walls()
        self.map_data[7][1] = "@"
        self.add_object(4, 4, Item("Шкура"))# шкура(бывшая) для сбора шкур
        self.add_object(5, 5, Item("Шкура"))
        self.map_data[6][3] = "o" # Камни
        self.map_data[2][4] = "o"
        self.map_data[4][5] = "o"
        self.map_data[1][13] = "o"
        self.map_data[13][2] = "o"
        self.map_data[11][4] = "o"
        self.map_data[8][5] = "o"
        self.map_data[6][7] = "o"
        self.map_data[6][10] = "o"
        self.map_data[10][9] = "o"
        self.map_data[8][9] = "o"
        self.map_data[11][11] = "o"
        self.map_data[10][6] = "o"
        self.add_object(7, 7, Item("Трава"))
        self.map_data[7][7] = "Ш"

    def add_border_walls(self):
        for x in range(self.width):
            self.map_data[0][x] = "#"
            self.map_data[self.height-1][x] = "#"
        for y in range(self.height):
            self.map_data[y][0] = "#"
            self.map_data[y][self.width-1] = "#"
