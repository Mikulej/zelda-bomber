from game_object import GameObject
from collider import Collider
from ennemy import Ennemy
import pygame

class Player:
    """
    Represents the player. Handles WASD inputs.

    Attributes:
        player (GameObject): GameObject representing the player
        ennemy_list (list[Ennemy]): list of ennemies to move with the player
    """
    player: GameObject
    ennemy_list: list[Ennemy]

    @staticmethod
    def Set(playerGameObject: GameObject, enn_list: list[Ennemy]):
        """
        Sets a new GameObject representing a player

        Parameters:
            playerGameObject (GameObject)
            enn_list (list[Ennemy])
        """
        Player.player = playerGameObject
        Player.ennemy_list = enn_list

    
    @staticmethod
    def Handle(dt: float, enn_list: list[Ennemy]):
        """
        Handles WASD input and player behaviour - moving. Moves ennemies. 
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            _, Player.player.y = Collider.move(Player.player,0,-300 * dt)
            for ennemy in Player.ennemy_list:
                ennemy.move_toward_player(Player.player, dt)
        if keys[pygame.K_s]:
            _, Player.player.y = Collider.move(Player.player,0,300 * dt)
            for ennemy in Player.ennemy_list:
                ennemy.move_toward_player(Player.player, dt)
        if keys[pygame.K_a]:
            Player.player.x, _ = Collider.move(Player.player,-300 * dt,0)
            for ennemy in Player.ennemy_list:
                ennemy.move_toward_player(Player.player, dt)
        if keys[pygame.K_d]:
            Player.player.x, _ = Collider.move(Player.player,300 * dt,0)
            for ennemy in Player.ennemy_list:
                ennemy.move_toward_player(Player.player, dt)

        Player.ennemy_list = enn_list