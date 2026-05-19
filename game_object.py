import pygame
from render import Renderer

GAME_OBJECT_LIMIT = 100

class GameObject():
    initialized = False
    game_object_list = [] 
    def __init__(self,x: float,y: float , width: float, height: float, color: pygame.Color = (255,255,255), center: bool = False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.id = -1
        self.color = pygame.Color(color)
        self.draw_function = GameObject.draw

        if GameObject.initialized == False:
            return

        if center:
            self.draw_function = GameObject.draw_center

        found = next((go for go in GameObject.game_object_list if go.id == -1), None)
        if found == None:
            print("Game object limit reached")
        else:
            self.id = GameObject.game_object_list.index(found)
            GameObject.game_object_list[self.id] = self

    def __del__(self):
        GameObject.game_object_list[self.id].id = -1

    @staticmethod
    def initialize():
        for i in range(0,GAME_OBJECT_LIMIT):
            go = GameObject(0,0,0,0)
            go.id = -1
            GameObject.game_object_list.append(go)

        GameObject.initialized = True


    def draw(self):
        pygame.draw.rect(Renderer.screen, self.color,
                         rect=pygame.Rect(self.x*Renderer.ratio.x,
                                          self.y*Renderer.ratio.y,
                                          self.width*Renderer.ratio.x,
                                          self.height*Renderer.ratio.y))
        
    def draw_center(self):
        pygame.draw.rect(Renderer.screen, self.color,
                         rect=pygame.Rect(self.x*Renderer.ratio.x - (self.width*Renderer.ratio.x/2),
                                          self.y*Renderer.ratio.y - (self.height*Renderer.ratio.y/2),
                                          self.width*Renderer.ratio.x,
                                          self.height*Renderer.ratio.y))
        
    @staticmethod
    def draw_all():
        for go in GameObject.game_object_list:
            if go.id != -1:
                go.draw_function(go)

    def serialize(self) -> dict:
        data: dict = {}
        data["x"] = self.x
        data["y"] = self.y
        data["width"] = self.width
        data["height"] = self.height
        data["color"] = (self.color.r,self.color.g,self.color.b)
        data["center"] = False if self.draw_function == GameObject.draw else True
        data["id"] = self.id
        return data
    
    @staticmethod
    def serialize_all() -> dict:
        data: dict = {}
        index = 0
        for go in GameObject.game_object_list:
            if go.id != -1:
                data[str(index)] = go.serialize()
                index += 1
        return data
    
    @staticmethod
    def deserialize(data: dict):
        GameObject(data["x"],data["y"],data["width"],data["height"],data["color"],data["center"])
    
    @staticmethod
    def deserialize_all(data: dict):
        for index in data:
            GameObject.deserialize(data[index])
            
    @staticmethod
    def destroy_all():
        for go in GameObject.game_object_list:
            go.id = -1
