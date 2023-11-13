import pygame,random

class Musuh:
    def __init__(self, x, y, w, h, color, target, speed) -> None:
        self.rect = pygame.Rect(0, 0, w, h)
        self.rect.center = (x, y)
        self.gerakanX,self.gerakanY = self.rect.x,self.rect.y #kene buat lagi satu variables coords sbb coords yg kat rect pygame x blh jdi float so akan ada rounding error
        self.color = color
        self.direction = pygame.math.Vector2(target.center) - pygame.math.Vector2(self.rect.center)
        self.direction = self.direction.normalize() # unit vector
        self.speed = speed
        
    def update(self):
        # Update the position of the rect
        self.gerakanX +=  (self.speed * self.direction.x)
        self.gerakanY +=  (self.speed * self.direction.y)
        
        self.rect.x = self.gerakanX
        self.rect.y = self.gerakanY
        
    def jana(bilangan, WN_LEBAR, pemain_rect):
        list_musuh = []
        for i in range(bilangan):
            # Generate random coordinates, size, and color for each rect
            x = random.randint(0, WN_LEBAR)
            y = random.randint(-100, 69)
            w = random.randint(10, 50)
            h = w #sbb nk buat square
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            laju = random.uniform(0.5, 10)
            
            musuh = Musuh(x, y, w, h, color, pemain_rect, laju)
            list_musuh.append(musuh)
            
        return list_musuh
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Pengawal_Musuh:
    def __init__(self) -> None:
        self.list_musuh = []
        
    def jana(self, bilangan, WN_LEBAR, pemain_rect):
        for i in range(bilangan):
            # Generate random coordinates, size, and color for each rect
            x = random.randint(0, WN_LEBAR)
            y = random.randint(-100, 69)
            w = random.randint(10, 50)
            h = w #sbb nk buat square
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            laju = random.uniform(0.5, 10)
            
            musuh = Musuh(x, y, w, h, color, pemain_rect, laju)
            self.list_musuh.append(musuh)