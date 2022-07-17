# Screen size constants
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 640

# default tunable props
## block spawns
BLOCK_SPAWN_MIN_RATE = 40
BLOCK_SPAWN_MAX_RATE = 60

## number of frames thresholds for each level
LEVEL_2 = 600
LEVEL_3 = 1200
LEVEL_4 = 1800

## background speed
ACCELERATION_FRAME_COUNT = 30
ACCELERATION_AMOUNT = -0.1
STARTING_SPEED = -6
MAX_SPEED = -21

## points
MAX_HEALTH = 20
HEALTH_INCREASE = 1
POINTS_PER_BLOCK = 1
LEVEL_1_SLOWDOWN_PER_BLOCK = 0.3
LEVEL_2_SLOWDOWN_PER_BLOCK = 0.2
LEVEL_3_SLOWDOWN_PER_BLOCK = 0.1
LEVEL_4_SLOWDOWN_PER_BLOCK = 0.1

import json
import os

from asset_loader import sibling_path

config_file_path = sibling_path('config.json')
print(config_file_path)
if os.path.exists(config_file_path):
    with open(config_file_path) as j:
        config_data = json.load(j)
        print(config_data)

        if config_data.get('BLOCK_SPAWN_MIN_RATE') is not None:
            BLOCK_SPAWN_MIN_RATE = config_data['BLOCK_SPAWN_MIN_RATE']
        if config_data.get('BLOCK_SPAWN_MAX_RATE') is not None:
            BLOCK_SPAWN_MAX_RATE = config_data['BLOCK_SPAWN_MAX_RATE']
        if config_data.get('LEVEL_2') is not None:
            LEVEL_2 = config_data['LEVEL_2']
        if config_data.get('LEVEL_3') is not None:
            LEVEL_3 = config_data['LEVEL_3']
        if config_data.get('LEVEL_4') is not None:
            LEVEL_4 = config_data['LEVEL_4']
        if config_data.get('ACCELERATION_FRAME_COUNT') is not None:
            ACCELERATION_FRAME_COUNT = config_data['ACCELERATION_FRAME_COUNT']
        if config_data.get('STARTING_SPEED') is not None:
            STARTING_SPEED = config_data['STARTING_SPEED']
        if config_data.get('MAX_SPEED') is not None:
            MAX_SPEED = config_data['MAX_SPEED']
        if config_data.get('ACCELERATION_AMOUNT') is not None:
            ACCELERATION_AMOUNT = config_data['ACCELERATION_AMOUNT']
        if config_data.get('HEALTH_INCREASE') is not None:
            HEALTH_INCREASE = config_data['HEALTH_INCREASE']
        if config_data.get('MAX_HEALTH') is not None:
            MAX_HEALTH = config_data['MAX_HEALTH']
        if config_data.get('POINTS_PER_BLOCK') is not None:
            POINTS_PER_BLOCK = config_data['POINTS_PER_BLOCK']
        if config_data.get('LEVEL_1_SLOWDOWN_PER_BLOCK') is not None:
            LEVEL_1_SLOWDOWN_PER_BLOCK = config_data['LEVEL_1_SLOWDOWN_PER_BLOCK']
        if config_data.get('LEVEL_2_SLOWDOWN_PER_BLOCK') is not None:
            LEVEL_2_SLOWDOWN_PER_BLOCK = config_data['LEVEL_2_SLOWDOWN_PER_BLOCK']
        if config_data.get('LEVEL_3_SLOWDOWN_PER_BLOCK') is not None:
            LEVEL_3_SLOWDOWN_PER_BLOCK = config_data['LEVEL_3_SLOWDOWN_PER_BLOCK']
        if config_data.get('LEVEL_4_SLOWDOWN_PER_BLOCK') is not None:
            LEVEL_4_SLOWDOWN_PER_BLOCK = config_data['LEVEL_4_SLOWDOWN_PER_BLOCK']

print('BLOCK_SPAWN_MIN_RATE', BLOCK_SPAWN_MIN_RATE)
print('BLOCK_SPAWN_MAX_RATE', BLOCK_SPAWN_MAX_RATE)
print('LEVEL_2', LEVEL_2)
print('LEVEL_3', LEVEL_3)
print('LEVEL_4', LEVEL_4)
print('ACCELERATION_FRAME_COUNT', ACCELERATION_FRAME_COUNT)
print('STARTING_SPEED', STARTING_SPEED)
print('MAX_SPEED', MAX_SPEED)
print('ACCELERATION_AMOUNT', ACCELERATION_AMOUNT)
print('MAX_HEALTH', MAX_HEALTH)
print('HEALTH_INCREASE', HEALTH_INCREASE)
print('POINTS_PER_BLOCK', POINTS_PER_BLOCK)
print('LEVEL_1_SLOWDOWN_PER_BLOCK', LEVEL_1_SLOWDOWN_PER_BLOCK)
print('LEVEL_2_SLOWDOWN_PER_BLOCK', LEVEL_2_SLOWDOWN_PER_BLOCK)
print('LEVEL_3_SLOWDOWN_PER_BLOCK', LEVEL_3_SLOWDOWN_PER_BLOCK)
print('LEVEL_4_SLOWDOWN_PER_BLOCK', LEVEL_4_SLOWDOWN_PER_BLOCK)