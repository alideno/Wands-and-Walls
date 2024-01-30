from wand import Wand

class EnhancedWand(Wand):
    def __init__(self, name, damage, durability, enhancement):
        super().__init__(name, damage, durability)
        self.enhancement = enhancement
    
    def deal_damage(self):
        damage_with_enhancement = super().deal_damage() + self.enhancement
        return damage_with_enhancement
    
    def perform_enhancement(self):
        print(f"Performing enhancement for {self.name}!")