class Enemy:
    
    current_health = 0
    total_health = 0
    gold = 0
    
    def __init__(self, health, damage, image, gold):
        self.total_health = health
        self.current_health = self.total_health
        if(damage >= 10):
            self.damage = 10
        else: 
            self.damage = damage
        self.gold = gold
        self.image = image
        self.rect = self.image.get_rect()

    def take_damage(self, amount):
        self.current_health -= amount
        
    def deal_damage(self):
        return self.damage

    def is_defeated(self):
        return self.current_health <= 0
    
    def give_gold(self):
        return self.gold
