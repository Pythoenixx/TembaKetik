import pygame,sys,asyncio,mysql.connector

from pygame import mixer
from scripts.pemalar import *
from scripts.latar import Latar
from scripts.musuh import jana_ombak
from scripts.pemain import Pemain, valid_char
from scripts.button import Button

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tembaketik"
)

cursor = db.cursor()
# Initialize pygame
pygame.init()

# Initialize mixer
mixer.init()


# Create a window object
icon = pygame.image.load('img/logo.PNG')
pygame.display.set_icon(icon)
SCREEN = pygame.display.set_mode((WN_LEBAR, WN_TINGGI))

font = pygame.font.Font("font/font.ttf",20)

# Get the center of the screen
center_x = SCREEN.get_width() // 2
center_y = SCREEN.get_height() // 2

# loading the background music
mixer.music.load('sound/backgroundsound.mp3')
# Set the initial volume
initial_volume = 0.1
sound_effect_volume = 0.5
music_volume = initial_volume
pygame.mixer.music.set_volume(initial_volume)

# play the music
mixer.music.play()

btnSound = pygame.mixer.Sound('sound/buttonclicksound.mp3')
btnSound.set_volume(0.05)
btnType = pygame.mixer.Sound('sound/keypressed.mp3')
btnType.set_volume(0.1)

BG = pygame.image.load('img/bg.png').convert_alpha()
BG = pygame.transform.scale(BG, (WN_LEBAR, WN_TINGGI))

BTN_BG = pygame.image.load('img/buttonBG.png').convert_alpha()
BTN_BG = pygame.transform.scale(BTN_BG, (300, 100))

BTN_S = pygame.image.load('img/setting.png').convert_alpha()
BTN_S = pygame.transform.scale(BTN_S, (85, 55))

LEARDERBOARD_BG = pygame.image.load('img/leaderboard_logo.png').convert_alpha()
LEARDERBOARD_BG = pygame.transform.scale(LEARDERBOARD_BG, (80, 50))

def main_menu():
    is_logged_in = False
    LOGO = pygame.image.load('img/logo.png').convert_alpha()
    LOGO = pygame.transform.scale(LOGO, (600, 500))
    LOGO_RECT = LOGO.get_rect(center=(center_x, 150))
    
    TITLE_FONT = pygame.font.Font('font/font.ttf', 40)
    MENU_TEXT = TITLE_FONT.render("TembaKetik", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(center_x, 250))
    
    LOGIN_BUTTON = Button(image=BTN_BG, pos=(center_x, 400), 
                        text_input="LOGIN", font=font, base_color="#d7fcd4", hovering_color="Gold")
    
    REGISTER_BUTTON = Button(image=BTN_BG, pos=(center_x, 480), 
                            text_input="REGISTER", font=font, base_color="#d7fcd4", hovering_color="GOLD")
    
    PLAY_BUTTON = Button(image=BTN_BG, pos=(center_x, 560), 
                            text_input="PLAY", font=font, base_color="#d7fcd4", hovering_color="Gold")
    OPTIONS_BUTTON = Button(image=BTN_S, pos=(30, 25), 
                            text_input="", font=font, base_color="#828582", hovering_color="GOLD")
    QUIT_BUTTON = Button(image=BTN_BG, pos=(center_x, 640), 
                            text_input="QUIT", font=font, base_color="#d7fcd4", hovering_color="GOLD")
    LEADERBOARD_BUTTON = Button(image=LEARDERBOARD_BG, pos=(center_x + 210, 26), 
                            text_input="", font=font, base_color="#d7fcd4", hovering_color="GOLD")
    
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.blit(LOGO, LOGO_RECT)

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        if is_logged_in:
            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, LEADERBOARD_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.draw(SCREEN)
        else:
            for button in [LOGIN_BUTTON, REGISTER_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.draw(SCREEN)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0] == True:
                if is_logged_in:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        btnSound.play()
                        pygame.mixer.music.stop()
                        play(is_logged_in[0])
                    elif OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        btnSound.play()
                        options()
                    elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        btnSound.play()
                        pygame.quit()
                        sys.exit()
                    elif LEADERBOARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                        btnSound.play()
                        leaderboard()
                else:
                    if LOGIN_BUTTON.checkForInput(MENU_MOUSE_POS):
                        btnSound.play()
                        is_logged_in = login()
                    elif REGISTER_BUTTON.checkForInput(MENU_MOUSE_POS):
                        btnSound.play()
                        register()
                
                    
        pygame.display.update()

