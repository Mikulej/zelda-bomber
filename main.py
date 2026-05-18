import pygame
from game_object import GameObject
from render import Renderer
from collider import Collider
from level import Level

def main():

    # pygame setup
    pygame.init()

    pygame.display.set_caption("Zelda Bomber")
    clock = pygame.time.Clock()
    running = True
    dt = 0

    GameObject.initialize()

    # Playable/walkable area
    GameObject(Renderer.BASE_RESOLUTION_X / 2,Renderer.BASE_RESOLUTION_Y / 2,Renderer.BASE_RESOLUTION_Y,Renderer.BASE_RESOLUTION_Y,(255, 197, 104),True)
    
    player = GameObject(Renderer.screen.get_width() / 2 / Renderer.ratio.x, Renderer.screen.get_height() / 2 / Renderer.ratio.y,20,20,"red")

    cursor = GameObject(0,0,20,20, (0,0,0,100))

    GameObject(100,100,50,50)
    GameObject(200,200,50,50,"blue")

    Collider(300,100,50,50,"brown")
    Collider(500,100,50,50,"brown")
    Collider(400,100,50,50,"brown")
    Collider(600,100,50,50,"brown")
    Collider(800,100,50,50,"brown")
    Collider(800,200,50,50,"brown")
    Collider(800,300,50,50,"green")
    Collider(800,350,50,50,"yellow")
    Collider(800,400,50,50,"red")
    Collider(700,300,50,150,"purple")

    oldMousePressed = False
    isPressing = False
    startPositionMouse = 0
    endPositionMouse = 0
    cursorSelection = 0

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        # fill the screen with a color to wipe away anything from last frame
        Renderer.screen.fill("lightblue")

        mouse = pygame.Vector2(pygame.mouse.get_pos())

        # ---- Render ----

        GameObject.draw_all()
        
        # Render grid cursor
        if mouse.x >= Renderer.BASE_RESOLUTION_X/2 * Renderer.ratio.x - (Renderer.BASE_RESOLUTION_Y*Renderer.ratio.x/2) and mouse.x <= Renderer.BASE_RESOLUTION_X/2 * Renderer.ratio.x + (Renderer.BASE_RESOLUTION_Y*Renderer.ratio.x/2) - cursor.width * Renderer.ratio.x:
            cursor.x, cursor.y = int(mouse.x / Renderer.ratio.x / cursor.width) * cursor.width, int(mouse.y / Renderer.ratio.y / cursor.height) * cursor.height

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            Level.save("testSave")
        if keys[pygame.K_t]:
            Level.load("testSave")
            player = GameObject.game_object_list[1]
            cursor = GameObject.game_object_list[2]
        if keys[pygame.K_w]:
            _, player.y = Collider.move(player,0,-300 * dt)
        if keys[pygame.K_s]:
            _, player.y = Collider.move(player,0,300 * dt)
        if keys[pygame.K_a]:
            player.x, _ = Collider.move(player,-300 * dt,0)
        if keys[pygame.K_d]:
            player.x, _ = Collider.move(player,300 * dt,0)
        if keys[pygame.K_1]:
            Renderer.changeResolution(1920,1080)
        if keys[pygame.K_2]:
            Renderer.changeResolution(1280,720)
        if keys[pygame.K_3]:
            Renderer.changeResolution(640,360)

        mousePressed = pygame.mouse.get_pressed()[0]

        # OnClick
        if mousePressed == True and oldMousePressed == False:
            cursorSelection = GameObject(cursor.x,cursor.y,cursor.width,cursor.height,pygame.Color(122,25,21))
            isPressing = True
            startPositionMouse = pygame.Vector2(cursor.x,cursor.y)
            endPositionMouse = pygame.Vector2(cursor.x,cursor.y)

        # When Holding
        elif mousePressed == True:
            endPositionMouse = pygame.Vector2(cursor.x,cursor.y)
            cursorSelection.width = endPositionMouse.x - startPositionMouse.x 
            cursorSelection.height = endPositionMouse.y - startPositionMouse.y

        # OnClickRelease
        elif mousePressed == False and oldMousePressed == False and isPressing:
            isPressing = False
            endPositionMouse = pygame.Vector2(cursor.x,cursor.y)

        oldMousePressed = mousePressed

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__=="__main__":
    main()

