import pygame

BASE_RESOLUTION_X = 1280 
BASE_RESOLUTION_Y = 720

def main():

    print("Hello World!")

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((BASE_RESOLUTION_X, BASE_RESOLUTION_Y))
    print(pygame.display.get_window_size())
    src_width, src_height = pygame.display.get_window_size()

    render_ratio = pygame.Vector2(src_width / BASE_RESOLUTION_X,src_height / BASE_RESOLUTION_Y)

    pygame.display.set_caption("Zelda Bomber")
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2 / render_ratio.x, screen.get_height() / 2 / render_ratio.y)
    player_width = 20*render_ratio.x
    player_height = 20*render_ratio.y

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
            screen = pygame.display.set_mode((1920, 1080))
            src_width, src_height = pygame.display.get_window_size()
            print(pygame.display.get_window_size())
            render_ratio.x = src_width / BASE_RESOLUTION_X
            render_ratio.y = src_height / BASE_RESOLUTION_Y
            player_width = 20*render_ratio.x
            player_height = 20*render_ratio.y
        if keys[pygame.K_q]:
            screen = pygame.display.set_mode((1280, 720))
            src_width, src_height = pygame.display.get_window_size()
            print(pygame.display.get_window_size())
            render_ratio.x = src_width / BASE_RESOLUTION_X
            render_ratio.y = src_height / BASE_RESOLUTION_Y
            player_width = 20*render_ratio.x
            player_height = 20*render_ratio.y
        if keys[pygame.K_r]:
            screen = pygame.display.set_mode((800, 600))
            src_width, src_height = pygame.display.get_window_size()
            print(pygame.display.get_window_size())
            render_ratio.x = src_width / BASE_RESOLUTION_X
            render_ratio.y = src_height / BASE_RESOLUTION_Y
            player_width = 20*render_ratio.x
            player_height = 20*render_ratio.y
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__=="__main__":
    main()

