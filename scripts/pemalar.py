import pygame
import os

def assets_load(image_path,scale):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (scale, scale)) #value ni kene sama dgn kat class Musuh
    return image

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

def animation_from_folder(folder, scale):
    animations = []
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        image = pygame.image.load(file_path)
        image = pygame.transform.scale(image, (scale, scale))
        animations.append(image)
    return animations

def renderTextCenteredAt(text, font, colour, x, y, screen, allowed_width):
    # first, split the text into words
    words = text.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))

        y_offset += fh

#window
WN_LEBAR = 500
WN_TINGGI = 820

FPS = 60

PIC_ZOOM = 5

PLAYER_ASSETS = {
    'Player' : animation_from_folder('img/Player', 80),#manusia
    'Bullet' : animation_from_folder('img/Bullet', 30),#dia pakai blaster
}

ENEMY_ASSETS = {
    'Zombetta' : (animation_from_folder('img/Zombetta', 60), cari_kiri_bawah(assets_load('img/Zombetta/zombetta1.png',60))),
    'Basic' : (animation_from_folder('img/Basic', 40), cari_kiri_bawah(assets_load('img/Basic/basic1.png',40))),
    'Gargantuan' : (animation_from_folder('img/Gargantuan', 69), cari_kiri_bawah(assets_load('img/Gargantuan/gargantuan1.png',69))),
    'ExplosionAni' : animation_from_folder('img/Explosion', 50),
}


