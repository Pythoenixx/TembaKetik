import math
import pygame
import mysql.connector
from pygame import mixer


mixer.init()
meletup = pygame.mixer.Sound('sound/meletup.mp3')
gameover = pygame.mixer.Sound('sound/gameover.mp3')
class Pemain(pygame.sprite.Sprite):
    def __init__(self, player_id, x, y, image_path) -> None:
        super().__init__()
        self.id = player_id
        self.hidup = True
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (69, 69))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.nearest_enemy = None
        self.typed_word_count = 0
        self.miss = 0
        self.miss_word = []
        self.accuracy = 0
        self.enemy_killed = 0#in wave
        self.start_time = 0
        self.end_time = 0
        self.elapsed_time = 0
        self.elapsed_time_list = []
        self.wpm = 0
        self.score = 0
    #deleted forgotten to delete gameOVer method
    def update(self, screen, enemy_group, char_typed, char_updated, cursor, db):
        if char_updated:
            if char_typed and self.nearest_enemy is None:
                if self.start_time == 0 : #utk pastikan dia x start timer byk kali and just bila dia 0 je
                    self.start_time = pygame.time.get_ticks()
                self.nearest_enemy = self.find_nearest_enemy(enemy_group, char_typed)
                if self.nearest_enemy is None:
                    self.miss += 1
        
        if self.nearest_enemy is not None:
            #highlight enemy
            self.nearest_enemy.text_color = 'Gold'
            pygame.draw.rect(screen, 'Gold', self.nearest_enemy.rect, 1)
            self.nearest_enemy.targeted = True
            if char_updated:
                #update enemy
                if self.nearest_enemy.word[0] == char_typed[-1]: # cane ai tau??
                    self.nearest_enemy.word = self.nearest_enemy.word[1:] #dia phm aku nk delete word tu ke?
                    self.typed_word_count += 1
                    if self.nearest_enemy.word == '':
                        meletup.play()
                        self.enemy_killed += 1
                        self.nearest_enemy = None
                        if len(enemy_group.sprites()) == 1: #last musuh blm mati lagi sbb update dia lepas pemain and dia akan mati sbb enemy.word == '' so kene cek klo tinggal 1 bukan 0
                            self.end_time = pygame.time.get_ticks()
                            self.elapsed_time = ((self.end_time - self.start_time) / 1000) / self.enemy_killed
                            self.elapsed_time_list.append(self.elapsed_time)
                            self.enemy_killed = 0
                            self.start_time = 0 #utk benarkan timer start balik
                else:
                    self.miss += 1
                    self.miss_word.append(self.nearest_enemy.ori_word)
        
        if pygame.sprite.spritecollide(self, enemy_group, False):#klo dh dekat dgn player baru check mask collision
            if pygame.sprite.spritecollide(self, enemy_group, True, pygame.sprite.collide_mask):
                gameover.play()
                self.kill()
                self.hidup = False
                self.accuracy = (self.typed_word_count / (self.typed_word_count + self.miss)) * 100 if self.typed_word_count + self.miss != 0 else 0
                #average spw to wpm conversion sbb tu 60 kat depan
                self.wpm = round(60/(sum(self.elapsed_time_list) / len(self.elapsed_time_list))) if len(self.elapsed_time_list) != 0 else 0
                self.score = int((0.69 * self.wpm * self.accuracy) + (0.42 * self.typed_word_count * self.accuracy)) #this formula is revealed in my dream
                #ofc not...(or is it??)
                try:
                    cursor.execute("INSERT INTO missed (player_ID, count, words) VALUES (%s, %s, %s)", (self.id, self.miss, ",".join(self.miss_word)))
                    cursor.execute("INSERT INTO WPM (player_ID, typed_word_count, nilai) VALUES (%s, %s, %s)", (self.id, self.typed_word_count, self.wpm))
                    db.commit()
                    
                    cursor.execute("SELECT MAX(ID) FROM missed")
                    miss_ID = cursor.fetchone()[0]
                    
                    cursor.execute("SELECT MAX(ID) FROM WPM")
                    wpm_ID = cursor.fetchone()[0]
                    
                    cursor.execute("INSERT INTO accuracy (miss_ID, WPM_ID, percentage) VALUES (%s, %s, %s)", (miss_ID, wpm_ID, self.accuracy))
                    db.commit()
                    
                    cursor.execute("SELECT ID FROM accuracy WHERE miss_ID = %s AND WPM_ID = %s", (miss_ID, wpm_ID))
                    accuracy_ID = cursor.fetchone()[0]
                    
                    cursor.execute("INSERT INTO score (miss_ID, accuracy_ID, WPM_ID, nilai) VALUES (%s, %s, %s, %s)", (miss_ID, accuracy_ID, wpm_ID, self.score))
                    db.commit()
                    
                    print("Data inserted successfully.")
                    
                except mysql.connector.Error as err:
                    print("MySQL Error: {}".format(err))
        

    # Define a function that takes a sprite and a list of sprites as parameters, and returns the nearest sprite in the list
    # if all enemy move at the same speed, this only need to run once for optimization
    def find_nearest_enemy(sprite, sprite_list, char_typed):
        # Initialize the minimum distance and the nearest sprite
        min_dist = math.inf
        nearest_sprite = None
        # Loop through the sprites in the list
        for other_sprite in sprite_list:
            if other_sprite.word[0] != char_typed[-1]:
                continue
            # Calculate the distance between the centers of the two sprites
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
    
    def stats(self, screen):
        if not self.hidup:
            font = pygame.font.Font(None, 30)
            text = font.render(f"Accuracy: {self.accuracy:.2f}%", True, (255, 255, 255))
            screen.blit(text, (10, 10))
            text = font.render(f"WPM: {self.wpm}", True, (255, 255, 255))
            screen.blit(text, (10, 40))
            text = font.render(f"Score: {self.score}", True, (255, 255, 255))
            screen.blit(text, (10, 70))
            transparent_surface = pygame.Surface (screen.get_size(), pygame.SRCALPHA) # Create a transparent surface
            transparent_surface.fill ((0, 0, 0, 128)) # Fill the surface with a semi-transparent black color
            screen.blit(transparent_surface, (0, 0)) # Blit the transparent surface to the screen)

def valid_char(username):
    if len(username) == 0:
        return False
    else:
        # Define the valid characters for a username
        valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._"
        # Loop through each character in the username
        for char in username:
            # If the character is not in the valid characters, return False
            if char not in valid_chars:
                return False
        # If the loop finishes without returning False, return True
        return True