import pygame
from asset_loader import asset_path

DICE_IMAGES = [
    None,
    pygame.image.load(asset_path('p1.png')),
    pygame.image.load(asset_path('p2.png')),
    pygame.image.load(asset_path('p3.png')),
    pygame.image.load(asset_path('p4.png')),
    pygame.image.load(asset_path('p5.png')),
    pygame.image.load(asset_path('p6.png')),
]