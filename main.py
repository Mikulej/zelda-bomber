import pygame
from game_object import GameObject

BASE_RESOLUTION_X = 1280 
BASE_RESOLUTION_Y = 720

def changeResolution(render_ratio: pygame.Vector2, width: int, height: int):
    pygame.display.set_mode((width, height))
    render_ratio.x = width / BASE_RESOLUTION_X
    render_ratio.y = height / BASE_RESOLUTION_Y

def main():

    print("Hello World!")

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((BASE_RESOLUTION_X, BASE_RESOLUTION_Y))

    render_ratio = pygame.Vector2(1,1)

    pygame.display.set_caption("Zelda Bomber")
    clock = pygame.time.Clock()
    running = True
    dt = 0

    GameObject.initialize()

    player_pos = pygame.Vector2(screen.get_width() / 2 / render_ratio.x, screen.get_height() / 2 / render_ratio.y)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("lightblue")

        # ---- Render ----

       
        pygame.draw.circle(screen, "red", [player_pos.x*render_ratio.x,player_pos.y*render_ratio.y], 40)
        player_width = 20*render_ratio.x
        player_height = 20*render_ratio.y
        pygame.draw.rect(screen,"orange",rect=pygame.Rect(player_pos.x*render_ratio.x -(player_width/2),(player_pos.y*render_ratio.y-(player_height/2)),player_width,player_height))

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
            changeResolution(render_ratio,1920,1080)
        if keys[pygame.K_q]:
            changeResolution(render_ratio,1280,720)
        if keys[pygame.K_r]:
            changeResolution(render_ratio,800,600)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__=="__main__":
    main()

