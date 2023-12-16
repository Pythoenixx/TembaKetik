import pygame, random

# Open the file and read the words
with open("txt/1000words.txt", "r") as f:
    most_used_words = f.read().split()

with open("txt/10000words.txt", "r") as f:
    least_used_words = f.read().split()

short_words = [word for word in most_used_words if len(word) <= 5]
long_words = [word for word in most_used_words if len(word) >= 6]
rare_long_words = [word for word in least_used_words if len(word) >= 7]

bil_tiny_kamikaze = 0
bil_kamikaze = 3
bil_gunner = 0

bil_ombak = 0

class Musuh(pygame.sprite.Sprite):
    def __init__(self, x, y, image, sasaran_rect, font,text_offset) -> None:
        super().__init__()
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = (x, y))
        self.gerakanX,self.gerakanY = self.rect.x,self.rect.y #kene buat lagi satu variables coords sbb coords yg kat rect pygame x blh jdi float so akan ada rounding error
        self.direction = pygame.math.Vector2(sasaran_rect.center) - pygame.math.Vector2(self.rect.center)
        self.direction = self.direction.normalize() # unit vector
        self.speed = 0.69
        self.font = font
        self.text_color = (255, 255, 255)
        self.text_offset = text_offset
        self.targeted = False
        self._layer = 0
        
    def update(self, screen, WN_TINGGI, group_musuh):
        # Update the position of the rect
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
        
        self.destruct(WN_TINGGI)
        
    def destruct(self, WN_TINGGI):
        if self.word == '':
            self.kill()
        if self.gerakanY > WN_TINGGI + 69:
            self.kill()
class Tiny_Kamikaze(Musuh):
    def __init__(self, x, y, image, sasaran_rect, font,text_offset) -> None:
        super().__init__(x, y, image, sasaran_rect, font, text_offset)
        self.word = random_word(most_used_words, least_used_words, 90)[0]
class Kamikaze(Musuh):
    def __init__(self, x, y, image, sasaran_rect, font,text_offset) -> None:
        super().__init__(x, y, image, sasaran_rect, font, text_offset)
        self.word = random.choice(short_words)
        self.speed *= 0.8

class Gunner(Musuh):
    def __init__(self, x, y, image, sasaran_rect, font,text_offset) -> None:
        super().__init__(x, y, image, sasaran_rect, font, text_offset)
        self.word = random.choice(rare_long_words)
        self.speed *= 0.69

def jana_musuh(enemy_class, bilangan, musuh_group,assets_loaded, WN_LEBAR, pemain_rect, font):
    for i in range(bilangan):
        # Generate random coordinates, size, and color for each rect
        x = random.randint(0, WN_LEBAR)#try phmkan blik napa value ni
        y = random.randint(-100, 69)
        
        musuh = enemy_class(x, y, assets_loaded[0], pemain_rect, font, assets_loaded[1])
        musuh_group.add(musuh)

def jana_ombak(musuh_group, assets, WN_LEBAR, pemain_rect, font):
    global bil_ombak,bil_tiny_kamikaze,bil_kamikaze,bil_gunner#maybe blh try buat func yg akan increase diff so x yh nk guna global var
    #maybe blh buat class asing for this type of func
    
    jana_musuh(Tiny_Kamikaze,bil_tiny_kamikaze, musuh_group, assets['Tiny_Kamikaze'], WN_LEBAR, pemain_rect, font)
    jana_musuh(Kamikaze,bil_kamikaze, musuh_group, assets['Kamikaze'], WN_LEBAR, pemain_rect, font)
    jana_musuh(Gunner,bil_gunner, musuh_group, assets['Gunner'], WN_LEBAR, pemain_rect, font)
    
    bil_ombak += 1
    bil_kamikaze = bil_ombak + 3
    bil_tiny_kamikaze = bil_ombak 
    bil_gunner += 1 if bil_ombak % 3 == 0 else 0
    
    
    
    return musuh_group,bil_ombak

def assets_load(image_path,scale):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (scale, scale)) #value ni kene sama dgn kat class Musuh
    bottomleft = cari_kiri_bawah(image)
    return (image,bottomleft)

# Define a function that takes two lists of words and a percentage as parameters, and returns a random word from the lists based on the percentage
def random_word(most_used, least_used, percentage):
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    # Use a ternary operator to pick a random word from the lists based on the percentage
    word = random.choice(most_used) if number <= percentage else random.choice(least_used)
    # Return the word
    return word

def cari_kiri_bawah(image):
    #x leh guna rect.bottomleft sbb dia akan amik kira background img so terpaksa buat func sendiri
    mask = pygame.mask.from_surface(image)
    outline_points = mask.outline()
    # Sort the list by y-values in descending order
    outline_points.sort (key=lambda c: c [1], reverse=True) #c[1] == y coord so sort highest y to lowest (y kene highest sbb y coord dlm pygame hala bwh)

    # Find the minimum x-value among the coordinates with the highest y-value
    min_x = min(c[0] for c in outline_points if c [1] == outline_points [0][1]) 
    #c[0] == x coord, so untuk setiap x, klo ada y dia sama dgn highest y, dia akan masukkan dlm tuple (x yg ada highest y kdg ada byk)
    
    # Return the coordinate that has both the highest y-value and the minimum x-value
    bottom_left = next(c for c in outline_points if c [0] == min_x and c [1] == outline_points [0][1])#next() akan dptkan first value of iterator
    #since dh dpt value x lowest,y highest, skrg dh blh loop setiap point tu utk cari coords yg same dgn x lowest,y highest
    
    
    return bottom_left