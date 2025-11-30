# Code for developing car racing game in python

# Importing all Modules

# Importing the Pygame library for game development

import pygame

# Importing the Time module for handling 
# time-related operations

import time

# Importing the Randam module for handling 

import random

# Loading and rendering fonts

import pygame.freetype

# provides functions and variables which are used to manipulate different parts of the Python Runtime Environment

import sys

# Initializing Pygame

pygame.init()


# Opening the file Score.txt and updating the score after every game

def score_write(Data):
    with open("score.txt", "w") as score:
        score.write(Data)


# Reading the file score.dat

def read_score():
    with open("score.txt", "r") as score:
        final_score = score.read()
        return final_score


score_write("0")
carimg = "car_1.png"

# Colour Codes

black = (0, 0, 0)
bright_black = (70, 70, 70)
white = (255, 255, 255)
red = (255, 50, 50)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)
yellow_ochre = (200, 174, 114)
yellow = (255, 255, 0)
dark_green = (80, 125, 42)
skyblue = (100, 100, 255)

# Setting the display mode with specified width and height

# Width of the game window

display_width = 800

# Height of the game window

display_hieght = 600
screen = pygame.display.set_mode((display_width, display_hieght))

# Setting a Title for the window

pygame.display.set_caption("Racing Beast!!!")

# Setting a Logo for the window

logo = pygame.image.load('car_1.png')
pygame.display.set_icon(logo)

# Loading all the image assets
car_images = [
    pygame.image.load('car_1.png'),
    pygame.image.load('car_2.png'),
    pygame.image.load("car_3.png"),
    pygame.image.load("car_4.png"),
    pygame.image.load("car_5.png"),
    pygame.image.load("car_6.png"),
    pygame.image.load("car_7.png"),
    pygame.image.load("car_8.png"),
    pygame.image.load("car_9.png"),
    pygame.image.load("car_10.png"),
    pygame.image.load("car_11.png")

]

car_names = ["car_1.png", "car_2.png", "car_3.png", "car_4.png",
             "car_5.png", "car_6.png", "car_7.png", "car_8.png", "car_9.png", "car_10.png", "car_11.png"]

carimg = pygame.image.load("car_1.png")
car_rect = carimg.get_rect()
background = pygame.image.load("Screenshot (143) - Copy - Copy.png")
intro_background = pygame.image.load("intro_background2.jpg")
instruction_background = pygame.image.load(
    "cartoon-city-street-metropolis-style-animation-3d-pour-enfants_720722-6853.jpg")
paused_background = pygame.image.load("cartoon-city-street-metropolis-style-animation-3d-pour-enfants_720722-6896.jpg")
Crash = pygame.image.load("Screenshot__142_-removebg-preview.png")
fuel_img = pygame.image.load('4185548_prev_ui.png')
coin_img = pygame.image.load("coin.png")  # Load your coin image
coin_x = random.randrange(250, display_width - 370)  # Randomize initial coin position
coin_y = -750  # Initial coin position above the screen
coin_width = 50
coin_height = 50
coin_speed = 5  # Adjust this value for the coin's falling speed
coin_collected = False

# Setting a Clock

clock = pygame.time.Clock()

# Setting the car width

car_width = 50

#  Initialize pause state

Pause = False

# Setting the Time to be  zero until Game Loop Runs

timer_break_point = 0

# Setting the hieght and width of car shield

shield_width = 50
shield_height = 100
car_height = 90
shield_x = 200
shield_y = 300
shield_active = False

# Functionalities for fuel of car

fuel_max = 1000
fuel = fuel_max
fuel_decrease_rate = 0.2
fuel_bar_width = 10
fuel_bar_height = 300
fuel_bar_color = (0, 255, 0)  # Green
low_fuel_color = (255, 0, 0)  # Red
fuel = 1000

# Loading all the songs and Sound Effects

intro_song = pygame.mixer.music.load("Grand-Theft-Auto-San-Andreas-Theme-Song - Copy.mp3")
pygame.mixer.music.play()
Sound_crash = pygame.mixer.Sound("Hammer Smashed Face")
sound_crash = pygame.mixer.Sound("collision-reverb-103405.mp3")
countdown_beep = pygame.mixer.Sound("robotic-countdown-43935.mp3")
mouseclick_beep = pygame.mixer.Sound("interface-124464.mp3")
coin_beep = pygame.mixer.Sound("Bag-of-Coins-A-www.fesliyanstudios.com - Copy.mp3")
fuel_beep = pygame.mixer.Sound("Water Drop Sound - Copy.mp3")

