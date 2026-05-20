from game_object import GameObject
from render import Renderer
import pygame

class Cursor:
    """
    Represents a cursor, that is used for level editor. Handles mouse input.

    Attributes:
        cursor (GameObject): GameObject representing a cursor
        oldMousePressed (tuple): Stores boolean values whether corresponding mouse key was pressed in previous frame
        isPressingLeft (bool): Flag for whether the left mouse button is being pressed in current frame
        startPositionMouse (pygame.Vector2): Start position of an selection
        endPositionMouse (pygame.Vector2): End position of an selection
        cursorSelection (GameObject): GameObject representing a selection
    """
    cursor: GameObject
    oldMousePressed: tuple = (False,False)
    isPressingLeft: bool = False
    startPositionMouse: pygame.Vector2
    endPositionMouse: pygame.Vector2
    cursorSelection: GameObject

    @staticmethod
    def Set(cursorGameObject: GameObject):
        """
        Sets a new GameObject representing a cursor

        Parameters:
            cursorGameObject (GameObject):
        """
        Cursor.cursor = cursorGameObject

    @staticmethod
    def Handle():
        """
        Handles mouse input and cursor behaviour - grid snapping and selection.
        """

        mousePos = pygame.Vector2(pygame.mouse.get_pos())
        leftPressed, _, rightPressed = pygame.mouse.get_pressed()

        # Render grid cursor
        if mousePos.x >= Renderer.BASE_RESOLUTION_X/2 * Renderer.ratio.x - (Renderer.BASE_RESOLUTION_Y*Renderer.ratio.x/2) and mousePos.x <= Renderer.BASE_RESOLUTION_X/2 * Renderer.ratio.x + (Renderer.BASE_RESOLUTION_Y*Renderer.ratio.x/2) - Cursor.cursor.width * Renderer.ratio.x:
            Cursor.cursor.x, Cursor.cursor.y = int(mousePos.x / Renderer.ratio.x / Cursor.cursor.width) * Cursor.cursor.width, int(mousePos.y / Renderer.ratio.y / Cursor.cursor.height) * Cursor.cursor.height
        
        # OnClick
        if leftPressed and not Cursor.oldMousePressed[0]:
            Cursor.cursorSelection = GameObject(Cursor.cursor.x,Cursor.cursor.y,Cursor.cursor.width,Cursor.cursor.height,pygame.Color(122,25,21))
            Cursor.isPressingLeft = True
            Cursor.startPositionMouse = pygame.Vector2(Cursor.cursor.x,Cursor.cursor.y)
            Cursor.endPositionMouse = pygame.Vector2(Cursor.cursor.x,Cursor.cursor.y)

        # When Holding
        elif leftPressed:
            Cursor.endPositionMouse = pygame.Vector2(Cursor.cursor.x,Cursor.cursor.y)
            Cursor.cursorSelection.width = Cursor.endPositionMouse.x - Cursor.startPositionMouse.x 
            Cursor.cursorSelection.height = Cursor.endPositionMouse.y - Cursor.startPositionMouse.y

        # OnClickRelease
        elif not leftPressed and not Cursor.oldMousePressed[0] and Cursor.isPressingLeft:
            Cursor.isPressingLeft = False
            Cursor.endPositionMouse = pygame.Vector2(Cursor.cursor.x,Cursor.cursor.y)

        Cursor.oldMousePressed = (leftPressed,rightPressed)
