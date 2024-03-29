import pygame, random
from pygame import mixer
from scripts.pemalar import WN_LEBAR,WN_TINGGI, ENEMY_ASSETS

# Open the file and read the words
with open("txt/1000words.txt", "r") as f:
    most_used_words = f.read().split()

with open("txt/10000words.txt", "r") as f:
    least_used_words = f.read().split()

with open("txt/malaywords.txt", "r") as f:
    malay_words = f.read().split()

with open("txt/moremalaywords.txt", "r") as f:
    more_malay_words = f.read().split()

short_words = [word for word in most_used_words if len(word) <= 5]
long_words = [word for word in most_used_words if len(word) >= 6]#xde guna lagi
rare_long_words = [word for word in least_used_words if len(word) >= 7]

perkataan_pendek = [word for word in malay_words if len(word) <= 5]
perkataan_panjang = [word for word in more_malay_words if len(word) >= 7]

both_short = short_words + perkataan_pendek
both_long = long_words + perkataan_panjang

mixer.init()
meletup = pygame.mixer.Sound('sound/meletup.mp3')
zombi = pygame.mixer.Sound('sound/zombiedeath.mp3')

class Musuh(pygame.sprite.Sprite):
    def __init__(self, x, y, animation, sasaran_rect, text_offset, word, sfx_vol) -> None:
        super().__init__()
        self.animation = animation
        self.image_i = 0 #maybe blh buat ni random so dia start at random location and make dont make all of the same type of the enemy walk simultaneously? but have potential for it to have different hitbox(mask)
        self.image = self.animation[self.image_i]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = (x, y))
        self.gerakanX,self.gerakanY = self.rect.x,self.rect.y #kene buat lagi satu variables coords sbb coords yg kat rect pygame x blh jdi float so akan ada rounding error
        self.direction = pygame.math.Vector2(sasaran_rect.center) - pygame.math.Vector2(self.rect.center)
        self.direction = self.direction.normalize() # unit vector (kene normalize kan sbb klo magnitude panjang/tinggi sgt ig)
        self.word = word
        self.ori_word = self.word
        self.max_bullet_hit = len(self.ori_word)
        self.speed = 0.69
        self.font = pygame.font.SysFont("Arial", 21)
        self.text_color = (255, 255, 255)
        self.text_offset = text_offset
        self.targeted = False
        self._layer = 0
        self.dying = False
        self.sfx_vol = sfx_vol
        self.exploded = False
        
        self.explosion_ani = ENEMY_ASSETS['ExplosionAni']
        self.explosion_i = 0
        
    def update(self, screen, group_musuh):
        # Update the position of the rect
        if not self.dying:
            if self.max_bullet_hit <= 0:
                self.dying = True
            #animation
            self.image_i += 0.1
            if self.image_i >= len(self.animation):
                self.image_i = 0
            self.image = self.animation[int(self.image_i)]
            
            # Update the position of the rect based on the direction and speed
            self.gerakanX +=  (self.speed * self.direction.x)
            self.gerakanY +=  (self.speed * self.direction.y)
            
            self.rect.x = self.gerakanX
            self.rect.y = self.gerakanY
            
            if self.targeted:
                group_musuh.change_layer(self, 1)
            
            self.text = self.font.render(self.word, True, self.text_color, (0, 0, 0))
            self.text.set_alpha(200)

            self.text_rect = self.text.get_rect(topright = (self.rect.x + self.text_offset[0], self.rect.y + self.text_offset[1]))
            # screen.blit(self.mask_image, (0,0))
            screen.blit(self.text, self.text_rect)
            #if keluar dari screen then bunuh diri
            if self.gerakanY > WN_TINGGI + 69:
                self.kill()
        else:
            if self.explosion_i < len(self.explosion_ani):
                screen.blit(self.explosion_ani[i := int(self.explosion_i)], self.explosion_ani[i].get_rect(center = self.rect.center))
                self.explosion_i += 0.25
                if not self.exploded:
                    self.exploded = True
                    meletup.set_volume(self.sfx_vol)
                    zombi.set_volume(self.sfx_vol * 0.69)
                    meletup.play()
                    zombi.play()
                    self.word = ''
            else:
                self.kill()


class Zombetta(Musuh):
    def __init__(self, x, y, image, sasaran_rect, text_offset, sfx_vol, language) -> None:
        word = random_word(most_used_words, more_malay_words, 69)[0]
        super().__init__(x, y, image, sasaran_rect, text_offset, word, sfx_vol)
        
class Basic(Musuh):
    def __init__(self, x, y, image, sasaran_rect, text_offset, sfx_vol, language) -> None:
        if language == 'English':
            word = random.choice(short_words)
        elif language == 'Malay':
            word = random.choice(perkataan_pendek)
        else:
            word = random.choice(both_short)
        super().__init__(x, y, image, sasaran_rect, text_offset, word, sfx_vol)
        self.speed *= 0.8

class Gargantuan(Musuh):
    def __init__(self, x, y, image, sasaran_rect, text_offset, sfx_vol, language) -> None:
        if language == 'English':
            word = random.choice(rare_long_words)
        elif language == 'Malay':
            word = random.choice(perkataan_panjang)
        else:
            word = random.choice(both_long)
        super().__init__(x, y, image, sasaran_rect, text_offset, word, sfx_vol)
        self.speed *= 0.69

def jana_musuh(enemy_class, bilangan, musuh_group, assets_loaded, pemain_rect, sfx_vol, language):
    for _ in range(bilangan):
        # Generate random coordinates
        x = random.randint(0, WN_LEBAR)
        y = random.randint(-100, 0)
        
        musuh = enemy_class(x, y, assets_loaded[0], pemain_rect, assets_loaded[1], sfx_vol, language)
        musuh_group.add(musuh)

def jana_ombak(bil_ombak, musuh_group, bil_musuh, pemain_rect, sfx_vol, language):
    #maybe blh buat class asing for this type of func
    
    jana_musuh(Zombetta, bil_musuh['Zombetta'], musuh_group, ENEMY_ASSETS['Zombetta'], pemain_rect, sfx_vol, language)
    jana_musuh(Basic, bil_musuh['Basic'], musuh_group, ENEMY_ASSETS['Basic'], pemain_rect, sfx_vol, language)
    jana_musuh(Gargantuan, bil_musuh['Gargantuan'], musuh_group, ENEMY_ASSETS['Gargantuan'], pemain_rect, sfx_vol, language)
    
    bil_ombak += 1
    
    bil_musuh['Zombetta'] = bil_ombak 
    bil_musuh['Basic'] = bil_ombak + 3
    bil_musuh['Gargantuan'] += 1 if bil_ombak % 3 == 0 else 0
    
    return musuh_group,bil_ombak

# Define a function that takes two lists of words and a percentage as parameters, and returns a random word from the lists based on the percentage
def random_word(most_used, least_used, percentage):
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    # Use a ternary operator to pick a random word from the lists based on the percentage
    word = random.choice(most_used) if number <= percentage else random.choice(least_used)
    # Return the word
    return word

