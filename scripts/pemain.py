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
                    
                    cursor.execute("SELECT score.nilai FROM score JOIN missed ON score.miss_ID = missed.ID JOIN player ON missed.player_ID = player.ID WHERE player.ID = %s", (self.id,))
                    self.score_list = cursor.fetchall()
                    self.score_list = [score[0] for score in self.score_list] #fetchall tu akan bagi tuple of tuples so kene first element setiap tuple and masukkan balik dlm variable supaya sume jadi list element
                    
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
        width = screen.get_width()
        height = screen.get_height()
        
        center_x = screen.get_width() // 2
        
        lbl_color = 'cyan'
        data_color = 'gold'
        graph_color = 'grey'
        #lbl coords
        wpm_coords = (10, 10)
        accuracy_coords = (center_x, 10)
        miss_coords = (10, 125)
        score_coords = (center_x, 125)
        
        font = pygame.font.Font('font/font.ttf', 17)
        data_font = pygame.font.Font('font/font.ttf', 30)
        
        transparent_surface = pygame.Surface (screen.get_size(), pygame.SRCALPHA) # Create a transparent surface
        transparent_surface.fill ((0, 0, 0, 169)) # Fill the surface with a semi-transparent black color
        screen.blit(transparent_surface, (0, 0)) # Blit the transparent surface to the screen)
        
        text = font.render(f"WPM", True, lbl_color)
        screen.blit(text, wpm_coords)
        text = data_font.render(f"{self.wpm}", True, data_color)
        screen.blit(text, (wpm_coords[0], wpm_coords[1] + 40))
        
        text = font.render(f"Accuracy", True, lbl_color)
        screen.blit(text, accuracy_coords)
        text = data_font.render(f"{self.accuracy:.2f}%", True, data_color)
        screen.blit(text, (accuracy_coords[0], accuracy_coords[1] + 40))
        
        text = font.render(f"Miss", True, lbl_color)
        screen.blit(text, miss_coords)
        text = data_font.render(f"{self.miss}", True, data_color)
        screen.blit(text, (miss_coords[0], miss_coords[1] + 40))
        
        text = font.render(f"Score", True, lbl_color)
        screen.blit(text, score_coords)
        text = data_font.render(f"{self.score}", True, data_color)
        screen.blit(text, (score_coords[0], score_coords[1] + 40))
        
        # Generate some random data points
        number_of_points = len(self.score_list) # Number of points
        data = self.score_list # Y values
        ceiling_data = 10 * round(max(data)/10)

        # Plot the data points and connect them with lines
        point_radius = 5
        line_width = 2

        # Set up margins and axes
        ver_margin = 180
        hor_margin = 50
        
        tick_font = pygame.font.SysFont("Arial", 15)
        bil_penanda_aras = 4
        hx = hor_margin + 10 * (width - 2 * hor_margin) / 10
        hy = height - ver_margin
        for i in range(bil_penanda_aras + 1): #sbb start dari 0 tu kene tambah 1
            # Draw vertical ticks and labels
            vx = hor_margin
            vy = (height - ver_margin - i * (height - 2 * ver_margin) / bil_penanda_aras) + 69
            label_value = int(i * ceiling_data / bil_penanda_aras)
            tick_label = tick_font.render(str(label_value), True, graph_color)
            screen.blit(tick_label, (vx - 30, vy - 5))
            pygame.draw.line(screen, graph_color, (hor_margin, vy), (hx, vy))

        for i in range(number_of_points):
            # Convert the data point to screen coordinates
            x = hor_margin + i * (width - 2 * hor_margin) / (number_of_points - 1 if number_of_points > 1 else number_of_points)
            y = (height - ver_margin - data[i] * (height - 2 * ver_margin) / ceiling_data) + 69
            # Draw the point as a blue circle
            pygame.draw.circle(screen, data_color, (x, y), point_radius)
            # Draw the line segment as a red line
            if i > 0:
                # Get the previous point's coordinates
                prev_x = hor_margin + (i - 1) * (width - 2 * hor_margin) / (number_of_points - 1 if number_of_points > 1 else number_of_points)
                prev_y = (height - ver_margin - data[i - 1] * (height - 2 * ver_margin) / ceiling_data) + 69
                # Draw the line from the previous point to the current point
                pygame.draw.line(screen, lbl_color, (prev_x, prev_y), (x, y), line_width)

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