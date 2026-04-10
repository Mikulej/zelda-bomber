import pygame
from render import Renderer

GAME_OBJECT_LIMIT = 100

class GameObject():
    initialized = False
    game_object_list = [] 
    def __init__(self,x: float,y: float , width: float, height: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.id = -1

        if GameObject.initialized == False:
            return

        found = next((go for go in GameObject.game_object_list if go.id == -1), None)
        if found == None:
            print("Game object limit reached")
        else:
            self.id = GameObject.game_object_list.index(found)
            GameObject.game_object_list[self.id] = self

    def __del__(self):
        GameObject.game_object_list[self.id].id = -1

    def initialize():
        for i in range(0,GAME_OBJECT_LIMIT):
            go = GameObject(0,0,0,0)
            go.id = -1
            GameObject.game_object_list.append(go)

        GameObject.initialized = True


    def draw(self):
        pygame.draw.rect(Renderer.screen,"orange",
                         rect=pygame.Rect(self.x*Renderer.ratio.x,
                                          self.y*Renderer.ratio.y,
                                          self.width*Renderer.ratio.x,
                                          self.height*Renderer.ratio.y))

    def draw_all():
        for go in GameObject.game_object_list:
            if go.id != -1:
                go.draw()

