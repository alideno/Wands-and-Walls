import data.wand
import pygame

class Player:
    
    wands = [None, None, None, None]
    gold = 0
    total_health = 0
    current_health = 0
    
    def __init__(self,total_health,gold):
        self.gold = gold
        self.total_health = total_health
        self.current_health = total_health
        
    def add_gold(self, to_add):
        self.gold = self.gold + to_add
        
    def pay(self,check):
        
        if(self.gold < check):
            return False
        else:
            self.gold -= check
            return True
        
    
    def add_health(self, to_add):
        if(to_add + self.current_health > self.total_health):
            self.current_health = self.total_health
        else:
            self.current_health += to_add
    
    def take_damage(self,damage):
        self.current_health -= damage
        
    def is_defeated(self):
        return self.current_health <= 0    

    
