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
ACCELERATION_FRAME_COUNT = 300
STARTING_SPEED = -6
ACCELERATION_AMOUNT = -1

## points
POINTS_PER_BLOCK = 1
SLOWDOWN_PER_BLOCK = 0.2

import json
import os

from asset_loader import sibling_path

config_file_path = sibling_path('config.json')
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
        if config_data.get('ACCELERATION_AMOUNT') is not None:
            ACCELERATION_AMOUNT = config_data['ACCELERATION_AMOUNT']
        if config_data.get('POINTS_PER_BLOCK') is not None:
            POINTS_PER_BLOCK = config_data['POINTS_PER_BLOCK']
        if config_data.get('SLOWDOWN_PER_BLOCK') is not None:
            SLOWDOWN_PER_BLOCK = config_data['SLOWDOWN_PER_BLOCK']
