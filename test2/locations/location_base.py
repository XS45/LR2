class LocationBase:
    def __init__(self, name, width, height, start_pos=(1,1)):
        self.name = name
        self.width = width
        self.height = height
        self.start_pos = start_pos
        self.map_data = self.generate_map()
        self.objects = {}

    def generate_map(self):
        return [["." for _ in range(self.width)] for _ in range(self.height)]

    def is_walkable(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return False
        if self.map_data[y][x] == "#":
            return False
        if (x, y) in self.objects:
            obj = self.objects[(x, y)]
            return getattr(obj, "walkable", True)
        return True

    def add_object(self, x, y, obj):
        self.objects[(x, y)] = obj

    def remove_object(self, x, y):
        if (x, y) in self.objects:
            del self.objects[(x, y)]
            self.map_data[y][x] = "."

    def get_object_at(self, x, y):
        return self.objects.get((x, y), None)

    def get_tile(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return None
        return self.map_data[y][x]
