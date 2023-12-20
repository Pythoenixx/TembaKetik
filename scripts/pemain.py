import math
import pygame


class Pemain(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path) -> None:
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (69, 69))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.nearest_enemy = None
        
    def update(self, screen, enemy_group, char_typed, char_updated):
        if char_typed and self.nearest_enemy is None and char_updated:
            self.nearest_enemy = self.find_nearest_enemy(enemy_group, char_typed)
        
        if self.nearest_enemy is not None:
            #highlight enemy
            self.nearest_enemy.text_color = 'Gold'
            pygame.draw.rect(screen, 'Gold', self.nearest_enemy.rect, 1)
            self.nearest_enemy.targeted = True
            if char_updated:
                #update enemy
                if self.nearest_enemy.word[0] == char_typed[-1]: # cane ai tau??
                    self.nearest_enemy.word = self.nearest_enemy.word[1:] #dia phm aku nk delete word tu ke?
                    if self.nearest_enemy.word == '':
                        self.nearest_enemy = None
        
        if pygame.sprite.spritecollide(self, enemy_group, False):#klo dh dekat dgn player baru check mask collision
            if pygame.sprite.spritecollide(self, enemy_group, True, pygame.sprite.collide_mask):
                self.kill()

    # Define a function that takes a sprite and a list of sprites as parameters, and returns the nearest sprite in the list
    # if all enemy move at the same speed, this only need to run once for optimization
    def find_nearest_enemy(sprite, sprite_list, char_typed):
        # Initialize the minimum distance and the nearest sprite
        min_dist = math.inf
        nearest_sprite = None
        # Loop through the sprites in the list
        for other_sprite in sprite_list:
            # Calculate the distance between the centers of the two sprites
            if other_sprite.word[0] != char_typed[-1]:
                continue
            
            dx = other_sprite.rect.centerx - sprite.rect.centerx
            dy = other_sprite.rect.centery - sprite.rect.centery
            dist = math.sqrt(dx**2 + dy**2)
            # Compare the distance with the minimum distance
            if dist < min_dist:
                # Update the minimum distance and the nearest sprite
                min_dist = dist
                nearest_sprite = other_sprite
        # Return the nearest sprite
        return nearest_sprite