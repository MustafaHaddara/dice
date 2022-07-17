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

ENEMY_COLOR_LAYER = (128, 0, 0)
def _blend(img: pygame.Surface):
    if img is None:
        return None
    s = img.copy()
    s.fill(ENEMY_COLOR_LAYER, special_flags=pygame.BLEND_MULT)
    return s

ENEMY_IMAGES = [_blend(i) for i in DICE_IMAGES]
