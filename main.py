import pygame,sys,asyncio,mysql.connector

from pygame import mixer
from scripts.pemalar import *
from scripts.latar import Latar
from scripts.musuh import jana_ombak, assets_load
from scripts.pemain import Pemain, is_name_valid
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
icon = pygame.image.load('img/kapal_angkasa.PNG')
pygame.display.set_icon(icon)
SCREEN = pygame.display.set_mode((WN_LEBAR, WN_TINGGI))

clock = pygame.time.Clock()

assets = {
    'Tiny_Kamikaze' : assets_load('renew/tiniykamikazeship/tinykamikazeship1.PNG',60),
    'Kamikaze' : assets_load('renew/kamikazeship/kamikazeship1.PNG',40),
    'Gunner' : assets_load('renew/gunnership/gunnership1.PNG',69),
}

font = pygame.font.Font("font/font.ttf",20)

# Get the center of the screen
center_x = SCREEN.get_width() // 2
center_y = SCREEN.get_height() // 2



latar = Latar(0, WN_TINGGI, 0, 0.2)

# loading the background music
mixer.music.load('sound/backgroundsound.mp3')
# Set the initial volume
initial_volume = 0.1
pygame.mixer.music.set_volume(initial_volume)

# play the music
mixer.music.play()

btnSound = pygame.mixer.Sound('sound/buttonclicksound.mp3')
btnSound.set_volume(0.05)
btnType = pygame.mixer.Sound('sound/keypressed.mp3')
btnType.set_volume(0.1)

def main_menu():
    is_logged_in = False
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
    
    LOGIN_BUTTON = Button(image=BTN_BG, pos=(center_x, 400), 
                        text_input="LOGIN", font=font, base_color="#d7fcd4", hovering_color="Gold")
    
    REGISTER_BUTTON = Button(image=BTN_BG, pos=(center_x, 480), 
                            text_input="REGISTER", font=font, base_color="#d7fcd4", hovering_color="GOLD")
    
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
        if is_logged_in:
            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
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
            if event.type == pygame.MOUSEBUTTONDOWN:
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
        LOGIN_BACK = Button(image=None, pos=(center_x, 500),
                            text_input="BACK", font=font, base_color="Black", hovering_color="Green")

        LOGIN_BACK.changeColor(LOGIN_MOUSE_POS)
        LOGIN_BACK.draw(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
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
                        loginUsername += event.unicode
                    # Adjust the position of the input text based on the length of the text
                    username_input = font.render("Username: " + loginUsername, True, "Black")
                    username_rect = username_input.get_rect(center=(center_x - 75, 370)) #ni mcm x di run je
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
                    else:
                        loginPassword += event.unicode
                    # Adjust the position of the input text based on the length of the text
                    password_input = font.render("Password: " + '*' * len(loginPassword), True, "Black")
                    password_rect = password_input.get_rect(center=(center_x - 75, 420))
        
        pygame.display.update()

def register():
    global registerUsername, registerPassword, confirmRegisterPassword #global ni utk apa?
    registerUsername = ""
    registerPassword = ""
    confirmRegisterPassword = ""
    active_textbox = None

    while True:
        REGISTER_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("gray")

        REGISTER_TEXT = font.render("Register Screen", True, "Black")
        REGISTER_RECT = REGISTER_TEXT.get_rect(center=(center_x, 260))
        SCREEN.blit(REGISTER_TEXT, REGISTER_RECT)

        # Draw username input
        username_input = font.render("Username: " + registerUsername, True, "Black")
        username_rect = username_input.get_rect(center=(center_x - 75, 330))
        SCREEN.blit(username_input, username_rect)

        # Draw password input
        password_input = font.render("Password: " + '*' * len(registerPassword), True, "Black")
        password_rect = password_input.get_rect(center=(center_x - 75, 380))
        SCREEN.blit(password_input, password_rect)

        # Draw confirm password input
        confirm_password_input = font.render("ConfirmPass: " + '*' * len(confirmRegisterPassword), True, "Black")
        confirm_password_rect = confirm_password_input.get_rect(center=(center_x - 80, 430))
        SCREEN.blit(confirm_password_input, confirm_password_rect)

        # Draw input boxes with different colors based on selection
        username_box = pygame.Rect(center_x + 25, 315, 200, 30)
        password_box = pygame.Rect(center_x + 25, 365, 200, 30)
        confirm_password_box = pygame.Rect(center_x + 25, 415, 200, 30)

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
        REGISTER_BACK = Button(image=None, pos=(center_x, 480),
                                text_input="BACK", font=font, base_color="Black", hovering_color="Green")

        REGISTER_BACK.changeColor(REGISTER_MOUSE_POS)
        REGISTER_BACK.draw(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
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
                    else:
                        registerUsername += event.unicode
                elif active_textbox == 'password':
                    if event.key == pygame.K_RETURN:
                        active_textbox = 'confirm_password'  # Switch to the next input box'
                    elif event.key == pygame.K_BACKSPACE:
                        registerPassword = registerPassword[:-1]
                    else:
                        registerPassword += event.unicode
                elif active_textbox == 'confirm_password':
                    if event.key == pygame.K_RETURN:
                        if registerPassword == confirmRegisterPassword and is_name_valid(registerUsername):
                            try:
                                cursor.execute('INSERT INTO player (Username, Password) VALUES (%s,%s)',(registerUsername, registerPassword))
                                db.commit()
                                print("Registration successful!")
                                return registerUsername, registerPassword, confirmRegisterPassword  # Return the entered values #values nya buat apa and pegi mne?
                            except mysql.connector.IntegrityError as err:
                                # Handle the error if the username already exists
                                print("Username already taken.")
                                print(err)
                            except mysql.connector.Error as err:
                                # Handle any other MySQL error
                                print("MySQL Error: {}".format(err))
                        else:
                            print("Not valid username or passwords do not match. Please try again.")
                    elif event.key == pygame.K_BACKSPACE:
                        confirmRegisterPassword = confirmRegisterPassword[:-1]
                    else:
                        confirmRegisterPassword += event.unicode

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
        OPTIONS_BACK.draw(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return

        pygame.display.update()

def play(player_id):
    pemain = Pemain(player_id, center_x, WN_TINGGI - 100, 'renew/PlayerShip/playership1.PNG')
    
    group_pemain = pygame.sprite.GroupSingle()
    group_pemain.add(pemain)
    
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
                    btnType.play()
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
        group_pemain.update(SCREEN, group_musuh, char_typed, char_updated, cursor, db)
        char_updated = False
        
        group_musuh.draw(SCREEN)
        group_musuh.update(SCREEN, group_musuh)
        
        pygame.display.flip()
        clock.tick(FPS)
        pygame.display.set_caption(f'TembaKetik FPS: {clock.get_fps() :.1f}')# f' ' tu utk tukar jdi f-string (mcm string data type)
        print('pemain wpm:',pemain.wpm)

main_menu()

