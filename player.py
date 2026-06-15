from game_object import GameObject
from collider import Collider
import pygame

class Player:
    """
    Represents the player. Handles WASD inputs.

    Attributes:
        player (GameObject): GameObject representing the player
    """
    player: GameObject

    @staticmethod
    def Set(playerGameObject: GameObject):
        """
        Sets a new GameObject representing a player

        Parameters:
            playerGameObject (GameObject)
        """
        Player.player = playerGameObject

    
    @staticmethod
    def Handle(dt: float):
        """
        Handles WASD input and player behaviour - moving.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            _, Player.player.y = Collider.move(Player.player,0,-300 * dt)
        if keys[pygame.K_s]:
            _, Player.player.y = Collider.move(Player.player,0,300 * dt)
        if keys[pygame.K_a]:
            Player.player.x, _ = Collider.move(Player.player,-300 * dt,0)
        if keys[pygame.K_d]:
            Player.player.x, _ = Collider.move(Player.player,300 * dt,0)