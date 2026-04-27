import pygame
from render import Renderer
from game_object import GameObject


class Collider(GameObject):
  collider_id_list = [] 
  
  def __init__(self, x: float, y: float, width: float, height: float, color: pygame.Color = (255,255,255), center: bool = False):
    super().__init__(x, y, width, height)
    Collider.collider_id_list.append(self.id)

  def __del__(self):
    super().__del__()
    Collider.collider_id_list.remove(self.id)

