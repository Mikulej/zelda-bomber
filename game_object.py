import pygame
from render import Renderer

GAME_OBJECT_LIMIT = 100

class GameObject():
    """
    A visible rectangle on the screen. The most atomic object of a game.

    Must be initialized before being used.

    Attributes:
        initialized (bool): Holds true if class was initialized
        game_object_list (list): List of all GameObject instances
    """
    initialized: bool = False
    game_object_list: list = [] 
    def __init__(self,x: float,y: float , width: float, height: float, color: pygame.Color = (255,255,255), center: bool = False):
        """
        Create a new GameObject.

        Parameters:
            x (float): X position of rectangle.
            y (float): Y position of rectangle.
            width (float): Width of rectangle.
            height (float): Height of rectangle.
            color (pygame.Color): Color of rectangle.
            center (bool): If True x, y will denote center of a rectangle otherwise they denote upper-left corner.
        """
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
        """
        Delete a GameObject.
        
        Marks an object as inactive by setting it's id to -1
        """
        GameObject.game_object_list[self.id].id = -1

    @staticmethod
    def initialize():
        """
        Initialize a GameObject class.

        Sets initialized flag to True
        """
        for i in range(0,GAME_OBJECT_LIMIT):
            go = GameObject(0,0,0,0)
            go.id = -1
            GameObject.game_object_list.append(go)

        GameObject.initialized = True


    def draw(self):
        """
        Draw a recangle using x, y as a upper-left corner.
        """
        pygame.draw.rect(Renderer.screen, self.color,
                         rect=pygame.Rect(self.x*Renderer.ratio.x,
                                          self.y*Renderer.ratio.y,
                                          self.width*Renderer.ratio.x,
                                          self.height*Renderer.ratio.y))
        
    def draw_center(self):
        """
        Draw a recangle using x, y as a center.
        """
        pygame.draw.rect(Renderer.screen, self.color,
                         rect=pygame.Rect(self.x*Renderer.ratio.x - (self.width*Renderer.ratio.x/2),
                                          self.y*Renderer.ratio.y - (self.height*Renderer.ratio.y/2),
                                          self.width*Renderer.ratio.x,
                                          self.height*Renderer.ratio.y))
        
    @staticmethod
    def draw_all():
        """
        Draw all GameObjects in game_object_list that are active.
        """
        for go in GameObject.game_object_list:
            if go.id != -1:
                go.draw_function(go)

    def serialize(self) -> dict:
        """
        Serialize an GameObject to dict.

        Returns:
            dict: Serialized GameObject
        """
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
        """
        Serialize all GameObjects in game_object_list that are active.

        Returns:
            dict: Serialized GameObjects
        """
        data: dict = {}
        index = 0
        for go in GameObject.game_object_list:
            if go.id != -1:
                data[str(index)] = go.serialize()
                index += 1
        return data
    
    @staticmethod
    def deserialize(data: dict):
        """
        Deserialize a single GameObject from dict.
        """
        GameObject(data["x"],data["y"],data["width"],data["height"],data["color"],data["center"])
    
    @staticmethod
    def deserialize_all(data: dict):
        """
        Deserialize multiple GameObjects from dict.
        """
        for index in data:
            GameObject.deserialize(data[index])
            
    @staticmethod
    def destroy_all():
        """
        Destroy all GameObjects in game_object_list by setting their ids to -1.
        """
        for go in GameObject.game_object_list:
            go.id = -1
