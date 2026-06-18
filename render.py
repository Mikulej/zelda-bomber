import pygame 

class Renderer():
    """
    Stores global values that handle rendering the game.

    Attributes:
        BASE_RESOLUTION_X (int): Base X-axis resolution of a game, used for scaling
        BASE_RESOLUTION_Y (int): Base Y-axis resolution of a game, used for scaling
        ratio (pygame.Vector2): Vector holding width and height scaling values
        screen: Pygame instance of a display
    """

    BASE_RESOLUTION_X: int = 1280 
    BASE_RESOLUTION_Y: int = 720
    
    ratio: pygame.Vector2 = pygame.Vector2(1,1)
    screen = pygame.display.set_mode((BASE_RESOLUTION_X, BASE_RESOLUTION_Y))
    
    @staticmethod
    def changeResolution(width: int, height: int):
        """
        Changes window resolution.

        Parameters:
            width (int):
            height (int):
        """
        pygame.display.set_mode((width, height))
        Renderer.ratio.x = width / Renderer.BASE_RESOLUTION_X
        Renderer.ratio.y = height / Renderer.BASE_RESOLUTION_Y