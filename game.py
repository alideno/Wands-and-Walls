import pygame
import data.button
import data.player
import data.wand
import data.enemy
import math
import random


screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
pygame.display.set_caption('Wands and Walls')
pygame.display.set_icon(pygame.image.load('data/icon.png'))
#menu
background_img = pygame.image.load('data/backgrounds/menu_background.png').convert_alpha()
start_img = pygame.image.load('data/buttons/menu/start_btn.png').convert_alpha()
exit_img = pygame.image.load('data/buttons/menu/exit_btn.png').convert_alpha()

start_button = data.button.Button(200, 700, start_img, 2.5)
exit_button = data.button.Button(1000, 700, exit_img, 2.5)

#game over 


#game
level = 1
user = data.player.Player(100,10)
enemy_img = pygame.image.load('data/enemies/enemy_image.png').convert_alpha()
enmy = None
attack_btn_img = pygame.image.load('data/buttons/fight/attack_btn.png').convert_alpha()
deactivated_attack_btn_img = pygame.image.load('data/buttons/fight/deactivated_attack_btn.png').convert_alpha()
health_image = pygame.image.load('data/buttons/fight/health.png').convert_alpha()
gold_image = pygame.image.load('data/buttons/fight/gold.png').convert_alpha()

just_defeated = False

attack1_button = data.button.Button(60,580, attack_btn_img,2)
attack2_button = data.button.Button(800,580, attack_btn_img,2)
attack3_button = data.button.Button(60,830, attack_btn_img,2)
attack4_button = data.button.Button(800,830, attack_btn_img,2)

BUTTON_TEXT_OFFSET_X = 250

#load between levels
continue_button_image = pygame.image.load('data/buttons/load/continue_btn.png').convert_alpha()
continue_button = data.button.Button(800,800,continue_button_image,2)
last_shop = 0
last_chest = 0

#startup
main_screen = True
game_screen = False
load_screen = False
gameover_screen = False
between_levels_screen = False
shop_screen = False
chest_screen = False
BOSS_LEVEL = 20
#wands
wands = [

    
    
    
        ]
user.wands[0] = data.wand.Wand("Starter Wand",5,20,pygame.image.load('data/wands/basic_wand.png').convert_alpha())
#fonts
pygame.font.init()
custom_font = pygame.font.Font('data/alagard.ttf', 50)
custom_font_big = pygame.font.Font('data/alagard.ttf',120)


#####TEMP TEMP TEMP#####


#####TEMP TEMP TEMP#####

