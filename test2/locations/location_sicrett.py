from test2.locations.location_base import LocationBase
from test2.item import Item

class LocationSicrett(LocationBase):
    def __init__(self):
        super().__init__(name="Секретная комната разраба", width=10, height=7, start_pos=(4,5))
        self.add_border_walls()
        self.map_data [5][8] ="@"

        self.add_object(5, 2, Item("Трава"))
        self.map_data[2][5] = "Ш"
        self.add_object(6, 2, Item("Шкура"))
        self.map_data [2][6] = chr(5860)
        self.add_object(4, 2, Item("Рататуй№2)"))
        self.map_data[2][4] = "K"


    def add_border_walls(self):
        for x in range(self.width):
            self.map_data[0][x] = "#"
            self.map_data[self.height-1][x] = "#"
        for y in range(self.height):
            self.map_data[y][0] = "#"
            self.map_data[y][self.width-1] = "#"
