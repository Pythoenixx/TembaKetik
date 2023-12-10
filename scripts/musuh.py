import pygame, random

# Open the file and read the words
with open("txt/1000words.txt", "r") as f:
    most_used_words = f.read().split()

with open("txt/10000words.txt", "r") as f:
    least_used_words = f.read().split()

class Musuh(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, sasaran_rect, speed, font,text_offset) -> None:
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center = (x, y))
        self.gerakanX,self.gerakanY = self.rect.x,self.rect.y #kene buat lagi satu variables coords sbb coords yg kat rect pygame x blh jdi float so akan ada rounding error
        self.direction = pygame.math.Vector2(sasaran_rect.center) - pygame.math.Vector2(self.rect.center)
        self.direction = self.direction.normalize() # unit vector
        self.speed = speed
        self.word = random_word(most_used_words, least_used_words, 90)
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

def jana_musuh(bilangan, WN_LEBAR, pemain_rect, font):
    image_path = 'img/tahi_bintang.png'
    image = pygame.image.load(image_path).convert_alpha()
    image = pygame.transform.scale(image, (50, 50)) #value ni kene sama dgn kat class Musuh
    bottomleft = cari_kiri_bawah(image)
    musuh_group = pygame.sprite.LayeredUpdates()
    for i in range(bilangan):
        # Generate random coordinates, size, and color for each rect
        x = random.randint(0, WN_LEBAR)
        y = random.randint(-100, 69)
        laju = 0.69
        
        musuh = Musuh(x, y, image_path, pemain_rect, laju, font, bottomleft)
        musuh_group.add(musuh)
        
    return musuh_group

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

# Define a function that takes two lists of words and a percentage as parameters, and returns a random word from the lists based on the percentage
def random_word(most_used, least_used, percentage):
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    # Use a ternary operator to pick a random word from the lists based on the percentage
    word = random.choice(most_used) if number <= percentage else random.choice(least_used)
    # Return the word
    return word