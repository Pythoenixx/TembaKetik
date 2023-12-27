import pygame,sys
from pygame import mixer
from scripts.pemalar import *
from scripts.latar import Latar
from scripts.musuh import jana_ombak, assets_load
from scripts.pemain import Pemain
from scripts.button import Button

# Initialize pygame
pygame.init()
# Initialize mixer
mixer.init()
# Create a window object
icon = pygame.image.load('img/kapal_angkasa.PNG')
pygame.display.set_icon(icon)
SCREEN = pygame.display.set_mode((WN_LEBAR, WN_TINGGI))

clock = pygame.time.Clock()

assets = {
    'Tiny_Kamikaze' : assets_load('img/tiny_kamikaze_ship.png',50),
    'Kamikaze' : assets_load('img/kamikaze_ship.png',40),
    'Gunner' : assets_load('img/gunner_ship.png',69),
}

font = pygame.font.Font("font/font.ttf",20)

# Get the center of the screen
center_x = SCREEN.get_width() // 2
center_y = SCREEN.get_height() // 2

pemain = Pemain(center_x, WN_TINGGI - 100, 'img/player_ship.PNG')
group_pemain = pygame.sprite.GroupSingle()
group_pemain.add(pemain)

latar = Latar(0, WN_TINGGI, 0, 0.2)

mixer.music.load('soundEffect/backgroundsound.mp3')
# Set the initial volume
initial_volume = 0.05
pygame.mixer.music.set_volume(initial_volume)

mixer.music.play()

def main_menu():
    LOGO = pygame.image.load('img/logo.png').convert_alpha()
    LOGO = pygame.transform.scale(LOGO, (600, 500))
    LOGO_RECT = LOGO.get_rect(center=(center_x, 150))
    
    TITLE_FONT = pygame.font.Font('font/font.ttf', 40)
    MENU_TEXT = TITLE_FONT.render("TembaKetik", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(center_x, 250))
    
    BG = pygame.image.load('img/angkasa1.png').convert_alpha()
    BG = pygame.transform.scale(BG, (WN_LEBAR, WN_TINGGI))
    
    BTN_BG = pygame.image.load('img/buttonBG.png').convert_alpha()
    BTN_BG = pygame.transform.scale(BTN_BG, (300, 100))
    
    PLAY_BUTTON = Button(image=BTN_BG, pos=(center_x, 560), 
                            text_input="PLAY", font=font, base_color="#d7fcd4", hovering_color="Gold")
    OPTIONS_BUTTON = Button(image=BTN_BG, pos=(center_x, 640), 
                            text_input="STATS", font=font, base_color="#d7fcd4", hovering_color="GOLD")
    QUIT_BUTTON = Button(image=BTN_BG, pos=(center_x, 720), 
                            text_input="QUIT", font=font, base_color="#d7fcd4", hovering_color="GOLD")
    
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.blit(LOGO, LOGO_RECT)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.update()
        
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = font.render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(center_x, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(center_x, 460), 
                            text_input="BACK", font=font, base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def play():
    char_typed = ''
    char_updated = False
    
    group_musuh = pygame.sprite.LayeredUpdates()
    group_musuh,bil_ombak = jana_ombak(group_musuh, assets, pemain.rect)
    text_ombak = font.render(str(bil_ombak), True, (255,255,255), (0, 0, 0))
    # Create a custom timer event
    WAVE_EVENT= pygame.USEREVENT + 1
    timer_setted = False
    
    running = True
    while running:
        # Get a list of events
        events = pygame.event.get()
        # Loop through the events
        for event in events:
            if event.type == WAVE_EVENT:
                group_musuh,bil_ombak = jana_ombak(group_musuh, assets, pemain.rect)
                pygame.time.set_timer(WAVE_EVENT, 0)# Reset the timer to 0 to stop it
                timer_setted = False
            # Check if the user has clicked the close button
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                # Exit the loop and quit the program
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    char_typed = char_typed[:-1]  #amik smua value selain akhir sekali dlm list tu
                else:
                    char_typed += event.unicode #utk amik keyboard text input
                    char_updated = True
                
        
        #biar x de trail
        SCREEN.fill((0, 0, 0))
        latar.gerak(SCREEN)
        
        text = font.render(char_typed, True, (255, 255, 255), (0, 0, 0))
        SCREEN.blit(text, (0, 0))
        
        if group_musuh.sprites() == []:
            text_ombak = font.render(f'WAVE:{bil_ombak} CLEARED', True, (255,255,255))
            SCREEN.blit(text_ombak, (100, center_y))
            if not timer_setted:
                pygame.time.set_timer(WAVE_EVENT, 3000)#start 3s timer
                timer_setted = True
        
        group_pemain.draw(SCREEN) #try cari group sprite utk yg ada 1 sprite je
        group_pemain.update(SCREEN, group_musuh, char_typed, char_updated)
        char_updated = False
        
        group_musuh.draw(SCREEN)
        group_musuh.update(SCREEN, group_musuh)
        
        pygame.display.flip()
        clock.tick(FPS)
        pygame.display.set_caption(f'TembaKetik FPS: {clock.get_fps() :.1f}')# f' ' tu utk tukar jdi f-string (mcm string data type)
        print('pemain wpm:',pemain.wpm)

main_menu()

