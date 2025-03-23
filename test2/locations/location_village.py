from test2.locations.location_base import LocationBase
from test2.item import Item

class LocationVillage(LocationBase):
    def __init__(self):
        super().__init__(name="Деревня_17", width=15, height=15, start_pos=(6,6))
        self.add_border_walls()
        self.map_data[13][7] = "@"
        self.map_data[10][7] = "S"
        self.map_data[5][10] = "C"
        self.add_object(4, 4, Item("Трава"))
        self.map_data[4][4] = "Ш"

    def add_border_walls(self):
        for x in range(self.width):
            self.map_data[0][x] = "#"
            self.map_data[self.height-1][x] = "#"
            self.map_data[7][7] = "Д"#ДАмики
            self.map_data[3][9] = "Д"
            self.map_data[11][2] = "Д"
            self.map_data[10][11] = "Д"
        for y in range(self.height):
            self.map_data[y][0] = "#"
            self.map_data[y][self.width-1] = "#"
