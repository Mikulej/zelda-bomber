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
    GameObject(100,100,50,50)

    player_pos = pygame.Vector2(Renderer.screen.get_width() / 2 / Renderer.ratio.x, Renderer.screen.get_height() / 2 / Renderer.ratio.y)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        Renderer.screen.fill("lightblue")

        # ---- Render ----

        GameObject.draw_all()
        pygame.draw.circle(Renderer.screen, "red", [player_pos.x*Renderer.ratio.x,player_pos.y*Renderer.ratio.y], 40)
        player_width = 20*Renderer.ratio.x
        player_height = 20*Renderer.ratio.y
        pygame.draw.rect(Renderer.screen,"orange",rect=pygame.Rect(player_pos.x*Renderer.ratio.x -(player_width/2),(player_pos.y*Renderer.ratio.y-(player_height/2)),player_width,player_height))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
        if keys[pygame.K_e]:
            Renderer.changeResolution(1920,1080)
        if keys[pygame.K_q]:
            Renderer.changeResolution(1280,720)
        if keys[pygame.K_r]:
            Renderer.changeResolution(800,600)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__=="__main__":
    main()

