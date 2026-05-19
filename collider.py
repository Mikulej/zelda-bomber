import pygame
from render import Renderer
from game_object import GameObject


class Collider(GameObject):
  collider_id_list = [] 
  
  def __init__(self, x: float, y: float, width: float, height: float, color: pygame.Color = (255,255,255), center: bool = False):
    super().__init__(x, y, width, height, color)
    Collider.collider_id_list.append(self.id)

  def __del__(self):
    super().__del__()
    Collider.collider_id_list.remove(self.id)

  @staticmethod
  def move(go: GameObject,dx: float, dy: float) -> tuple[float, float]:
      skip_id = go.id
      next_pos_x = go.x + dx
      next_pos_y = go.y + dy
      # consider go and GameObjects have it's center at the top left corner
      if dx < 0: #move left
        #check within y-axis bounds
        colliders = [id for id in Collider.collider_id_list if (go.y >= GameObject.game_object_list[id].y and go.y <= (GameObject.game_object_list[id].y + GameObject.game_object_list[id].height)) or ((go.y + go.height) >= GameObject.game_object_list[id].y and (go.y + go.height) <= (GameObject.game_object_list[id].y + GameObject.game_object_list[id].height))]
        # get GameObject that are on right side of go
        colliders = [id for id in colliders if GameObject.game_object_list[id].x + GameObject.game_object_list[id].width <= go.x and id != skip_id] 
        if len(colliders) != 0:
          colliders.sort(key=lambda c: GameObject.game_object_list[c].x,reverse=True)#find closest GameObject to go
          collider: GameObject = GameObject.game_object_list[colliders[0]] # get closest one
          if (go.y >= collider.y and go.y <= (collider.y + collider.height)) or ((go.y + go.height) >= collider.y and (go.y + go.height) <= (collider.y + collider.height)):
            if go.x + dx <= collider.x + collider.width:
              next_pos_x = collider.x + collider.width

      if dx > 0 : # move right
        # check within y-axis bounds
        colliders = [id for id in Collider.collider_id_list if (go.y >= GameObject.game_object_list[id].y and go.y <= (GameObject.game_object_list[id].y + GameObject.game_object_list[id].height)) or ((go.y + go.height) >= GameObject.game_object_list[id].y and (go.y + go.height) <= (GameObject.game_object_list[id].y + GameObject.game_object_list[id].height))]
        # get GameObject that are on left side of go
        colliders = [id for id in colliders if GameObject.game_object_list[id].x >= go.x + go.width and id != skip_id]
        if len(colliders) != 0:
          colliders.sort(key=lambda c: GameObject.game_object_list[c].x,reverse=False)#find closest GameObject to go
          collider: GameObject = GameObject.game_object_list[colliders[0]] # get closest one
          if (go.y >= collider.y and go.y <= (collider.y + collider.height)) or ((go.y + go.height) >= collider.y and (go.y + go.height) <= (collider.y + collider.height)):
            if go.x + go.width + dx >= collider.x:
              next_pos_x = collider.x - go.width

      if dy < 0: # move up
        # check within x-axis bounds
        colliders = [id for id in Collider.collider_id_list if (go.x >= GameObject.game_object_list[id].x and go.x <= (GameObject.game_object_list[id].x + GameObject.game_object_list[id].width)) or ((go.x + go.width) >= GameObject.game_object_list[id].x and (go.x + go.width) <= (GameObject.game_object_list[id].x + GameObject.game_object_list[id].width))]
        # get GameObject that are on top side of go
        colliders = [id for id in colliders if GameObject.game_object_list[id].y + GameObject.game_object_list[id].height <= go.y and id != skip_id] 
        colliders.sort(key=lambda c: GameObject.game_object_list[c].y,reverse=True)#find closest GameObject to go
        if len(colliders) != 0:
          collider: GameObject = GameObject.game_object_list[colliders[0]] # get closest one
          if go.y + dy <= collider.y + collider.height:
            next_pos_y = collider.y + collider.height

      if dy > 0: # move down
        # check within x-axis bounds
        colliders = [id for id in Collider.collider_id_list if (go.x >= GameObject.game_object_list[id].x and go.x <= (GameObject.game_object_list[id].x + GameObject.game_object_list[id].width)) or ((go.x + go.width) >= GameObject.game_object_list[id].x and (go.x + go.width) <= (GameObject.game_object_list[id].x + GameObject.game_object_list[id].width))]
        # get GameObject that are on bottom side of go
        colliders = [id for id in colliders if GameObject.game_object_list[id].y >= go.y + go.height and id != skip_id] 
        colliders.sort(key=lambda c: GameObject.game_object_list[c].y,reverse=False)#find closest GameObject to go
        if len(colliders) != 0:
          collider: GameObject = GameObject.game_object_list[colliders[0]] # get closest one
          if go.y + go.height + dy >= collider.y:
            next_pos_y = collider.y - go.height
        
      return next_pos_x,next_pos_y
  
  @staticmethod
  def serialize_all(gameObjectData: dict) -> dict:
      data: dict = {}
      index = 0
      for id in Collider.collider_id_list:
          for go_index in gameObjectData:
             if gameObjectData[go_index]["id"] == id:
                data[str(index)] = int(go_index)
                break
          index += 1
      return data
  
  @staticmethod
  def deserialize_all(data: dict):
      Collider.collider_id_list = []
      for index in data:
          Collider.collider_id_list.append(data[index])

  @staticmethod
  def destroy_all():
      Collider.collider_id_list = []