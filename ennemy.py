from collider import Collider
from game_object import GameObject
import pygame


class Ennemy(Collider):
    """
    An ennemy is a collider that moves on its own towards the player
    
    """

    def __init__(self, x: float, y: float, width: float, height: float, color: pygame.Color = (255,255,255), center: bool = False):
        """
        Create a new ennemy.

        Parameters:
            x (float): X position of rectangle.
            y (float): Y position of rectangle.
            width (float): Width of rectangle.
            height (float): Height of rectangle.
            color (pygame.Color): Color of rectangle.
            center (bool): If True x, y will denote center of a rectangle otherwise they denote upper-left corner.
        """
        super().__init__(x, y, width, height, color)


    def move_toward_player(self, go: GameObject, dt: float):
        """
        Moves the ennemy towards the game object using Collider.move
        """

        if self.x < go.x :
            self.x, _ = Collider.move(self, 300 * dt, 0)
        elif self.x > go.x :
            self.x, _ = Collider.move(self, -300 * dt, 0)
        if self.y < go.y :
            _, self.y = Collider.move(self, 0, 300 * dt)
        elif self.y > go.y :
            _, self.y = Collider.move(self, 0, -300 * dt)