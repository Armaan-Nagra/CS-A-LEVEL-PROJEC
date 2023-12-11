import pygame
from settings import *
import json
#from button import *
pygame.init()
def initialise_pygame_display():
    global width, height, clock, gameDisplay # makes variables global so that they can be accessed elsewhere
    pygame.init() #initialises pygame library
    pygame.font.init()
    pygame.mixer.init()# initialises sound
    pygame.display.set_caption("Operation Monkey")
    # below, size of display is set as 2 variables
    width = 1000
    height = 1000
    gameDisplay = pygame.display.set_mode((width, height)) # display is created
    clock = pygame.time.Clock() # variable clock is an object which keeps track of time
    return width, height, gameDisplay, clock

def can_proceed(events):
    if events["space"] == 1:
        return "name"
    else:
        return "start"

def play_music(music):
    if not pygame.mixer.get_busy():
        music.play(-1)


def draw_cover(picture):
    gameDisplay.blit(picture,(0,0))
    
def draw_messages_and_title(gameDisplay):
    gameDisplay.fill(white)
    title = arcade_font.render("OPERATION MONKEY", False, black)
    gameDisplay.blit(title, (width // 2 - title.get_width() // 2, 50))
    gameDisplay.blit(message1, (0,200))
    gameDisplay.blit(message2, (0,425))


def ask_name(gameDisplay):
    global name_placeholder, input_rect, inside_input_box #makes variables global
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                inside_input_box = True # if the user clicks on the input box the variable is set to true
        if event.type == pygame.KEYDOWN:
            if inside_input_box:
                if event.key == pygame.K_BACKSPACE:
                    name_placeholder = name_placeholder[:-1] # if user presses backspace, a letter from name is deleted
                else:
                    name_placeholder += event.unicode # character is added to name variable depending on key pressed
                    
    if inside_input_box:
        colour = red
        outline = 5 # if user clicks on input box it changes colour and outline width
    else:
        colour = black
        outline = 2 # if he does not, it remains the same

    #input box is drawn and text is added to it as the player types in their name
    pygame.draw.rect(gameDisplay,colour,input_rect,outline)
    text_surface = base_font.render(name_placeholder,True, black)
    gameDisplay.blit(text_surface, (input_rect.x + 5, input_rect.y + 8))
    input_rect.w = max(300,text_surface.get_width() + 10) #input box automatically resizes itself
    
    return name_placeholder

def display_text(colour, x, y, message, font):
    message = font.render(message, False, colour)
    gameDisplay.blit(message, (x, y))
    
def load_name_score():
    try:
        with open('name_score.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}



def display_name_score(name):
    file = load_name_score()
    for x in file["users"]:
        if x["username"] == name.upper():
            high_score = x["high_score"]
    display_text(white,15,175,"Name: "+name,name_score_font)
    display_text(white,15,225,"High Score: "+str(high_score),name_score_font)

    
def precedence(first_button,second_button,current):
    if first_button!= current and second_button == current:
        return first_button
    elif second_button!= current and first_button == current:
        return second_button
    else:
        return current

def display_menu_texts():
    gameDisplay.fill(black)
    display_text(white,207,50,"OPERATION MONKEY",arcade_font)
    display_text(red,600,900,"PRESS ESC TO EXIT",pygame.font.Font(None,50))
    
def display_leaderboard():
    gameDisplay.fill(black)
    display_text(yellow, 230,50,"LEADERBOARD",pygame.font.Font("Stages/Stage 2/pixel.ttf", 50))

    positions = calculate_positions() # functions returns the top 3 scores as dictionary objects

    if positions == "invalid":
        display_text(red, 200,400 , "NOT ENOUGH DATA", leaderboard_font)
    else:
        display_text(white, 250, 250, "NAME", leaderboard_font) 
        display_text(white, 750, 250, "SCORE", leaderboard_font)
        for x in range(3): # loops 3 times to display the names and high_scores
            display_text(white, 50, 350+(100*x),(str(x+1)+".       "+ positions[x]["username"]), leaderboard_font)
            display_text(white, 750, 350+(100*x), str(positions[x]["high_score"]), leaderboard_font)
        
        




def calculate_positions():
    data = load_name_score() #loads the JSON file

    #creates placeholders for the top 3 scorers
    first = {
        "username": "player1",
        "high_score": 0
        }
    second = {
        "username": "player2",
        "high_score": 0
        }
    third = {
        "username": "player3",
        "high_score": 0
        }

    #returns "invalid" if there are less than 3 items of data.
    if len(data["users"]) < 3:
        return "invalid"
    
    #logic to check the order of scoring
    for x in data["users"]:
        if x["high_score"] > first["high_score"]: 
            third = second.copy()
            second = first.copy()
            first = x
        elif x["high_score"] > second["high_score"]:
            third = second.copy()
            second = x
        elif x["high_score"] > third["high_score"]:
            third = x

    return first, second, third

def scroll_background(gd):
    global background_x #creates a global variable which contains x co-ordinate of background photo
    background_x -= scroll_speed #the photo moves to the left with "scroll_speed"
    if background_x <= -2000: #if the photo reaches x co-ordinate "-2000", x co-ordinate becomes 0
        background_x = 0 
    #background_image is a variable stored in settings and it's displayed to the screen at x co-ordinate 0 and 2,000
    gd.blit(background_image, (background_x, 0)) 
    gd.blit(background_image, (background_x + 2000, 0))
    
