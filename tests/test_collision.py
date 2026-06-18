import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pygame
from game_object import GameObject
from render import Renderer
from collider import Collider
import random
import time

def main() -> int:

    # pygame setup
    pygame.init()

    pygame.display.set_caption("Zelda Bomber")
    clock = pygame.time.Clock()
    running = True
    dt = 0

    GameObject.initialize()

    Collider(80,0,120,20,"red")
    Collider(80,300,120,20,"red")
    Collider(-20,100,20,120,"red")
    Collider(280,100,20,120,"red")

    Collider(100,100,100,20,"red")
    Collider(80,200,100,20,"red")
    Collider(80,100,20,100,"red")
    Collider(180,120,20,100,"red")

    correctArea = GameObject(100,120,80,80,"green")

    testPlayer = GameObject(150,150,20,20,"blue")

    start_time = time.time()

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        # fill the screen with a color to wipe away anything from last frame
        Renderer.screen.fill("lightblue")

        direction_x = random.randint(-1,1)
        direction_y = random.randint(-1,1)
        ratio_x = random.uniform(0,1)
        ratio_y = 1.0 - ratio_x
        speed = random.uniform(1000,2000)
        testPlayer.x, testPlayer.y = Collider.move(testPlayer,dt*direction_x*speed*ratio_x,dt*direction_y*speed*ratio_y)

        if testPlayer.x + testPlayer.width > correctArea.x + correctArea.width or testPlayer.x < correctArea.x or testPlayer.y < correctArea.y or testPlayer.y + testPlayer.height > correctArea.y + correctArea.height:
            pygame.quit()
            raise Exception("test_collision has failed - out of bounds")

        if time.time() - start_time  >= 10:
            print("test_collision has finished succesfully")
            pygame.quit()
            return 0
        
        GameObject.draw_all()
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__=="__main__":
    main()