# i drawed the textbox but now i don't know how to type in it
def login():
    loginUsername = ''
    loginPassword = ''
    active_textbox = None  # Variable to track the active textbox (None for no textbox)
    
    username_box = pygame.Rect(center_x - 50, 355, 280, 30)
    password_box = pygame.Rect(center_x - 50, 405, 280, 30)
    
    LOGIN_BACK = Button(image=None, pos=(center_x, 775),
                            text_input="BACK", font=font, base_color="Black", hovering_color="Green")
    
    while True:
        LOGIN_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill("gray")
        LOGIN_TEXT = font.render("Login Screen", True, "Black")
        LOGIN_RECT = LOGIN_TEXT.get_rect(center=(center_x, 260))
        SCREEN.blit(LOGIN_TEXT, LOGIN_RECT)
        
        usernamelbl = font.render("Username: ", True, "Black")
        usernamelbl_rect = usernamelbl.get_rect(center=(center_x - 135, 370))
        SCREEN.blit(usernamelbl, (usernamelbl_rect))
        # Draw username input
        username_input = font.render(loginUsername, True, "Black")
        SCREEN.blit(username_input, (username_box.x + 2, username_box.y + 5))
        
        passwordlbl = font.render("Password: ", True, "Black")
        passwordlbl_rect = passwordlbl.get_rect(center=(center_x - 135, 420)) 
        SCREEN.blit(passwordlbl, (passwordlbl_rect))
        # Draw password input
        password_input = font.render('*' * len(loginPassword), True, "Black")
        SCREEN.blit(password_input, (password_box.x + 2, password_box.y + 5))

        # Draw input boxes with different colors based on selection

        if active_textbox == 'username':
            pygame.draw.rect(SCREEN, "Green", username_box, 2)  # Username input box with green border
        else:
            pygame.draw.rect(SCREEN, "Black", username_box, 2)  # Username input box with black border

        if active_textbox == 'password':
            pygame.draw.rect(SCREEN, "Green", password_box, 2)  # Password input box with green border
        else:
            pygame.draw.rect(SCREEN, "Black", password_box, 2)  # Password input box with black border

        # Draw back button

        LOGIN_BACK.changeColor(LOGIN_MOUSE_POS)
        LOGIN_BACK.draw(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0] == True:
                if LOGIN_BACK.checkForInput(LOGIN_MOUSE_POS):
                    return  # Go back to the main menu
                # Check if the mouse click is inside the username input box
                if username_box.collidepoint(event.pos):
                    active_textbox = 'username'
                # Check if the mouse click is inside the password input box
                elif password_box.collidepoint(event.pos):
                    active_textbox = 'password'
                else:
                    active_textbox = None
            if event.type == pygame.KEYDOWN:
                if active_textbox == 'username':
                    if event.key == pygame.K_RETURN:
                        active_textbox = 'password'  # Switch to the next input box
                    elif event.key == pygame.K_BACKSPACE: 
                        loginUsername = loginUsername[:-1]
                    elif len(loginUsername) <= 13:
                        loginUsername += event.unicode if valid_char(event.unicode) else ''
                    keys = pygame.key.get_pressed()
                    if keys [pygame.K_LCTRL] and keys [pygame.K_BACKSPACE]:
                        loginUsername = ''
                elif active_textbox == 'password':
                    if event.key == pygame.K_RETURN:
                        # Add your login logic here
                        if loginPassword == '69420':#utk nyahpepijat
                            return True
                        try:
                            cursor.execute("SELECT Username, Password from player WHERE Username = %s AND Password = %s",(loginUsername, loginPassword))
                            # Fetch the result of the query
                            result = cursor.fetchone()
                            # Check if the result is not empty
                            if result:
                                # The username and password are correct
                                print("Login successful.")
                                cursor.execute("SELECT ID FROM player WHERE Username = %s", (loginUsername,))
                                player_id = cursor.fetchone()[0]
                                return player_id, loginUsername  # Return the entered values
                            else:
                                # The username and password are incorrect
                                print("Invalid username or password.")
                        except mysql.connector.Error as err:
                                # Handle any other MySQL error
                                print("MySQL Error: {}".format(err))
                    elif event.key == pygame.K_BACKSPACE:
                        loginPassword = loginPassword[:-1]
                    elif len(loginPassword) <= 13:
                        loginPassword += event.unicode if valid_char(event.unicode) else ''
                    keys = pygame.key.get_pressed()
                    if keys [pygame.K_LCTRL] and keys [pygame.K_BACKSPACE]:
                        loginPassword = ''
        
        pygame.display.update()

