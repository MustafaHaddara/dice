import random
import os
import sys

# print(os.path.dirname(__file__))
# print(os.listdir(os.path.dirname(__file__)))
# print(os.listdir(os.path.dirname(__file__) + '/assets'))

import pygame
import pygame_menu

from asset_loader import asset_path
from config import SCREEN_HEIGHT, SCREEN_WIDTH, BLOCK_SPAWN_MIN_RATE, BLOCK_SPAWN_MAX_RATE, LEVEL_2, LEVEL_3, LEVEL_4
from gameobjects.background import BACKGROUND_IMAGE, Background
from gameobjects.block import Block
from gameobjects.player import Player
from singletons.level import level_manager
from singletons.score import score_manager
from singletons.speed import speed_manager
 

#Initializing 
pygame.init()
icon = pygame.image.load(asset_path('dice.png'))
pygame.display.set_icon(icon)

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Dice")

NEXT_BLOCK_SPAWN = int( (BLOCK_SPAWN_MIN_RATE + BLOCK_SPAWN_MAX_RATE) / 2 )
LANES = [1,2,3,4,5]

def start_the_game():
    global NEXT_BLOCK_SPAWN

    # reset a bunch of global stuff before we start:
    NEXT_BLOCK_SPAWN = int( (BLOCK_SPAWN_MIN_RATE + BLOCK_SPAWN_MAX_RATE) / 2 )
    level_manager.reset()
    score_manager.reset()
    speed_manager.reset()

    player = Player()
    game_objects = [
        speed_manager,
        level_manager,
        Background([0, 0]),
        Background([0, BACKGROUND_IMAGE.get_height()]),
        Background([0, 2 * BACKGROUND_IMAGE.get_height()]),
        player,
        score_manager,
    ]
    tick = 0
    while player.health>0:
        tick += 1

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)


        # update all objects
        for o in game_objects:
            o.update(events)


        # determines collisions
        for block in game_objects:
            if not isinstance(block, Block):
                continue
            if player.get_rect().colliderect(block.get_rect()):
                player.collision(block)


        # gc
        new_game_objects = []
        for o in game_objects:
            if not o.destroyed:
                new_game_objects.append(o)
        game_objects = new_game_objects


        # spawn new blocks
        if tick == NEXT_BLOCK_SPAWN:
            num_to_spawn = level_manager.current_level()

            random.shuffle(LANES)

            for l in LANES[:num_to_spawn]:
                x = int( (l - 0.5) * 64 - 32)
                game_objects.append(Block([x, SCREEN_HEIGHT]))
            
            NEXT_BLOCK_SPAWN = tick + random.randint(BLOCK_SPAWN_MIN_RATE, BLOCK_SPAWN_MAX_RATE)
            # print(f'tick {tick}, next {NEXT_BLOCK_SPAWN}')

        # render
        for o in game_objects:
            o.render(DISPLAYSURF)
        for o in game_objects:
            o.render_ui(DISPLAYSURF)

        pygame.display.update()
        FramePerSec.tick(FPS)

    menu = pygame_menu.Menu('Game Over', SCREEN_WIDTH, SCREEN_HEIGHT,
                        theme=pygame_menu.themes.THEME_DARK)
    menu.add.label(f'Your score was: {score_manager.score}')

    menu.add.button('Play Again', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(DISPLAYSURF)

if __name__ == '__main__':
    menu = pygame_menu.Menu('Welcome', SCREEN_WIDTH, SCREEN_HEIGHT,
                    theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(DISPLAYSURF)


