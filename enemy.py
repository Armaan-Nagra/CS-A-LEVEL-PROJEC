import pygame
from settings import *
import random


class enemy(pygame.sprite.Sprite):
    def __init__(self,gx,gy,ghealth,gspritesheet,gstops,gdirection,gspeed,gcooldown,gplayer):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.x = gx
        self.y = gy
        self.health = ghealth
        self.spritesheet = gspritesheet
        self.stops = gstops
        self.direction = gdirection
        self.offscreen = False
        self.last_time = pygame.time.get_ticks()
        self.cooldown = gcooldown
        self.stop1 = None
        self.stop2 = None
        if self.direction == 1:
            self.speed = gspeed
        else:
            self.speed = gspeed * -1
        self.stop1_time = None
        self.stop2_time = None        
        self.player = gplayer
        self.moving = True
        self.stop1_passed = False
        self.stop2_passed = False
        self.rect = self.spritesheet[0].get_rect()
        

    def move(self,gd):
        current_time = pygame.time.get_ticks()
        if self.moving:
            if current_time - self.last_time >= self.cooldown:
                self.frame += 1
                self.last_time = current_time
                if self.frame >= 2:
                    self.frame = 0
            self.x += self.speed 
            self.rect.x = self.x
            self.rect.y = self.y
            if self.direction == 1:
                gd.blit(pygame.transform.flip(self.spritesheet[self.frame],True ,False),(self.x,self.y))
            else:
                gd.blit(pygame.transform.flip(self.spritesheet[self.frame],False,False),(self.x,self.y))


    def shoot(self,gd):
        current_time = pygame.time.get_ticks() #time since the last shot
        if current_time - self.last_time >= self.cooldown: #checks if enough time has passed since last shot
            self.last_time = current_time # last shot updated to current time variable
            gd.blit(self.spritesheet[3],(self.x,self.y)) #animation of player is updated to the 4th one
            self.player.change_health(-0.5) #the health of the player is changed by an amount (-0.5 in this case)

        else: #if enough time has not passed since the last shot
            gd.blit(self.spritesheet[2],(self.x,self.y)) #the 3rd animation is drawn onto the screen

 
    
    def update(self,gd):
        if self.stops == 1:
            self.stop1 = random.randint(100,800)
            self.stops = 0
        if self.stops == 2:
            self.stop1 = random.randint(100,300)
            self.stop2 = random.randint(400,800)
            self.stops = 0
        if self.moving == True:
            self.move(gd)
        self.stop_move(gd)
        self.spawn_back()




        

    def stop_move(self,gd):
        if self.stop2 == None: #if enemy stops once
            #checks if the the enemy is "over" the 1st stop
            if ((self.stop1 - 1) <= self.x and self.x <= (self.stop1 + 1)) and self.stop1_passed == False:
                self.moving = False #enemy stops moving because it will now start shooting
                self.stop1_passed = True #the enemy has passed the first stop

            if self.stop1_passed:
                if self.stop1_time is None:
                    self.stop1_time = pygame.time.get_ticks()  #gets the current time when the enemy stops
                elapsed_time = pygame.time.get_ticks() - self.stop1_time #time since the enemy stopped
                if elapsed_time <= 2500: #if time since enemy stopped is less than 2500 milliseconds
                    self.shoot(gd) #the shoot method is called
                else:
                    self.moving = True #enemy is moving again.
                self.x -= scroll_speed #enemies move at the same rate as the background scroll speed
            
        if self.stop2 != None: #if enemy stops twice
            if ((self.stop1 - 1) <= self.x and self.x <= (self.stop1 + 1)) and self.stop1_passed == False:
                self.moving = False
                self.stop1_passed = True

            if self.stop1_passed:
                if self.stop1_time is None:
                    self.stop1_time = pygame.time.get_ticks()  
                elapsed_time1 = pygame.time.get_ticks() - self.stop1_time
                if elapsed_time1 <= 2500:  
                    self.shoot(gd)
                else:
                    self.moving = True
                    self.stop1_passed = None #variable is set to none so that this conditional statement is not run again.
                self.x -= scroll_speed #asdfasd
                

            #checks if enemy is on the second stop and changes variables appropriately
            if ((self.stop2 - 2) <= self.x and self.x <= (self.stop2 + 2)) and self.stop2_passed == False: 
                self.moving = False
                self.stop2_passed = True

            if self.stop2_passed:
                if self.stop2_time is None:
                    self.stop2_time = pygame.time.get_ticks()  
                elapsed_time2 = pygame.time.get_ticks() - self.stop2_time
                if elapsed_time2 <= 2500: 
                    self.shoot(gd)  
                else:
                    self.moving = True 
                    self.stop2_passed = None
                self.x -= scroll_speed

            

        
    
    def spawn_back(self):
        if self.direction == 1 and self.x>= 1000:
            self.x = random.randint(-500,0)
            self.y = random.randint(250,600)
            self.stops = random.randint(1,2)
            self.stop1_time = None
            self.stop2_time = None 
            self.stop1_passed = False
            self.stop2_passed = False
        if self.direction == 0 and self.x<= -100:
            self.x = random.randint(1000,1500)
            self.y = random.randint(250,600)
            self.stops = random.randint(1,2)
            self.stop1_time = None
            self.stop2_time = None 
            self.stop1_passed = False
            self.stop2_passed = False