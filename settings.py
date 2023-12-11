import pygame
pygame.mixer.init()
pygame.font.init()

#load background and music
main_background = pygame.image.load('Stages/Stage 1/monkey.png')
message1 = pygame.image.load('Stages/Stage 2/message1.png')
message2 = pygame.image.load('Stages/Stage 2/message2.png')
background_music = pygame.mixer.Sound("Stages/Stage 1/background.mp3")

#colours
white = (255,255,255)
black =(27,26,26)
yellow = (255,164,0)
dark_green = (12,83,15)
navy_blue = (0,38,114)
red = (212, 0, 0)
orange = (255, 117, 24)

#fonts
arcade_font = pygame.font.Font("Stages/Stage 2/pixel.ttf", 36)
base_font = pygame.font.Font(None,100)
name_score_font = pygame.font.Font(None,50)
leaderboard_font = pygame.font.Font(None,100)
level_font = pygame.font.Font(None,50)

#name
name_placeholder = ''

#creating rectangle
input_rect = pygame.Rect(500,700,140,100)

#check to see if user is inside_box
inside_input_box = False

#gunshot
gunshot_sound = pygame.mixer.Sound("Stages/Stage 5/sounds/uzi-new.mp3")

#bullets
bullets = 100


#uzi
uzi = pygame.image.load('Stages/Stage 5/photos/uzi-new.png')
gunshot_sound = pygame.mixer.Sound("Stages/Stage 5/sounds/uzi-new.mp3")
black_cross = pygame.image.load('Stages/Stage 5/photos/INGAME/black_cross.png')

#grenade
grenade_image = pygame.image.load('Stages/Stage 5/photos/grenade-new.png')
grenade_sound = pygame.mixer.Sound("Stages/Stage 5/sounds/explosion.mp3")
grenade_visual = pygame.image.load('Stages/Stage 5/photos/INGAME/explosion.png')

#level background
background_image = pygame.image.load('Stages/Stage 5/photos/backgroundtest.png')

#scrolling speed of background
scroll_speed = 0.5
background_x = 0

#load soldiers
shooting_soldier = pygame.image.load('Stages/Stage 5/photos/INGAME/shooter.png')
run1 = pygame.image.load('Stages/Stage 5/photos/INGAME/run1.png')
run2 = pygame.image.load('Stages/Stage 5/photos/INGAME/run2.png')
white_shoot = pygame.image.load('Stages/Stage 5/photos/INGAME/white shoot.png')
#load spritesheet
soldier_spritesheet = pygame.image.load("Stages/Stage 5/photos/INGAME/invSpritesheet.png")

max_enemies = 5
enemies_killed = 0


