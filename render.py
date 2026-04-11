import pygame 

class Renderer():

    BASE_RESOLUTION_X = 1280 
    BASE_RESOLUTION_Y = 720
    
    ratio = pygame.Vector2(1,1)
    screen = pygame.display.set_mode((BASE_RESOLUTION_X, BASE_RESOLUTION_Y))

    @staticmethod
    def changeResolution(width: int, height: int):
        pygame.display.set_mode((width, height))
        Renderer.ratio.x = width / Renderer.BASE_RESOLUTION_X
        Renderer.ratio.y = height / Renderer.BASE_RESOLUTION_Y