run = True
while run:

    screen.fill((202, 228, 241))

    if main_screen:
        screen.blit(background_img, (0, 0))
        if start_button.draw(screen):
            main_screen = False
            game_screen = False
            gameover_screen = False
            load_screen = True

            pygame.time.delay(150)
        if exit_button.draw(screen):
            run = False
    
    elif gameover_screen:
        gameover_text = custom_font_big.render(f"", True, (0, 0, 0))
        gameover_text2 = custom_font_big.render(f"GAME OVER", True, (0, 0, 0))
        screen.blit(gameover_text,(150,600))
        screen.blit(gameover_text2,(400,450))
        if start_button.draw(screen):
            main_screen = False
            game_screen = False
            gameover_screen = False
            load_screen = True
            gameover_screen = False
            user = data.player.Player(50,10)
            level = 1
            last_chest = 0
            last_shop = 0
            pygame.time.delay(150)
        if exit_button.draw(screen):
            run = False
            
    elif load_screen:
        enmy = data.enemy.Enemy(5,2,enemy_img,5)
        load_screen = False
        game_screen = True
        just_defeated = False
        load_text = custom_font_big.render(f"GOING DEEPER IN THE DUNGEON...", True, (0, 0, 0))
        screen.blit(load_text, (0, 340))
        pygame.display.flip()
        pygame.time.delay(150)
    
    elif between_levels_screen:
        hp_text = custom_font_big.render(f"HP: {user.current_health}/{user.total_health}", True, (0,0,0))
        screen.blit(hp_text,(100,100))
        gold_text = custom_font_big.render(f"Gold: {user.gold}", True, (0,0,0))
        screen.blit(gold_text,(100,200))
        
        shop_text = custom_font_big.render(f"Shop Chance: {last_shop}%", True, (0,0,0))
        screen.blit(shop_text,(100,300))
        chest_text = custom_font_big.render(f"Chest Chance: {last_chest}%", True, (0,0,0))
        screen.blit(chest_text,(100,400))
        if(BOSS_LEVEL-level > 1):
            boss_text = custom_font_big.render(f"Until Boss: {BOSS_LEVEL-level+1} Rooms", True, (0,0,0))
        else:
            boss_text = custom_font_big.render(f"Boss Battle!", True, (0,0,0))
        screen.blit(boss_text,(100,500))        
        
        enmy = data.enemy.Enemy(5+level*2,1+level,enemy_img,5)   
        if(continue_button.draw(screen)):
            if(last_shop >= random.randint(0,100)):
                between_levels_screen = False
                shop_screen = True
                just_defeated = False
            elif(last_chest >= random.randint(0,100)):
                between_levels_screen = False
                chest_screen = True
                just_defeated = False               
            else:
                between_levels_screen = False
                game_screen = True
                just_defeated = False
            pygame.time.delay(150)

        pygame.display.flip()

        
        
    elif game_screen:
        #screen.blit(background_game_img,(0,0))
        #Display player health and gold
        hp_text = custom_font.render(f"HP: {user.current_health}", True, (146, 28, 61))
        screen.blit(health_image,(1540,580))
        screen.blit(hp_text,(1570,730))
        gold_text = custom_font.render(f"Gold: {user.gold}", True, (255, 209, 123))
        screen.blit(gold_image,(1540,830))
        screen.blit(gold_text,(1550,960))
        #Creating The Enemy
        screen.blit(enmy.image,(screen.get_width()/2-enmy.image.get_width()/2,100))
        enemy_hp_text = custom_font.render(f"HP: {enmy.current_health}", True, (0, 0, 0))
        screen.blit(enemy_hp_text, (300, 300))
        #Dispaly level
        level_text = custom_font.render(f"Level: {level}", True, (0,0,0))
        screen.blit(level_text, (0,100))

  
        if user.wands[0] is not None:
            
            attack1_button.change_image(attack_btn_img)
            attack1_button.add_image(user.wands[0].image,(10,0))
            attack1_button.add_text(f"{user.wands[0].name}", (BUTTON_TEXT_OFFSET_X, 30), text_color=(0, 0, 0), font = custom_font)
            attack1_button.add_text(f"Level: {user.wands[0].level}", (BUTTON_TEXT_OFFSET_X, 80), text_color=(0, 0, 0), font = custom_font)
            attack1_button.add_text(f"Uses: {user.wands[0].current_durability}/{user.wands[0].total_durability}", (BUTTON_TEXT_OFFSET_X, 130), text_color=(0, 0, 0), font = custom_font)
            
            if attack1_button.draw(screen) and user.wands[0].current_durability > 0:
                
                enmy.take_damage(user.wands[0].deal_damage())
                user.take_damage(enmy.deal_damage())
                                
        else:
            attack1_button.change_image(deactivated_attack_btn_img)
            attack1_button.draw(screen) 
        
        if user.wands[1] is not None:
            attack2_button.change_image(attack_btn_img)
            attack2_button.add_image(user.wands[1].image,(10,0))
            attack2_button.add_text(f"{user.wands[1].name}", (BUTTON_TEXT_OFFSET_X, 30), text_color=(0, 0, 0), font = custom_font)
            attack2_button.add_text(f"Level: {user.wands[1].level}", (BUTTON_TEXT_OFFSET_X, 80), text_color=(0, 0, 0), font = custom_font)
            attack2_button.add_text(f"Uses: {user.wands[1].current_durability}/{user.wands[1].total_durability}", (BUTTON_TEXT_OFFSET_X, 130), text_color=(0, 0, 0), font = custom_font)
            
            if attack2_button.draw(screen) and user.wands[1].current_durability > 0:
                enmy.take_damage(user.wands[1].deal_damage())
                user.take_damage(enmy.deal_damage())
                    
        else:
            attack2_button.change_image(deactivated_attack_btn_img)
            attack2_button.draw(screen)
            
        if user.wands[2] is not None:
            attack3_button.change_image(attack_btn_img)
            attack3_button.add_image(user.wands[2].image,(10,0))
            attack3_button.add_text(f"{user.wands[2].name}", (BUTTON_TEXT_OFFSET_X, 30), text_color=(0, 0, 0), font = custom_font)
            attack3_button.add_text(f"Level: {user.wands[2].level}", (BUTTON_TEXT_OFFSET_X, 80), text_color=(0, 0, 0), font = custom_font)
            attack3_button.add_text(f"Uses: {user.wands[2].current_durability}/{user.wands[2].total_durability}", (BUTTON_TEXT_OFFSET_X, 130), text_color=(0, 0, 0), font = custom_font)
            
            if attack3_button.draw(screen) and user.wands[2].current_durability > 0:
                enmy.take_damage(user.wands[2].deal_damage())
                user.take_damage(enmy.deal_damage())
        else:
            attack3_button.change_image(deactivated_attack_btn_img)
            attack3_button.draw(screen)
            
        if user.wands[3] is not None:
            attack4_button.change_image(attack_btn_img)
            attack4_button.add_image(user.wands[3].image,(10,0))
            attack4_button.add_text(f"{user.wands[3].name}", (BUTTON_TEXT_OFFSET_X, 30), text_color=(0, 0, 0), font = custom_font)
            attack4_button.add_text(f"Level: {user.wands[3].level}", (BUTTON_TEXT_OFFSET_X, 80), text_color=(0, 0, 0), font = custom_font)
            attack4_button.add_text(f"Uses: {user.wands[3].current_durability}/{user.wands[3].total_durability}", (BUTTON_TEXT_OFFSET_X, 130), text_color=(0, 0, 0), font = custom_font)
            
            if attack4_button.draw(screen) and user.wands[3].current_durability > 0:
                enmy.take_damage(user.wands[3].deal_damage())
                user.take_damage(enmy.deal_damage())
        else:
            attack4_button.change_image(deactivated_attack_btn_img)
            attack4_button.draw(screen)
            
        if user.is_defeated():
            game_screen = False
            gameover_screen = True
    
        if just_defeated: 
            user.add_gold(enmy.give_gold())
            level += 1  
            just_defeated = False
            game_screen = False
            between_levels_screen = True
            last_shop += 20
            last_chest += 20
            pygame.display.update()
            pygame.time.delay(1000)
            
        if enmy.is_defeated():
            just_defeated = True
        
            



    # Event handler
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
