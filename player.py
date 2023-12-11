import pygame

class player():
    def __init__(self,gscore,ghigh_score,ghealth):
        self.name = ""
        self.score = gscore
        self.high_score = ghigh_score
        self.health = ghealth



    def change_health(self,amount):
        self.health += amount


    def health_bar(self,gd):
        ratio = self.health/100
        pygame.draw.rect(gd, "red", (400,5, 200,50))
        pygame.draw.rect(gd, "green", (400,5, 200 * ratio, 50))

    def change_name(self,name):
        self.name = name


