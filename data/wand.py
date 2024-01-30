class Wand:
    damage = 0
    current_durability = 0
    name = "null"
    total_durability = 0
    level = 1
    image = None  
    
    def __init__(self, name, damage, durability, image):
        self.name = name
        self.damage = damage
        self.total_durability = durability
        self.current_durability = self.total_durability
        self.image = image

    def deal_damage(self):
        self.current_durability = self.current_durability - 1
        return self.damage + int(self.level/3)

    def add_level(self):
        self.level += 1
