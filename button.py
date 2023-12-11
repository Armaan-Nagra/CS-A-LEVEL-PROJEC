import pygame
from settings import *
from functions import *
import json
class button():
    clicked = False
    def __init__(self, gx,gy,gh,gw,ggd,gbuttoncolour,gcurrent, gdestination, gtext, gfontsize,glettercolour,gevents):
        self.x = gx
        self.y = gy
        self.h = gh
        self.w = gw
        self.gd = ggd
        self.bc = gbuttoncolour
        self.gc = glettercolour
        self.current = gcurrent
        self.dest = gdestination
        self.text = gtext
        self.fs = gfontsize
        self.events = gevents

    def draw(self):
        base_font = pygame.font.Font(None,self.fs)
        button_rect = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.gd, self.bc, button_rect)
        text_surface = base_font.render(self.text, True, self.gc)
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.gd.blit(text_surface, text_rect.topleft)
        
    def update(self):
        self.draw()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.events["left-click"]==1:
            if mouse_x > self.x and mouse_x < self.x + self.w:
                if mouse_y > self.y and mouse_y < self.y + self.h:
                    if self.events["left-click"] == 1:
                        self.clicked = True

    def name(self,name):
        self.update()
        if self.clicked == True:
            if name == '':
                display_text(red, 200, 100, "Enter valid name!", base_font)
                return self.current
            else:
                name_score = load_name_score()
                user_exists = False
                for x in name_score["users"]:
                    if x["username"] == name.upper():
                        user_exists = True
                        return self.dest
                        break

                if not user_exists:
                    new_user = {
                        "username" : name.upper(),
                        "high_score" : 0
                    }
                    name_score["users"].append(new_user)
                    with open("name_score.json","w") as json_file:
                        json.dump(name_score, json_file, indent=4)
                    return self.dest
        else:
            return self.current

    def redirect(self):
        self.update()
        if self.clicked == True:
            return self.dest
        else:
            return self.current

