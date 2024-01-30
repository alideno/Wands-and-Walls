import pygame

class Button():
    
    def __init__(self, x, y, image, scale):
        self.scale = scale
        width = image.get_width()
        height = image.get_height()
        self.original_image = image
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

    def change_image(self, new_image):
        self.original_image = new_image
        width = new_image.get_width()
        height = new_image.get_height()
        self.image = pygame.transform.scale(new_image, (int(width * self.scale), int(height * self.scale)))

    def add_text(self, text, coords, text_color=(255, 255, 255), font=None):
        font = font or pygame.font.Font(None, 36)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(topleft=coords)
        self.image.blit(text_surface, text_rect)

    def add_image(self, image, image_coords):
        self.image.blit(image, image_coords)

