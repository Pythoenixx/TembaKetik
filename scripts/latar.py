import pygame,random
from scripts.pemalar import *

class Latar:
    def __init__(self,x,y,veloX,veloY) -> None:
        self.x = x
        self.y = y
        self.veloX = veloX
        self.veloY = veloY
        
        self.gmbr = pygame.image.load('img/bg.png').convert_alpha()
        self.gmbr = pygame.transform.scale(self.gmbr,(WN_LEBAR*PIC_ZOOM,WN_TINGGI*PIC_ZOOM))
        
    
    def gerak(self, screen, player_alive):
        screen.blit(self.gmbr, self.gmbr.get_rect(midbottom=(self.x,round(self.y))))
        if player_alive:
            self.y += self.veloY
        # Check if the image goes off the bottom of the screen
        if self.y > (self.gmbr.get_height()):
        # Wrap the image around to the top of the screen
            self.y -= self.gmbr.get_height() - WN_TINGGI
            self.x += 100
            if self.x > (self.gmbr.get_width()):
                self.x = random.randint(0,self.gmbr.get_width())