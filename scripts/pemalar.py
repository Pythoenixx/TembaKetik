import pygame
import os

def assets_load(image_path,scale):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (scale, scale)) #value ni kene sama dgn kat class Musuh
    bottomleft = cari_kiri_bawah(image)
    return (image,bottomleft)

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
    print(animations)
    return animations

#window
WN_LEBAR = 500
WN_TINGGI = 820

FPS = 60

PIC_ZOOM = 5

assets = {
    'Tiny_Kamikaze' : assets_load('renew/tiniykamikazeship/tinykamikazeship1.PNG',60),
    'Kamikaze' : assets_load('renew/kamikazeship/kamikazeship1.PNG',40),
    'Gunner' : assets_load('renew/gunnership/gunnership1.PNG',69),
    'ExplosionAni' : animation_from_folder('renew/explosion',69),
}
