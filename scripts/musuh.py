import pygame, random
from scripts.pemalar import WN_LEBAR,WN_TINGGI, assets

# Open the file and read the words
with open("txt/1000words.txt", "r") as f:
    most_used_words = f.read().split()

with open("txt/10000words.txt", "r") as f:
    least_used_words = f.read().split()

with open("txt/malaywords.txt", "r") as f:
    malay_words = f.read().split() 

short_words = [word for word in most_used_words if len(word) <= 5]
long_words = [word for word in most_used_words if len(word) >= 6]
rare_long_words = [word for word in least_used_words if len(word) >= 7]

class Musuh(pygame.sprite.Sprite):
    def __init__(self, x, y, image, sasaran_rect, text_offset, word) -> None:
        super().__init__()
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = (x, y))
        self.gerakanX,self.gerakanY = self.rect.x,self.rect.y #kene buat lagi satu variables coords sbb coords yg kat rect pygame x blh jdi float so akan ada rounding error
        self.direction = pygame.math.Vector2(sasaran_rect.center) - pygame.math.Vector2(self.rect.center)
        self.direction = self.direction.normalize() # unit vector
        self.word = word
        self.ori_word = self.word
        self.speed = 0.69
        self.font = pygame.font.SysFont("Arial", 21)
        self.text_color = (255, 255, 255)
        self.text_offset = text_offset
        self.targeted = False
        self._layer = 0
        self.dying = False
        
        self.explosion_ani = assets['ExplosionAni']
        self.explosion_index = 0
        
    def update(self, screen, group_musuh):
        # Update the position of the rect
        if not self.dying:
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
        
        self.destruct(screen)
        
    def destruct(self, screen):
        if self.word == '' or self.gerakanY > WN_TINGGI + 69:
            self.dying = True
            if self.explosion_index < len(self.explosion_ani):
                screen.blit(self.explosion_ani[i := int(self.explosion_index)], self.explosion_ani[i].get_rect(center = self.rect.center))
                self.explosion_index += 0.25
            else:
                self.kill()
            

class Tiny_Kamikaze(Musuh):
    def __init__(self, x, y, image, sasaran_rect, text_offset) -> None:
        word = random_word(most_used_words, least_used_words, 90)[0]
        super().__init__(x, y, image, sasaran_rect, text_offset, word)
        
class Kamikaze(Musuh):
    def __init__(self, x, y, image, sasaran_rect, text_offset) -> None:
        word = random.choice(short_words)
        super().__init__(x, y, image, sasaran_rect, text_offset, word)
        self.speed *= 0.8

class Gunner(Musuh):
    def __init__(self, x, y, image, sasaran_rect, text_offset) -> None:
        word = random.choice(rare_long_words)
        super().__init__(x, y, image, sasaran_rect, text_offset, word)
        self.speed *= 0.69

def jana_musuh(enemy_class, bilangan, musuh_group, assets_loaded, pemain_rect):
    for _ in range(bilangan):
        # Generate random coordinates
        x = random.randint(0, WN_LEBAR)
        y = random.randint(-100, 0)
        
        musuh = enemy_class(x, y, assets_loaded[0], pemain_rect, assets_loaded[1])
        musuh_group.add(musuh)

def jana_ombak(bil_ombak, musuh_group, bil_musuh, pemain_rect):
    #maybe blh buat class asing for this type of func
    
    jana_musuh(Tiny_Kamikaze, bil_musuh['Tiny_Kamikaze'], musuh_group, assets['Tiny_Kamikaze'], pemain_rect)
    jana_musuh(Kamikaze, bil_musuh['Kamikaze'], musuh_group, assets['Kamikaze'], pemain_rect)
    jana_musuh(Gunner, bil_musuh['Gunner'], musuh_group, assets['Gunner'], pemain_rect)
    
    bil_ombak += 1
    
    bil_musuh['Kamikaze'] = bil_ombak + 3
    bil_musuh['Tiny_Kamikaze'] = bil_ombak 
    bil_musuh['Gunner'] += 1 if bil_ombak % 3 == 0 else 0
    
    return musuh_group,bil_ombak

# Define a function that takes two lists of words and a percentage as parameters, and returns a random word from the lists based on the percentage
def random_word(most_used, least_used, percentage):
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    # Use a ternary operator to pick a random word from the lists based on the percentage
    word = random.choice(most_used) if number <= percentage else random.choice(least_used)
    # Return the word
    return word

