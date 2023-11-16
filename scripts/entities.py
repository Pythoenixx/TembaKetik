import pygame,random

class Musuh(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, sasaran_rect, speed) -> None:
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.gerakanX,self.gerakanY = self.rect.x,self.rect.y #kene buat lagi satu variables coords sbb coords yg kat rect pygame x blh jdi float so akan ada rounding error
        self.direction = pygame.math.Vector2(sasaran_rect.center) - pygame.math.Vector2(self.rect.center)
        self.direction = self.direction.normalize() # unit vector
        self.speed = speed
        
    def update(self, WN_TINGGI):
        # Update the position of the rect
        self.gerakanX +=  (self.speed * self.direction.x)
        self.gerakanY +=  (self.speed * self.direction.y)
        
        self.rect.x = self.gerakanX
        self.rect.y = self.gerakanY
        
        self.destruct(WN_TINGGI)
        
    def destruct(self, WN_TINGGI):
        if self.gerakanY > WN_TINGGI + 69:
            self.kill()

class Pemain(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path) -> None:
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def update(self):
        pass
        

def jana_musuh(bilangan, WN_LEBAR, pemain_rect):
    musuh_group = pygame.sprite.Group()
    for i in range(bilangan):
        # Generate random coordinates, size, and color for each rect
        x = random.randint(0, WN_LEBAR)
        y = random.randint(-100, 69)
        laju = random.uniform(0.5, 10)
        
        musuh = Musuh(x, y, 'img/tahi_bintang.png', pemain_rect, laju)
        musuh_group.add(musuh)
        
    return musuh_group

