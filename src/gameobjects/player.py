import pygame

from config import SCREEN_HEIGHT, SCREEN_WIDTH
from gameobjects.base import GameObject
from gameobjects.block import Block
from singletons.speed import speed_manager
from sprites.dice import DICE_IMAGES

LANE_WIDTH = DICE_IMAGES[1].get_width()
PLAYER_Y = 75
MAX_HEALTH = 20

class Player(GameObject):
    def __init__(self):
        super().__init__(DICE_IMAGES[1], [0, PLAYER_Y], [0, 0])
        self.face = 1
        # self.lane = 3 # goes from 1 to 5
        self.health = MAX_HEALTH
        self.set_lane(3)
        self.padding = [4,4]

    def render(self, surface):
        super().render(surface)

    def render_ui(self, surface):
        super().render_ui(surface)
        self.draw_healthbar(surface)

    def draw_healthbar(self, surface):
       pygame.draw.rect(surface, (255,0,0), pygame.Rect(0,0,SCREEN_WIDTH,20)) # NEW
       pygame.draw.rect(surface, (0,128,0), pygame.Rect(0,0,self.health*SCREEN_WIDTH/MAX_HEALTH,20)) # NEW

    def update(self, events):
        super().update(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.lane == 1:
                        self.set_lane(5)
                    else:
                        self.set_lane(self.lane-1)

                if event.key == pygame.K_RIGHT:
                    if self.lane == 5:
                        self.set_lane(1)
                    else:
                        self.set_lane(self.lane+1)
                if event.key == pygame.K_1:
                    self.set_face(1)
                if event.key == pygame.K_2:
                    self.set_face(2)
                if event.key == pygame.K_3:
                    self.set_face(3)
                if event.key == pygame.K_4:
                    self.set_face(4)
                if event.key == pygame.K_5:
                    self.set_face(5)
                if event.key == pygame.K_6:
                    self.set_face(6)

    def set_face(self, face_num):
        self.face = face_num
        self.image = DICE_IMAGES[face_num]

    def set_lane(self, lane):
        self.lane = lane
        self.pos[0] = int( (self.lane - 0.5) * LANE_WIDTH - LANE_WIDTH/2)

    def collision(self, block: Block):
        if self.face==block.value:
            speed_manager.adjust_speed(0.2)
        else:
            self.health -= block.value
        block.destroy()
