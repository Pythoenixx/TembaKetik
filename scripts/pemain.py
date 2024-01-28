import math
import pygame
import mysql.connector
from pygame import mixer
from scripts.pemalar import PLAYER_ASSETS, WN_LEBAR, WN_TINGGI

gameover = pygame.mixer.Sound('sound/gameover.mp3')
mati = pygame.mixer.Sound('sound/die.mp3')
bullet_impact = pygame.mixer.Sound('sound/bulletImpact.mp3')
class Pemain(pygame.sprite.Sprite):
    def __init__(self, player_id, x, y, animation, group_bullets) -> None:
        super().__init__()
        self.id = player_id
        self.x = x
        self.y = y
        self.hidup = True
        self.image_i = 0
        self.animation = animation
        self.image = animation[self.image_i]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = (x, y))
        self.group_bullets = group_bullets
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
    def update(self, screen, enemy_group, char_typed, char_updated, cursor, db, sound_effect_volume):
        #animation
        self.image_i += 0.1
        if self.image_i >= len(self.animation):
            self.image_i = 0
        self.image = self.animation[int(self.image_i)]
        
        self.rect = self.image.get_rect(center = (self.x, self.y)) #solve the issue of the sudden change in coords when rotating the image at some angle. It works sort of like a default rect coords when no rotated rect coords is given
        
        if char_updated:
            if char_typed and self.nearest_enemy is None:
                if self.start_time == 0 : #utk pastikan dia x start timer byk kali and just bila dia 0 je
                    self.start_time = pygame.time.get_ticks()
                self.nearest_enemy = self.find_nearest_enemy(enemy_group, char_typed)
                if self.nearest_enemy is None:
                    self.miss += 1
                else:
                    print(self.nearest_enemy.word)
        
        if self.nearest_enemy is not None:
            #rotate self to enemy
            jrk_x = self.nearest_enemy.rect.centerx - self.rect.centerx
            jrk_y = -(self.nearest_enemy.rect.centery - self.rect.centery)
            sudut = math.degrees(math.atan2(jrk_y, jrk_x))
            self.image = pygame.transform.rotate(self.image, sudut - 90)
            self.rect = self.image.get_rect(center = (self.x, self.y)) #this make it rotate at its center for some reason #maybe cos when the image rotate, it create new image and new image has its own rect size but since new rect size is not created, it still use the old rect and its coords so it makes other images cant grow past this old rect coord point(which is at topleft) but it still allow other corner to grow
            #highlight enemy
            self.nearest_enemy.text_color = 'Gold'
            pygame.draw.rect(screen, 'Gold', self.nearest_enemy.rect, 1)
            self.nearest_enemy.targeted = True
            
            if self.nearest_enemy.word == '' or self.nearest_enemy.dying:
                self.enemy_killed += 1
                print(self.nearest_enemy.ori_word, "killed, coords:", self.nearest_enemy.rect.center)
                self.nearest_enemy = None
                print("enemy set to :", self.nearest_enemy)
                
                if len(enemy_group.sprites()) == 1: #last musuh blm mati lagi sbb update dia lepas pemain and dia akan mati sbb enemy.word == '' so kene cek klo tinggal 1 bukan 0
                    self.end_time = pygame.time.get_ticks()
                    self.elapsed_time = ((self.end_time - self.start_time) / 1000) / self.enemy_killed
                    self.elapsed_time_list.append(self.elapsed_time)
                    self.enemy_killed = 0
                    self.start_time = 0 #utk benarkan timer start balik
            
            elif char_updated:
                print("player type:", char_typed[-1])
                #update enemy
                if self.nearest_enemy.word[0] == char_typed[-1]: # cane ai tau??
                    tembak = Bullet(self.x, self.y, self.nearest_enemy)
                    self.group_bullets.add(tembak)
                    
                    self.nearest_enemy.word = self.nearest_enemy.word[1:] #dia phm aku nk delete word tu ke?
                    print("remaining word:", self.nearest_enemy.word)
                    self.typed_word_count += 1
                else:
                    self.miss += 1
                    self.miss_word.append(self.nearest_enemy.ori_word)

        if pygame.sprite.spritecollide(self, enemy_group, False):#klo dh dekat dgn player baru check mask collision
            if pygame.sprite.spritecollide(self, enemy_group, True, pygame.sprite.collide_mask):
                mati.set_volume(sound_effect_volume)
                gameover.set_volume(sound_effect_volume * 69)
                mati.play()
                gameover.play()
                self.kill()
                self.hidup = False
                self.accuracy = (self.typed_word_count / (self.typed_word_count + self.miss)) * 100 if self.typed_word_count + self.miss != 0 else 0
                #average spw to wpm conversion sbb tu 60 kat depan
                self.wpm = round(60/(sum(self.elapsed_time_list) / len(self.elapsed_time_list))) if len(self.elapsed_time_list) != 0 else 0
                self.score = int((6.9 * self.wpm) + (4.2 * self.typed_word_count) + (5 * self.accuracy)) #this formula is revealed in my dream
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
            if other_sprite.word == '' or other_sprite.word[0] != char_typed[-1]:
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
    
    def show_stats(self, screen):
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
        for i in range(bil_penanda_aras + 1): #sbb start dari 0 tu kene tambah 1
            # Draw vertical ticks and labels
            vx = hor_margin
            vy = (height - ver_margin - i * (height - 2 * ver_margin) / bil_penanda_aras) + 69
            label_value = int(i * ceiling_data / bil_penanda_aras)
            tick_label = tick_font.render(str(label_value), True, 'white')
            screen.blit(tick_label, (vx - 45, vy - 5))
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

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, sasaran) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.animation = PLAYER_ASSETS['Bullet']
        self.image_i = 0
        self.image = self.animation[self.image_i]
        self.rect = self.image.get_rect(center = (x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.sasaran = sasaran
        self.gerakanX,self.gerakanY = self.rect.x,self.rect.y #kene buat lagi satu variables coords sbb coords yg kat rect pygame x blh jdi float so akan ada rounding error
        self.speed = 25
    
    def update(self, group_musuh, sfx_vol):
        #animation
        self.image_i += 0.1
        if self.image_i >= len(self.animation):
            self.image_i = 0
        self.image = self.animation[int(self.image_i)]
        
        #rotate self to enemy
        self.jrk_x = self.sasaran.rect.centerx - self.rect.centerx
        self.jrk_y = -(self.sasaran.rect.centery - self.rect.centery)
        self.sudut = math.degrees(math.atan2(self.jrk_y, self.jrk_x))
        self.image = pygame.transform.rotate(self.image, self.sudut - 90)
        self.rect = self.image.get_rect(center = (self.x, self.y))
        
        self.direction = pygame.math.Vector2(self.sasaran.rect.center) - pygame.math.Vector2(self.rect.center)
        self.direction = self.direction.normalize() # unit vector (kene normalize kan sbb klo magnitude panjang/tinggi sgt ig)
        
        # Update the position of the rect based on the direction and speed
        self.gerakanX +=  (self.speed * self.direction.x)
        self.gerakanY +=  (self.speed * self.direction.y)
        
        self.rect.x = self.gerakanX
        self.rect.y = self.gerakanY
        
        #klo keluar dari skrin bunuh diri
        if self.rect.x > WN_LEBAR or self.rect.x < 0 or self.rect.y > WN_TINGGI or self.rect.y < 0:
            self.kill()
            self.sasaran.max_bullet_hit -= 1
            if self.sasaran.max_bullet_hit <= 0:
                self.sasaran.dying = True
        
        collision_list = pygame.sprite.spritecollide(self, group_musuh, False, pygame.sprite.collide_mask)
        if collision_list:
            if self.sasaran in collision_list:
                self.kill()
                bullet_impact.set_volume(sfx_vol * 0.25)
                bullet_impact.play()
                self.sasaran.max_bullet_hit -= 1
                if self.sasaran.max_bullet_hit <= 0:
                    self.sasaran.dying = True
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