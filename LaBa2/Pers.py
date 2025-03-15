class Character:
    def __init__(self, name, hp, mp, arm, dmg):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.arm = arm
        self.dmg = dmg

    def is_alive(self):
        return self.hp > 0

    def attack(self, defender):
        damage = self.calculate_damage(defender)
        defender.hp -= damage
        print(f"{self.name} нанес {damage} урона {defender.name}. У {defender.name} осталось {defender.hp} HP.")

    def calculate_damage(self, defender):
        damage = self.dmg - defender.arm
        return max(damage, 0)