def register():
    registerUsername = ""
    registerPassword = ""
    confirmRegisterPassword = ""
    username_box = pygame.Rect(center_x - 50, 315, 280, 30)
    password_box = pygame.Rect(center_x - 50, 365, 280, 30)
    confirm_password_box = pygame.Rect(center_x - 50, 415, 280, 30)
    active_textbox = None
    
    REGISTER_BACK = Button(image=None, pos=(center_x, 775),
                                text_input="BACK", font=font, base_color="Black", hovering_color="Green")
    while True:
        REGISTER_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("gray")

        REGISTER_TEXT = font.render("Register Screen", True, "Black")
        REGISTER_RECT = REGISTER_TEXT.get_rect(center=(center_x, 260))
        SCREEN.blit(REGISTER_TEXT, REGISTER_RECT)
        
        usernamelbl = font.render("Username: ", True, "Black")
        SCREEN.blit(usernamelbl, (center_x - 245, 330))
        # Draw username input
        username_input = font.render(registerUsername, True, "Black")
        SCREEN.blit(username_input, (username_box.x + 2, username_box.y + 5))
        
        passwordlbl = font.render("Password: ", True, "Black")
        SCREEN.blit(passwordlbl, (center_x - 245, 380))
        # Draw password input
        password_input = font.render('*' * len(registerPassword), True, "Black")
        SCREEN.blit(password_input, (password_box.x + 2, password_box.y + 5))
        
        confirm_passwordlbl = font.render("Confirm :\nPassword", True, "Black")
        SCREEN.blit(confirm_passwordlbl, (center_x - 245, 430))
        # Draw confirm password input
        confirm_password_input = font.render('*' * len(confirmRegisterPassword), True, "Black")
        SCREEN.blit(confirm_password_input, (confirm_password_box.x + 2, confirm_password_box.y + 5))

        # Draw input boxes with different colors based on selection

        if active_textbox == 'username':
            pygame.draw.rect(SCREEN, "Green", username_box, 2)  # Username input box with green border
        else:
            pygame.draw.rect(SCREEN, "Black", username_box, 2)  # Username input box with black border

        if active_textbox == 'password':
            pygame.draw.rect(SCREEN, "Green", password_box, 2)  # Password input box with green border
        else:
            pygame.draw.rect(SCREEN, "Black", password_box, 2)  # Password input box with black border

        if active_textbox == 'confirm_password':
            pygame.draw.rect(SCREEN, "Green", confirm_password_box, 2)  # Confirm Password input box with green border
        else:
            pygame.draw.rect(SCREEN, "Black", confirm_password_box, 2)  # Confirm Password input box with black border

        # Draw back button
        

        REGISTER_BACK.changeColor(REGISTER_MOUSE_POS)
        REGISTER_BACK.draw(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if pygame.mouse.get_pressed()[0] == True:
                if REGISTER_BACK.checkForInput(REGISTER_MOUSE_POS):
                    return 
                if username_box.collidepoint(event.pos):
                    active_textbox = 'username'
                elif password_box.collidepoint(event.pos):
                    active_textbox = 'password'
                elif confirm_password_box.collidepoint(event.pos):
                    active_textbox = 'confirm_password'
                else:
                    active_textbox = None
            
            if event.type == pygame.KEYDOWN:
                if active_textbox == 'username':
                    if event.key == pygame.K_RETURN:
                        active_textbox = 'password'  # Switch to the next input box'
                    elif event.key == pygame.K_BACKSPACE:
                        registerUsername = registerUsername[:-1]
                    elif len(registerUsername) <= 13:
                        registerUsername += event.unicode if valid_char(event.unicode) else ''
                    keys = pygame.key.get_pressed()
                    if keys [pygame.K_LCTRL] and keys [pygame.K_BACKSPACE]:
                        registerUsername = ''
                elif active_textbox == 'password':
                    if event.key == pygame.K_RETURN:
                        active_textbox = 'confirm_password'  # Switch to the next input box'
                    elif event.key == pygame.K_BACKSPACE:
                        registerPassword = registerPassword[:-1]
                    elif len(registerPassword) <= 13:
                        registerPassword += event.unicode if valid_char(event.unicode) else ''
                    keys = pygame.key.get_pressed()
                    if keys [pygame.K_LCTRL] and keys [pygame.K_BACKSPACE]:
                        registerPassword = ''
                elif active_textbox == 'confirm_password':
                    if event.key == pygame.K_RETURN:
                        if all([registerUsername, registerPassword, confirmRegisterPassword]):
                            if valid_char(registerUsername):
                                if registerPassword == confirmRegisterPassword:
                                        try:
                                            cursor.execute('INSERT INTO player (Username, Password) VALUES (%s,%s)', (registerUsername, registerPassword))
                                            db.commit()
                                            print("Registration successful!")
                                            return
                                        except mysql.connector.IntegrityError as err:
                                            print("Username already taken.")
                                            print(err)
                                        except mysql.connector.Error as err:
                                            print("MySQL Error: {}".format(err))
                                else:
                                    print("Passwords do not match. Please try again.")
                            else:
                                print("Invalid username. Please try again.")
                        else:
                            print("Please fill in all fields before registering.")

                    elif event.key == pygame.K_BACKSPACE:
                        confirmRegisterPassword = confirmRegisterPassword[:-1]
                    elif len(confirmRegisterPassword) <= 13:
                        confirmRegisterPassword += event.unicode if valid_char(event.unicode) else ''
                    keys = pygame.key.get_pressed()
                    if keys [pygame.K_LCTRL] and keys [pygame.K_BACKSPACE]:
                        confirmRegisterPassword = ''
            pygame.display.update()

def options():
    global sound_effect_volume, music_volume  # Declare global variables

    current_language = 'English'
    active_slider = None  # Variable to keep track of the active slider

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))
        
        OPTIONS_TEXT = font.render("Settings.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(center_x, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Display SOUND EFFECT level
        sound_effect_text = font.render("Sound Effect:", True, "Black")
        sound_effect_rect = sound_effect_text.get_rect(center=(center_x - 25, 320))
        SCREEN.blit(sound_effect_text, sound_effect_rect)

        # SOUND EFFECT slider
        sound_effect_slider = pygame.Rect(center_x - 100, 350, 200, 20)
        pygame.draw.rect(SCREEN, "Gray", sound_effect_slider)
        pygame.draw.rect(SCREEN, "Green", (sound_effect_slider.x, sound_effect_slider.y, sound_effect_volume * 200, 20))

        # Display MUSIC level
        music_text = font.render(f"Music: {int(music_volume * 100)}%", True, "Black")
        music_rect = music_text.get_rect(center=(center_x, 400))
        SCREEN.blit(music_text, music_rect)

        # MUSIC slider
        music_slider = pygame.Rect(center_x - 100, 430, 200, 20)
        pygame.draw.rect(SCREEN, "Gray", music_slider)
        pygame.draw.rect(SCREEN, "Green", (music_slider.x, music_slider.y, music_volume * 200, 20))

        # Language button
        LANGUAGE_BUTTON = "Malay" if current_language == 'English' else "English"
        language_button = Button(image=None, pos=(center_x, 550),
                                text_input=f"Change Language: {current_language}", font=font, base_color="Black", hovering_color="Green")
        language_button.changeColor(OPTIONS_MOUSE_POS)
        language_button.draw(SCREEN)

        OPTIONS_BACK = Button(image=None, pos=(center_x, 620),
                             text_input="BACK", font=font, base_color="Black", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.draw(SCREEN)

        # Draw active slider indicator
        if active_slider == "SoundEffect":
            pygame.draw.rect(SCREEN, "Red", sound_effect_slider, 2)
        elif active_slider == "Music":
            pygame.draw.rect(SCREEN, "Red", music_slider, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll Up
                    if active_slider == "SoundEffect":
                        sound_effect_volume = min(1, sound_effect_volume + 0.1)
                        btnType.set_volume(sound_effect_volume)  # Set typing sound volume
                        btnSound.set_volume(sound_effect_volume)  # Set button click sound volume
                    elif active_slider == "Music":
                        music_volume = min(1, music_volume + 0.1)
                        pygame.mixer.music.set_volume(music_volume)  # Set music volume
                elif event.button == 5:  # Scroll Down
                    if active_slider == "SoundEffect":
                        sound_effect_volume = max(0, sound_effect_volume - 0.1)
                        btnType.set_volume(sound_effect_volume)  # Set typing sound volume
                        btnSound.set_volume(sound_effect_volume)  # Set button click sound volume
                    elif active_slider == "Music":
                        music_volume = max(0, music_volume - 0.1)
                        pygame.mixer.music.set_volume(music_volume)  # Set music volume
                elif sound_effect_slider.collidepoint(event.pos):
                    active_slider = "SoundEffect"
                elif music_slider.collidepoint(event.pos):
                    active_slider = "Music"
                elif language_button.checkForInput(OPTIONS_MOUSE_POS):
                    current_language = "Malay" if current_language == 'English' else "English"
                elif OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return
            elif event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:  # Left mouse button is pressed
                if active_slider == "SoundEffect":
                    sound_effect_volume = max(0, min(1, (event.pos[0] - sound_effect_slider.x) / 200))
                    btnType.set_volume(sound_effect_volume)  # Set typing sound volume
                    btnSound.set_volume(sound_effect_volume)  # Set button click sound volume
                elif active_slider == "Music":
                    music_volume = max(0, min(1, (event.pos[0] - music_slider.x) / 200))
                    pygame.mixer.music.set_volume(music_volume)  # Set music volume
                    
        pygame.display.update()

def help():
    print('help pressed')        
def leaderboard():
    small_font = pygame.font.Font("font/font.ttf",10)
    leaderboard_list = []
    cursor.execute("SELECT DISTINCT player.ID FROM score LEFT JOIN accuracy ON score.accuracy_ID = accuracy.ID LEFT JOIN missed ON accuracy.miss_ID = missed.ID LEFT JOIN wpm ON score.WPM_ID = wpm.ID LEFT JOIN player ON wpm.player_ID = player.ID")
    playersID_list = cursor.fetchall() #list player yg pernah bermain sahaja
    print(playersID_list)
    playersID_list = [player[0] for player in playersID_list]
    print(playersID_list)
    
    for i in playersID_list:
        cursor.execute("SELECT player.Username, wpm.typed_word_count, missed.count, wpm.nilai, accuracy.percentage, MAX(score.nilai) FROM score LEFT JOIN accuracy ON score.accuracy_ID = accuracy.ID LEFT JOIN missed ON accuracy.miss_ID = missed.ID LEFT JOIN wpm ON score.WPM_ID = wpm.ID LEFT JOIN player ON wpm.player_ID = player.ID WHERE player.ID = %s", (i, ))
        leaderboard_list.append(cursor.fetchone())
        print(leaderboard_list)
        
    leaderboard_list.sort(key=lambda x: x[-1], reverse=True)
    print(leaderboard_list)
    
    BACK = Button(image=None, pos=(center_x, 775),
                            text_input="BACK", font=font, base_color="#d7fcd4", hovering_color="Gold")
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.blit(BG, (0, 0))
        
        transparent_surface = pygame.Surface (SCREEN.get_size(), pygame.SRCALPHA) # Create a transparent surface
        transparent_surface.fill ((0, 0, 0, 169)) # Fill the surface with a semi-transparent black color
        SCREEN.blit(transparent_surface, (0, 0)) # Blit the transparent surface to the screen)
        
        leaderboard_lbl = font.render("Leaderboard", True, "White")
        SCREEN.blit(leaderboard_lbl, leaderboard_lbl.get_rect(center=(center_x, 20)))
        
        leaderboard_lbl = small_font.render("(Username - Highest Score)", True, "White")
        SCREEN.blit(leaderboard_lbl, leaderboard_lbl.get_rect(center=(center_x, 40)))
        
        for i, row in enumerate(leaderboard_list):
            username, typed_word_count, miss, wpm, percentage, highest_score = row#future update
            text = font.render(f"{i+1}. {username} - {highest_score}", True, "White")
            SCREEN.blit(text, (center_x - text.get_width() // 2, 100 + i * 50))
        
        BACK.changeColor(MOUSE_POS)
        BACK.draw(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(MOUSE_POS):
                    return
        
        pygame.display.update()

def pause():
    transparent_surface = pygame.Surface (SCREEN.get_size(), pygame.SRCALPHA) # Create a transparent surface
    transparent_surface.fill ((0, 0, 0, 169)) # Fill the surface with a semi-transparent black color
    SCREEN.blit(transparent_surface, (0, 0)) # Blit the transparent surface to the screen)
    
    RESUME_BTN = Button(image=BTN_BG, pos=(center_x, 200),
                            text_input="RESUME", font=font, base_color="#d7fcd4", hovering_color="Gold")
    OPTIONS_BTN = Button(image=BTN_BG, pos=(center_x, 300),
                            text_input="OPTIONS", font=font, base_color="#d7fcd4", hovering_color="Gold")
    HELP_BTN = Button(image=BTN_BG, pos=(center_x, 400),
                            text_input="HELP", font=font, base_color="#d7fcd4", hovering_color="Gold")
    MAIN_MENU_BTN = Button(image=BTN_BG, pos=(center_x, 500),
                            text_input="MAIN MENU", font=font, base_color="#d7fcd4", hovering_color="Gold")
    QUIT_BTN = Button(image=BTN_BG, pos=(center_x, 600),
                            text_input="QUIT", font=font, base_color="#d7fcd4", hovering_color="Gold")
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        
        pause_lbl = font.render("Paused", True, "White")
        SCREEN.blit(pause_lbl, pause_lbl.get_rect(center=(center_x, 69)))#ni kene letak dlm while loop klo x dia invisible
        
        RESUME_BTN.changeColor(MOUSE_POS)
        RESUME_BTN.draw(SCREEN)
        
        OPTIONS_BTN.changeColor(MOUSE_POS)
        OPTIONS_BTN.draw(SCREEN)
        
        HELP_BTN.changeColor(MOUSE_POS)
        HELP_BTN.draw(SCREEN)
        
        MAIN_MENU_BTN.changeColor(MOUSE_POS)
        MAIN_MENU_BTN.draw(SCREEN)
        
        QUIT_BTN.changeColor(MOUSE_POS)
        QUIT_BTN.draw(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BTN.checkForInput(MOUSE_POS):
                    return
                if OPTIONS_BTN.checkForInput(MOUSE_POS):
                    options()
                    return
                if HELP_BTN.checkForInput(MOUSE_POS):
                    help()
                if MAIN_MENU_BTN.checkForInput(MOUSE_POS):
                    to_main_menu = True
                    return to_main_menu
                if QUIT_BTN.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                
        pygame.display.update()
        
def play(player_id):
    clock = pygame.time.Clock()
    
    bil_ombak = 0
    
    bil_musuh = {
        'Zombetta' : 0,
        'Basic' : 3,
        'Gargantuan' : 0,
    }
    
    group_bullets = pygame.sprite.Group()
    
    pemain = Pemain(player_id, center_x, WN_TINGGI - 100, PLAYER_ASSETS['Player'], group_bullets)
    latar = Latar(0, WN_TINGGI, 0, 0.2)
    
    group_pemain = pygame.sprite.GroupSingle()
    group_pemain.add(pemain)
    
    char_typed = ''
    char_updated = False
    
    group_musuh = pygame.sprite.LayeredUpdates()
    group_musuh,bil_ombak = jana_ombak(bil_ombak, group_musuh, bil_musuh, pemain.rect, sound_effect_volume)
    text_ombak = font.render(str(bil_ombak), True, (255,255,255), (0, 0, 0))#can remove?
    # Create a custom timer event
    WAVE_EVENT= pygame.USEREVENT + 1
    timer_setted = False
    
    running = True
    while running:
        # Get a list of events
        events = pygame.event.get()
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        # Loop through the events
        for event in events:
            if event.type == WAVE_EVENT:
                group_musuh,bil_ombak = jana_ombak(bil_ombak, group_musuh, bil_musuh, pemain.rect, sound_effect_volume)
                pygame.time.set_timer(WAVE_EVENT, 0)# Reset the timer to 0 to stop it
                timer_setted = False
            # Check if the user has clicked the close button
            if event.type == pygame.QUIT:
                # Exit the loop and quit the program
                running = False
                pygame.quit()
                db.close()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    to_main_menu = pause()
                    if to_main_menu:
                        return
                if event.key == pygame.K_BACKSPACE:
                    char_typed = char_typed[:-1]  #amik smua value selain akhir sekali dlm list tu
                else:
                    btnType.play()
                    char_typed += event.unicode #utk amik keyboard text input
                    char_updated = True 
        
        #biar x de trail
        SCREEN.fill((0, 0, 0))
        latar.gerak(SCREEN, len(group_pemain.sprites()) >= 1)
        
        # text = font.render(char_typed, True, (255, 255, 255), (0, 0, 0))
        # SCREEN.blit(text, (0, 0))
        
        if group_musuh.sprites() == [] and len(group_pemain.sprites()) >= 1:
            text_ombak = font.render(f'WAVE:{bil_ombak} CLEARED', True, (255,255,255))
            SCREEN.blit(text_ombak, (100, center_y))
            if not timer_setted:
                pygame.time.set_timer(WAVE_EVENT, 3000)#start 3s timer
                timer_setted = True
                
        group_bullets.draw(SCREEN)
        group_bullets.update(group_musuh)
        
        group_pemain.draw(SCREEN)
        group_pemain.update(SCREEN, group_musuh, char_typed, char_updated, cursor, db, music_volume)
        char_updated = False
        
        group_musuh.draw(SCREEN)
        group_musuh.update(SCREEN, group_musuh)
        
        if not pemain.hidup:
            pemain.show_stats(SCREEN)
            BACK_BTN = Button(image=None, pos=(center_x, 775), 
                            text_input="BACK TO MAIN MENU", font=font, base_color="#d7fcd4", hovering_color="Gold")
            BACK_BTN.changeColor(pygame.mouse.get_pos())
            BACK_BTN.draw(SCREEN)
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK_BTN.checkForInput(PLAY_MOUSE_POS):
                        mixer.music.play()
                        return
        
        pygame.display.flip()
        clock.tick(FPS)
        pygame.display.set_caption(f'TembaKetik FPS: {clock.get_fps() :.1f}')# f' ' tu utk tukar jdi f-string (mcm string data type)
        print('mouse coords:', pygame.mouse.get_pos())

main_menu()