# Funtion to make the depleation of fuel

def decrease_fuel():
    global fuel
    fuel -= fuel_decrease_rate
    if fuel < 0:
        fuel = 0


# Funtion to make the fuel bar

def draw_vertical_fuel_tank_bar(fuel):
    fuel_tank_bar_width = 30
    fuel_tank_bar_height = 300
    fuel_tank_color = (0, 255, 0)  # Green when fuel is sufficient
    if fuel < 50:
        fuel_tank_color = (255, 0, 0)  # Red when fuel is less than 10

    pygame.draw.rect(screen, fuel_tank_color, [650, 150, fuel_tank_bar_width, (fuel / fuel_max) * fuel_tank_bar_height])
    pygame.draw.rect(screen, black,
                     [display_width - fuel_tank_bar_width - 10, 10, fuel_tank_bar_width, fuel_tank_bar_height], 2)


# Funtion to refill fuel

def refill_fuel():
    global fuel
    fuel = 1000


# Funtion to show the fuel text

def draw_fuel_text(fuel):
    font = pygame.font.Font("freesansbold.ttf", 25)
    fuel_text = font.render("Fuel: {}".format(fuel), True, white)
    screen.blit(fuel_text, (634.5, 460))


# Making a car selector button

def Car_Selector():
    global screen

    pygame.init()
    screen = pygame.display.set_mode((display_width, display_hieght))
    pygame.display.set_caption("RACING BEAST!!!")
    logo = pygame.image.load('car_1.png')
    pygame.display.set_icon(logo)
    # Set up the display
    screen = pygame.display.set_mode((display_width, display_hieght))
    pygame.display.set_caption("RACING BEAST!!!")

    # Load car images
    car_images = [
        pygame.image.load('car_1.png').convert_alpha(),
        pygame.image.load('car_2.png').convert_alpha(),
        pygame.image.load('car_3.png').convert_alpha(),
        pygame.image.load('car_4.png').convert_alpha(),
        pygame.image.load('car_5.png').convert_alpha(),
        pygame.image.load('car_6.png').convert_alpha(),
        pygame.image.load('car_7.png').convert_alpha(),
        pygame.image.load('car_8.png').convert_alpha(),
        pygame.image.load('car_9.png').convert_alpha(),
        pygame.image.load('car_10.png').convert_alpha(),
        pygame.image.load('car_11.png').convert_alpha(),
        pygame.image.load('car_12.png').convert_alpha(),
        pygame.image.load('car_13.png').convert_alpha(),
        pygame.image.load('car_14.png').convert_alpha(),
        pygame.image.load('car_15.png').convert_alpha(),
        pygame.image.load('car_16.png').convert_alpha(),
        pygame.image.load('car_17.png').convert_alpha(),
        pygame.image.load('car_18.png').convert_alpha(),
        pygame.image.load('car_19.png').convert_alpha(),
        pygame.image.load('car_20.png').convert_alpha(),
        pygame.image.load('car_21.png').convert_alpha(),
        pygame.image.load('car_22.png').convert_alpha(),
        pygame.image.load('car_23.png').convert_alpha(),
        pygame.image.load('car_24.png').convert_alpha(),
        pygame.image.load('car_25.png').convert_alpha(),
        pygame.image.load('car_26.png').convert_alpha(),
        pygame.image.load('car_27.png').convert_alpha(),
        pygame.image.load('car_28.png').convert_alpha(),
        pygame.image.load('car_29.png').convert_alpha(),
        pygame.image.load('car_30.png').convert_alpha(),
        pygame.image.load('car_31.png').convert_alpha(),
        pygame.image.load('car_32.png').convert_alpha(),
        pygame.image.load('car_33.png').convert_alpha(),
        pygame.image.load('car_34.png').convert_alpha(),
        pygame.image.load('car_35.png').convert_alpha(),
        pygame.image.load('car_36.png').convert_alpha(),
        pygame.image.load('car_37.png').convert_alpha(),
        pygame.image.load('car_38.png').convert_alpha(),
        pygame.image.load('car_39.png').convert_alpha(),
        pygame.image.load('car_40.png').convert_alpha(),
        pygame.image.load('car_41.png').convert_alpha()

    ]

    current_car = 0

    def display_current_car():

        screen.fill(black)  # Fill the screen with white color
        largetext = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objectsss("Click on Escape Button to Select", largetext)
        TextRect.center = ((display_width / 2), 30)
        screen.blit(TextSurf, TextRect)
        current_image = car_images[current_car]
        screen.blit(current_image, (display_width // 2 - current_image.get_width() // 2,
                                    display_hieght // 2 - current_image.get_height() // 2))
        pygame.display.flip()

    running = True

    while running:

        global carimg

        display_current_car()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    # Move to the next car image
                    mouseclick_beep.play()
                    current_car = (current_car + 1) % len(car_images)
                    display_current_car()
                    pygame.display.update()

                elif event.key == pygame.K_LEFT:
                    # Move to the previous car image
                    mouseclick_beep.play()
                    current_car = (current_car - 1) % len(car_images)
                    display_current_car()
                    pygame.display.update()

                elif event.key == pygame.K_ESCAPE:

                    mouseclick_beep.play()
                    carimg = pygame.image.load(car_names[current_car])
                    pygame.display.update()

                    intro_loop()


# Making a Stopwatch

def timer():
    font = pygame.freetype.SysFont(None, 28)

    ticks = pygame.time.get_ticks() - timer_break_point
    millis = ticks % 1000
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 24)
    out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
    font.render_to(screen, (30, 520), out, pygame.Color('dodgerblue'))
    font.render_to(screen, (10, 480), "Time Survived:", pygame.Color('white'))

    pygame.display.flip()


# Making the Intro Screen

def intro_loop():
    Sound_crash.stop()

    intro = True

    while intro:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                SystemExit()

        # Display background image

        screen.blit(intro_background, (0, 0))

        # Render and display "CAR GAME" text

        largetext = pygame.font.Font("freesansbold.ttf", 100)
        TextSurf, TextRect = text_object("CAR GAME", largetext)
        TextRect.center = (400, 100)
        screen.blit(TextSurf, TextRect)

        # Render and display "START" button

        button("START", 25, 520, 100, 50, dark_green, green, "play")

        # Render and display "QUIT" button

        button("QUIT", 400, 520, 100, 50, bright_red, red, "quit")

        # Render and display "INSTRUCTION" button

        button("INSTRUCTIONS", 150, 520, 200, 50, blue, skyblue, "intro")

        # Render and display "SELECT CAR" button

        button("SELECT CAR", 550, 520, 200, 50, yellow_ochre, yellow, "select_car")

        pygame.display.update()  # Update the display
        clock.tick(50)


# Making the Button Function
# Function to create a button with specified parameters
# msg: The text to be displayed on the button
# x, y: The coordinates of the top-left corner of the button
# w, h: The width and height of the button
# ic: The color of the button when inactive
# ac: The color of the button when active (hovered over)
# action: The action to be performed when the button is clicked

def button(msg, x, y, w, h, ic, ac, action=None):
    # Get the current mouse position

    mouse = pygame.mouse.get_pos()

    # Get the current state of mouse buttons

    click = pygame.mouse.get_pressed()

    # Check if mouse is within the button's boundaries

    if x + w > mouse[0] > x and y + h > mouse[1] > y:

        # Draw button with active color

        pygame.draw.rect(screen, ac, (x, y, w, h))

        # Check if left mouse button is clicked
        # and action is specified

        if click[0] == 1 and action is not None:

            mouseclick_beep.play()

            # If action is "play", call the countdown()

            if action == "play":
                pygame.mixer.music.pause()
                countdown_beep.play()
                countdown()

            # If action is "quit", quit the game

            elif action == "quit":

                pygame.quit()
                quit()
                SystemExit()

            # If action is "intro", call the introduction() function

            elif action == "intro":

                pygame.mixer.music.unpause()
                introduction()

            # If action is "menu", call the intro_loop() function

            elif action == "menu":

                pygame.mixer.music.unpause()
                Sound_crash.stop()
                intro_loop()

            # If action is "pause", call the paused() function

            elif action == "pause":

                pygame.mixer.music.unpause()
                paused()

            # If action is "unpause", call the unpaused() function

            elif action == "unpause":

                pygame.mixer.music.pause()
                Sound_crash.play()
                unpaused()

            # If action is "select_car", call the Car_Selector() function

            elif action == "select_car":

                Car_Selector()
    else:

        # Draw button with inactive color

        pygame.draw.rect(screen, ic, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_objectsss(msg, smalltext)
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textsurf, textrect)


# Function to display the introduction screen

def introduction():
    Sound_crash.stop()
    pygame.mixer.music.unpause()

    introduction = True

    while introduction:

        # Get events from the event queue

        for event in pygame.event.get():

            # If the 'QUIT' event is triggered
            # (e.g., window closed)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                SystemExit()

        # Draw the instruction background

        screen.blit(instruction_background, (0, 0))

        # Set font for large text

        largetext = pygame.font.Font("freesansbold.ttf", 80)

        # Set font for small text

        smalltext = pygame.font.Font("freesansbold.ttf", 20)

        # Set font for medium text

        mediumtext = pygame.font.Font("freesansbold.ttf", 40)

        # Render and draw the instruction text

        textSurf, textRect = text_object("    THIS IS A CAR GAME WHERE YOU HAVE TO DODGE INCOMMING CARS  ", smalltext)
        textRect.center = (350, 200)
        TextSurf, TextRect = text_object("INSTRUCTION ", largetext)
        TextRect.center = (370, 100)
        screen.blit(TextSurf, TextRect)
        screen.blit(textSurf, textRect)

        # Render and draw the control instructions

        stextSurf, stextRect = text_object(" • ARROW LEFT : LEFT TURN ", smalltext)
        stextRect.center = (350, 400)
        hTextSurf, hTextRect = text_object(" • ARROW RIGHT : RIGHT TURN ", smalltext)
        hTextRect.center = (350, 450)
        atextSurf, atextRect = text_object(" • A : ACCELERATION ", smalltext)
        atextRect.center = (350, 500)
        rtextSurf, rtextRect = text_object(" • B : BRAKE ", smalltext)
        rtextRect.center = (350, 550)
        ptextSurf, ptextRect = text_object(" • P : PAUSE ", smalltext)
        ptextRect.center = (350, 350)
        sTextSurf, sTextRect = text_object("  CONTROLS ", mediumtext)
        sTextRect.center = (350, 300)

        screen.blit(sTextSurf, sTextRect)
        screen.blit(stextSurf, stextRect)
        screen.blit(hTextSurf, hTextRect)
        screen.blit(atextSurf, atextRect)
        screen.blit(rtextSurf, rtextRect)
        screen.blit(ptextSurf, ptextRect)

        # Render and draw the 'BACK' button

        button(" BACK ", 600, 450, 100, 50, blue, skyblue, "menu")

        pygame.display.update()  # Update the display
        clock.tick(30)  # Limit frame rate to 30 FPS


# Making the Pause function

def paused():
    Sound_crash.stop()
    pygame.mixer.music.unpause()
    global Pause

    paused_start_time = pygame.time.get_ticks()

    # Loop for handling events during pause state

    while Pause:

        global timer_break_point

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                SystemExit()

        screen.blit(paused_background, (0, 0))

        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_object("PAUSED", largetext)
        TextRect.center = ((display_width / 2), (display_hieght / 2))
        screen.blit(TextSurf, TextRect)

        # Create buttons for continue, restart, and main menu

        button("CONTINUE", 150, 450, 150, 50, green, bright_green, "unpause")
        button("RESTART", 350, 450, 150, 50, blue, skyblue, "play")
        button("MAIN MENU", 550, 450, 200, 50, red, bright_red, "menu")

        pygame.display.update()
    paused_end_time = pygame.time.get_ticks()
    global timer_break_point
    timer_break_point = timer_break_point + (paused_end_time - paused_start_time)

    pygame.display.update()
    clock.tick(30)


# Making the Unpause Function

def unpaused():
    pygame.mixer.music.pause()
    Sound_crash.play()

    global Pause

    Pause = False


# Making the Background Still when Countdown is On

def countdown_background():
    # Import the necessary modules and set up the game display
    # Initialize the font for displaying text

    pygame.mixer.music.pause()

    font = pygame.font.SysFont(None, 30)

    # Set the initial positions for the game objects
    # (background, strips, car, and text)

    x = (display_width * 0.45)
    y = (display_hieght * 0.8)

    # Draw the background images on the game display

    screen.blit(background, (220, 0))

    # Draw the car on the game display

    screen.blit(carimg, (x, y))

    # Draw the text for the score, highscore, distance and number of dodged cars

    text = font.render("Passed : ", True, green)
    score = font.render("Score : ", True, red)
    high_score = font.render("High Score : ", True, white)
    distance = font.render("Distance : ", True, yellow)
    coins = font.render("Coin Collected: ", True, white)
    screen.blit(text, (20, 60))
    screen.blit(score, (20, 30))
    screen.blit(high_score, (20, 90))
    screen.blit(distance, (20, 120))
    screen.blit(coins, (20, 150))

    # Draw the "PAUSE" and "QUIT" button on the game display

    button("PAUSE", 640, 30, 150, 50, blue, bright_blue, "pause")
    button("QUIT", 660, 540, 100, 50, bright_red, red, "quit")


# Making the Countdown Function

def countdown():
    # Initialize a boolean variable to indicate if countdown is i
    # n progress

    countdown = True

    pygame.mixer.music.pause()
    countdown_beep.play()

    # Continue looping until countdown is complete

    while countdown:

        # Check for events in the pygame event queue

        for event in pygame.event.get():

            # If user closes the game window

            if event.type == pygame.QUIT:
                pygame.quit()  # Quit pygame
                quit()  # Quit the game
                SystemExit()  # Exit the program

        # Fill the game display with a black color

        screen.fill(black)

        # Call a function to display the countdown background

        countdown_background()

        # Display "3" in large font at the center of the screen

        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("3", largetext)
        TextRect.center = ((display_width / 2), (display_hieght / 2))
        screen.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(1)  # Delay for 1 second
        screen.fill(black)

        countdown_background()

        # Display "2" in large font at the center of the screen

        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objectss("2", largetext)
        TextRect.center = ((display_width / 2), (display_hieght / 2))
        screen.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(1)  # Delay for 1 second
        screen.fill(black)

        countdown_background()

        # Display "1" in large font at the center of the screen

        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objectsss("1", largetext)
        TextRect.center = ((display_width / 2), (display_hieght / 2))
        screen.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(1)  # Delay for 1 second
        screen.fill(black)

        countdown_background()

        # Display "GO!!!" in large font at the center of the screen

        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objectssss("GO!!!", largetext)
        TextRect.center = ((display_width / 2), (display_hieght / 2))
        screen.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(1)  # Delay for 1 second

        # Call the game loop function after the countdown is complete

        game_loop()


# Making the Scoring Process

def score_system(passed, score, high_score, distance, coins):
    # Create a font object with size 30

    font = pygame.font.SysFont(None, 30)

    # Render the "Passed" text with passed parameter
    # and color green

    text = font.render("Passed : " + str(passed) + " Cars", True, green)

    # Render the "Score" text with score parameter and color white

    score = font.render("Score : " + str(score), True, red)

    # Render the "Highscore" text with score parameter and color white

    high_score = font.render("High Score : " + str(high_score), True, white)

    # Render the "Distance" text with score parameter and color yellow

    distance = font.render("Distance : " + str(distance) + " m", True, yellow)

    # Render the "Distance" text with score parameter and color yellow

    coins = font.render("Coin Collected: " + str(coins), True, white)

    # Draw the "Passed" text on the game display at (20, 60)
    # coordinates

    screen.blit(text, (20, 60))

    # Draw the "Score" text on the game display at (20,30)
    # coordinates

    screen.blit(score, (20, 30))

    # Draw the "Highscore" text on the game display at (20,90)
    # coordinates

    screen.blit(high_score, (20, 90))

    # Draw the "Distance" text on the game display at (20,120)
    # coordinates

    screen.blit(distance, (20, 120))

    # Draw the "Coins Collected" text on the game display at (20,120)
    # coordinates

    screen.blit(coins, (20, 150))


# Loading the obstacles

def obstacle(obs_startx, obs_starty, obs):
    if obs == 0:
        obs_pic = pygame.image.load("car_1.png")
    elif obs == 1:
        obs_pic = pygame.image.load("car_2.png")
    elif obs == 2:
        obs_pic = pygame.image.load("car_3.png")
    elif obs == 3:
        obs_pic = pygame.image.load("car_4.png")
    elif obs == 4:
        obs_pic = pygame.image.load("car_5.png")
    elif obs == 5:
        obs_pic = pygame.image.load("car_6.png")
    elif obs == 6:
        obs_pic = pygame.image.load("car_7.png")
    elif obs == 7:
        obs_pic = pygame.image.load("car_8.png")
    elif obs == 8:
        obs_pic = pygame.image.load("car_9.png")
    elif obs == 9:
        obs_pic = pygame.image.load("car_10.png")
    elif obs == 10:
        obs_pic = pygame.image.load("car_11.png")
    elif obs == 11:
        obs_pic = pygame.image.load("car_12.png")
    elif obs == 12:
        obs_pic = pygame.image.load("car_13.png")
    elif obs == 13:
        obs_pic = pygame.image.load("car_14.png")
    elif obs == 14:
        obs_pic = pygame.image.load("car_15.png")
    elif obs == 15:
        obs_pic = pygame.image.load("car_16.png")
    elif obs == 16:
        obs_pic = pygame.image.load("car_17.png")
    elif obs == 17:
        obs_pic = pygame.image.load("car_18.png")
    elif obs == 18:
        obs_pic = pygame.image.load("car_19.png")
    elif obs == 19:
        obs_pic = pygame.image.load("car_20.png")
    elif obs == 20:
        obs_pic = pygame.image.load("car_21.png")
    elif obs == 21:
        obs_pic = pygame.image.load("car_22.png")
    elif obs == 22:
        obs_pic = pygame.image.load("car_23.png")
    elif obs == 23:
        obs_pic = pygame.image.load("car_24.png")
    elif obs == 24:
        obs_pic = pygame.image.load("car_25.png")
    elif obs == 25:
        obs_pic = pygame.image.load("car_26.png")
    elif obs == 26:
        obs_pic = pygame.image.load("car_27.png")
    elif obs == 27:
        obs_pic = pygame.image.load("car_28.png")
    elif obs == 28:
        obs_pic = pygame.image.load("car_29.png")
    elif obs == 29:
        obs_pic = pygame.image.load("car_30.png")
    elif obs == 30:
        obs_pic = pygame.image.load("car_31.png")
    elif obs == 31:
        obs_pic = pygame.image.load("car_32.png")
    elif obs == 32:
        obs_pic = pygame.image.load("car_33.png")
    elif obs == 33:
        obs_pic = pygame.image.load("car_34.png")
    elif obs == 34:
        obs_pic = pygame.image.load("car_35.png")
    elif obs == 35:
        obs_pic = pygame.image.load("car_36.png")
    elif obs == 36:
        obs_pic = pygame.image.load("car_37.png")
    elif obs == 37:
        obs_pic = pygame.image.load("car_38.png")
    elif obs == 38:
        obs_pic = pygame.image.load("car_39.png")
    elif obs == 39:
        obs_pic = pygame.image.load("car_40.png")
    elif obs == 40:
        obs_pic = pygame.image.load("car_41.png")

    screen.blit(obs_pic, (obs_startx, obs_starty))


# Making a text Red colour

def text_objects(text, font):
    textsurface = font.render(text, True, bright_red)
    return textsurface, textsurface.get_rect()


# Making a text Black colour

def text_object(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


# Making a text Yellow colour

def text_objectss(text, font):
    textsurface = font.render(text, True, yellow)
    return textsurface, textsurface.get_rect()


# Making a text White colour

def text_objectsss(text, font):
    textsurface = font.render(text, True, white)
    return textsurface, textsurface.get_rect()


# Making a text Green colour

def text_objectssss(text, font):
    textsurface = font.render(text, True, green)
    return textsurface, textsurface.get_rect()


# Displaying a Text

def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 70)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((display_width / 2), (display_hieght / 2))
    screen.blit(textsurf, textrect)

    pygame.display.update()
    time.sleep(3)
    game_loop()


# Making the Crash Function

def crash():
    Sound_crash.stop()
    pygame.mixer.music.pause()
    sound_crash = pygame.mixer.Sound("collision-reverb-103405.mp3")
    sound_crash.play()

    CRASH = True

    while CRASH:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(background, (220, 0))
        screen.blit(Crash, (220, 340))
        largetext = pygame.font.Font('freesansbold.ttf', 70)
        TextSurf, TextRect = text_objects("YOU HAVE CRASHED", largetext)
        TextRect.center = ((display_width / 2), (display_hieght / 3))
        screen.blit(TextSurf, TextRect)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objectsss("YOURS SCORE:" + str(read_score()), mediumtext)
        TextRect.center = ((display_width / 2), (display_hieght / 2))
        screen.blit(TextSurf, TextRect)
        button("RESTART", 150, 450, 150, 50, blue, skyblue, "play")
        button("MAIN MENU", 450, 450, 200, 50, red, bright_red, "menu")

        pygame.display.update()
        clock.tick(30)


# Making of the Car

def car(x, y):
    screen.blit(carimg, (x, y))


# Making the Background

def back_ground():
    screen.blit(background, (220, 0))


# Function for activating the shield

def activate_shield(x, y):
    global shield_active
    shield_active = True


# Function for creating a screen when fuel=0

def fuel_empty():
    Sound_crash.stop()
    pygame.mixer.music.pause()
    sound_crash = pygame.mixer.Sound("collision-reverb-103405.mp3")
    sound_crash.play()

    FUEL_EMPTY = True

    while FUEL_EMPTY:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(background, (220, 0))
        screen.blit(Crash, (220, 340))
        largetext = pygame.font.Font('freesansbold.ttf', 70)
        TextSurf, TextRect = text_objects("OUT OF FUEL", largetext)
        TextRect.center = ((display_width / 2), (display_hieght / 3))
        screen.blit(TextSurf, TextRect)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objectsss("YOURS SCORE:" + str(read_score()), mediumtext)
        TextRect.center = ((display_width / 2), (display_hieght / 2))
        screen.blit(TextSurf, TextRect)
        button("RESTART", 150, 450, 150, 50, blue, skyblue, "play")
        button("MAIN MENU", 450, 450, 200, 50, red, bright_red, "menu")

        pygame.display.update()
        clock.tick(30)


# Making the Main Game

def game_loop():

    global timer_break_point
    timer_break_point = pygame.time.get_ticks()

    pygame.mixer.music.pause()
    Sound_crash.play()

    global Pause
    x = (display_width * 0.45)
    y = (display_hieght * 0.8)
    x_change = 0
    obstacle_speed = 9
    obs = 0

    obs_startx = random.randrange(290, (display_width - 370))
    obs_starty = -750
    obs_width = 45
    obs_hieght = 100
    passed = 0
    level = 0
    score = 0
    distance = 0
    global coin_y, coin_collected
    blink = True
    blink_timer = 0
    blink_interval = 100  # in ms
    shield_duration = 5000  # in ms
    shield_timer = 0

    coin_score = 0

    # ---------- COIN & FUEL INITIAL SETUP + TIMING ----------
    delay_between_coin_and_fuel = 5000  # milliseconds

    coin_x = random.randrange(290, display_width - 370)
    coin_y = -750  # coin starts first

    fuel_x = random.randrange(290, display_width - 370)
    fuel_y = display_hieght + 1000  # start fuel off-screen so it comes later

    coin_width = 50
    coin_height = 50
    coin_speed = 5

    fuel_speed = 5
    fuel_width = 50
    fuel_hieght = 50

    coin_collected = False
    fuel_collected = False

    # record the spawn times so we can enforce 5s gap
    last_coin_spawn_time = pygame.time.get_ticks()
    last_fuel_spawn_time = pygame.time.get_ticks() - delay_between_coin_and_fuel
    # --------------------------------------------------------

    global fuel
    fuel_max = 1000
    fuel = fuel_max

    car_crash = False
    global shield_active

    y2 = 7

    with open("high_score.txt", "r") as ob:
        high_score = int(ob.read())

    run = True

    while run:

        # time (ms) since last frame (from last clock.tick(60))
        dt = clock.get_time()
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = +5
                if event.key == pygame.K_a:
                    obstacle_speed += 2
                if event.key == pygame.K_b:
                    obstacle_speed -= 2
                if event.key == pygame.K_SPACE:
                    activate_shield(x, y)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if x > 512 - car_width or x < 250:
            car_crash = True
            crash()

        x += x_change

        Pause = True
        screen.fill(black)

        rel_y = y2 % background.get_rect().width
        screen.blit(background, (220, rel_y - background.get_rect().width))

        if rel_y < 580:
            screen.blit(background, (220, rel_y))

        y2 += obstacle_speed
        obs_starty -= (obstacle_speed / 4)

        obstacle(obs_startx, obs_starty, obs)

        obs_starty += obstacle_speed

        car(x, y)

        # ------------------- DRAW & MOVE COIN / FUEL -------------------
        screen.blit(coin_img, (coin_x, coin_y))
        coin_y += coin_speed

        screen.blit(fuel_img, (fuel_x, fuel_y))
        fuel_y += fuel_speed
        # ----------------------------------------------------------------

        # Build rects for proper collision
        player_rect = pygame.Rect(x, y, car_width, car_height)
        coin_rect = pygame.Rect(coin_x, coin_y, coin_width, coin_height)
        fuel_rect = pygame.Rect(fuel_x, fuel_y, fuel_width, fuel_hieght)

        # ---------------- COIN COLLISION + RESPAWN TIMING --------------
        if player_rect.colliderect(coin_rect):
            coin_beep.play()
            coin_score += 1
            coin_y = display_hieght + 1000  # move off-screen
            coin_collected = True

        # respawn coin only if enough time since last fuel spawn
        if coin_collected and (current_time - last_fuel_spawn_time >= delay_between_coin_and_fuel):
            coin_x = random.randrange(290, display_width - 370)
            coin_y = -750
            last_coin_spawn_time = current_time
            coin_collected = False

        # if coin goes off-screen without being collected, respawn with delay
        if coin_y > display_hieght and not coin_collected:
            if current_time - last_fuel_spawn_time >= delay_between_coin_and_fuel:
                coin_x = random.randrange(290, display_width - 370)
                coin_y = -750
                last_coin_spawn_time = current_time
        # ----------------------------------------------------------------

        # ---------------- FUEL COLLISION + RESPAWN TIMING --------------
        if player_rect.colliderect(fuel_rect):
            refill_fuel()
            fuel_beep.play()
            fuel_y = display_hieght + 1000  # move off-screen
            fuel_collected = True

        # respawn fuel only if enough time since last coin spawn
        if fuel_collected and (current_time - last_coin_spawn_time >= delay_between_coin_and_fuel):
            fuel_x = random.randrange(290, display_width - 370)
            fuel_y = -750
            last_fuel_spawn_time = current_time
            fuel_collected = False

        # if fuel goes off-screen without being collected, respawn with delay
        if fuel_y > display_hieght and not fuel_collected:
            if current_time - last_coin_spawn_time >= delay_between_coin_and_fuel:
                fuel_x = random.randrange(290, display_width - 370)
                fuel_y = -750
                last_fuel_spawn_time = current_time
        # ----------------------------------------------------------------

        # Decrease fuel over time
        decrease_fuel()

        # Draw the fuel tank bar
        draw_vertical_fuel_tank_bar(fuel)

        # Draw the fuel text
        draw_fuel_text(fuel)

        if x > 505 - car_width or x < 290:
            car_crash = True
            crash()

        if x > display_width - (car_width + 290) or x < 290:
            car_crash = True
            crash()

        if obs_starty > display_hieght:
            obs_starty = 0 - obs_hieght
            obs_startx = random.randrange(290, (display_width - 370))
            obs = random.randrange(0, 41)
            passed = passed + 1
            score = passed * 10
            distance = score * 10

            if int(passed) % 10 == 0:
                level = level + 1
                obstacle_speed += 5
                largetext = pygame.font.Font("freesansbold.ttf", 70)
                textsurf, textrect = text_objects("LEVEL " + str(level), largetext)
                textrect.center = ((display_width / 2), (display_hieght / 2))
                screen.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if y < obs_starty + obs_hieght:
            if not shield_active:
                if (x > obs_startx and x < obs_startx + obs_width) or (x + car_width > obs_startx and x + car_width < obs_startx + obs_width):
                    crash()

        if shield_active:
            font = pygame.font.Font(None, 30)
            text = font.render("Car Shielded ", True, yellow_ochre)
            screen.blit(text, (20, 240))
            shield_img = pygame.image.load("shield.png")
            screen.blit(shield_img, (x - 20, y))
            shield_timer += dt
            if shield_timer >= shield_duration:
                shield_active = False
                shield_timer = 0

        if not car_crash:
            if score > high_score:
                high_score = score
                with open("high_score.txt", "w") as ob:
                    ob.write(str(high_score))

        blink_timer += dt
        if blink_timer >= blink_interval:
            blink = not blink
            blink_timer = 0

        if blink:
            font = pygame.font.Font(None, 30)
            text = font.render("Speed Boosted x " + str(level), True, white)
            screen.blit(text, (20, 210))

        if fuel <= 0:
            fuel_empty()

        score_system(passed, score, high_score, distance, coins=coin_score)
        score_write(Data=str(score))

        button("PAUSE", 640, 30, 150, 50, blue, skyblue, "pause")
        button("QUIT", 660, 540, 100, 50, bright_red, red, "quit")
        timer()
        pygame.display.update()
        clock.tick(60)

intro_loop()
game_loop()
pygame.quit()
quit()