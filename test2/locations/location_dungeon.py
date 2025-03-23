from test2.locations.location_base import LocationBase
from test2.item import Item

class LocationDungeon(LocationBase):
    def __init__(self):
        super().__init__(name="ПодземельеЫ)", width=15, height=15, start_pos=(12,7))
        self.add_border_walls()
        self.map_data[7][13] = "@"
        self.map_data[6][5] = "#"
        self.add_object(6, 6, Item("Рататуй№1)"))#крысы для квеста "Крысы в подвале"
        self.add_object(7, 6, Item("Рататуй№2)"))
        self.map_data[6][6] = "K"
        self.map_data[7][6] = "K"
        self.add_object(4, 8, Item("Амууууулет"))
        self.map_data[8][4] = "A"
        self.add_object(9, 9, Item("Трава"))
        self.map_data[9][9] = "Ш"

    def add_border_walls(self):
        for x in range(self.width):
            self.map_data[0][x] = "#"
            self.map_data[self.height-1][x] = "#"
        for y in range(self.height):
            self.map_data[y][0] = "#"
            self.map_data[y][self.width-1] = "#"
