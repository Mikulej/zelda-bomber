from game_object import GameObject
from render import Renderer
import pygame

class Cursor:
    cursor: GameObject
    oldMousePressed = False
    isPressing = False
    startPositionMouse: pygame.Vector2
    endPositionMouse: pygame.Vector2
    cursorSelection: GameObject

    @staticmethod
    def Set(cursorGameObject: GameObject):
        Cursor.cursor = cursorGameObject

    @staticmethod
    def Handle():

        mousePos = pygame.Vector2(pygame.mouse.get_pos())
        mousePressed = pygame.mouse.get_pressed()[0]

        # Render grid cursor
        if mousePos.x >= Renderer.BASE_RESOLUTION_X/2 * Renderer.ratio.x - (Renderer.BASE_RESOLUTION_Y*Renderer.ratio.x/2) and mousePos.x <= Renderer.BASE_RESOLUTION_X/2 * Renderer.ratio.x + (Renderer.BASE_RESOLUTION_Y*Renderer.ratio.x/2) - Cursor.cursor.width * Renderer.ratio.x:
            Cursor.cursor.x, Cursor.cursor.y = int(mousePos.x / Renderer.ratio.x / Cursor.cursor.width) * Cursor.cursor.width, int(mousePos.y / Renderer.ratio.y / Cursor.cursor.height) * Cursor.cursor.height
        
        # OnClick
        if mousePressed and not Cursor.oldMousePressed:
            Cursor.cursorSelection = GameObject(Cursor.cursor.x,Cursor.cursor.y,Cursor.cursor.width,Cursor.cursor.height,pygame.Color(122,25,21))
            Cursor.isPressing = True
            Cursor.startPositionMouse = pygame.Vector2(Cursor.cursor.x,Cursor.cursor.y)
            Cursor.endPositionMouse = pygame.Vector2(Cursor.cursor.x,Cursor.cursor.y)

        # When Holding
        elif mousePressed:
            Cursor.endPositionMouse = pygame.Vector2(Cursor.cursor.x,Cursor.cursor.y)
            Cursor.cursorSelection.width = Cursor.endPositionMouse.x - Cursor.startPositionMouse.x 
            Cursor.cursorSelection.height = Cursor.endPositionMouse.y - Cursor.startPositionMouse.y

        # OnClickRelease
        elif not mousePressed and not Cursor.oldMousePressed and Cursor.isPressing:
            Cursor.isPressing = False
            Cursor.endPositionMouse = pygame.Vector2(Cursor.cursor.x,Cursor.cursor.y)

        Cursor.oldMousePressed = mousePressed
