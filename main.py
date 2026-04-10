import pygame
from game_object import GameObject
from render import Renderer


def main():

    print("Hello World!")

    # pygame setup
    pygame.init()

    pygame.display.set_caption("Zelda Bomber")
    clock = pygame.time.Clock()
    running = True
    dt = 0

    GameObject.initialize()

    # Playable/walkable area
    plane = GameObject(Renderer.BASE_RESOLUTION_X / 2,Renderer.BASE_RESOLUTION_Y / 2,Renderer.BASE_RESOLUTION_Y,Renderer.BASE_RESOLUTION_Y,(255, 197, 104),True)
    
    GameObject(100,100,50,50)
    GameObject(200,100,50,50,"blue")

    cursor = GameObject(0,0,20,20, (0,0,0,100))

    player_pos = pygame.Vector2(Renderer.screen.get_width() / 2 / Renderer.ratio.x, Renderer.screen.get_height() / 2 / Renderer.ratio.y)

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
        pygame.draw.circle(Renderer.screen, "red", [player_pos.x*Renderer.ratio.x,player_pos.y*Renderer.ratio.y], 40)
        player_width = 20*Renderer.ratio.x
        player_height = 20*Renderer.ratio.y
        pygame.draw.rect(Renderer.screen,"orange",rect=pygame.Rect(player_pos.x*Renderer.ratio.x -(player_width/2),(player_pos.y*Renderer.ratio.y-(player_height/2)),player_width,player_height))
        
        # Render grid cursor
        if mouse.x >= Renderer.BASE_RESOLUTION_X/2 * Renderer.ratio.x - (Renderer.BASE_RESOLUTION_Y*Renderer.ratio.x/2) and mouse.x <= Renderer.BASE_RESOLUTION_X/2 * Renderer.ratio.x + (Renderer.BASE_RESOLUTION_Y*Renderer.ratio.x/2) - cursor.width * Renderer.ratio.x:
            cursor.x, cursor.y = int(mouse.x / Renderer.ratio.x / cursor.width) * cursor.width, int(mouse.y / Renderer.ratio.y / cursor.height) * cursor.height

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
        if keys[pygame.K_1]:
            Renderer.changeResolution(1920,1080)
        if keys[pygame.K_2]:
            Renderer.changeResolution(1280,720)
        if keys[pygame.K_3]:
            Renderer.changeResolution(640,360)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__=="__main__":
    main()

