class Character:
    def __init__(self, x, y, name="Незнакомец", HP=100, MP=50, ARM=10, DMG=20):
        self.x = x
        self.y = y
        self.name = name
        self.HP = HP
        self.MP = MP
        self.ARM = ARM
        self.DMG = DMG

class Player(Character):
    def __init__(self, x, y):
        super().__init__(x, y, name="PC", HP=120, MP=70, ARM=15, DMG=25)
        self.inventory = None  # Будет проинициализирован в game.py

class Enemy(Character):
    def __init__(self, x, y):
        super().__init__(x, y, name="Enemy", HP=20, MP=30, ARM=5, DMG=10)
