from test2.locations.location_base import LocationBase
from test2.item import Item

class LocationForest(LocationBase):
    def __init__(self):
        super().__init__(name="Лес___СкибидиДобДобЕсЕс", width=15, height=15, start_pos=(10,12))
        self.add_border_walls()
        self.map_data[13][10] = "@"
        self.map_data[4][4] = "/|\ "# Е'лочки
        self.map_data[6][8] = "/|\ "
        self.map_data[8][9] = "/|\ "
        self.map_data[3][8] = "/|\ "
        self.map_data[1][6] = "/|\ "
        self.map_data[10][3] = "/|\ "
        self.map_data[9][2] = "/|\ "
        self.map_data[12][8] = "/|\ "
        self.add_object(5, 5, Item("Трава"))
        self.map_data[5][5] = "Ш"

    def add_border_walls(self):
        for x in range(self.width):
            self.map_data[0][x] = "#"
            self.map_data[self.height-1][x] = "#"
        for y in range(self.height):
            self.map_data[y][0] = "#"
            self.map_data[y][self.width-1] = "#"
