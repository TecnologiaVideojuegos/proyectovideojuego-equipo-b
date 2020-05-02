import os.path

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Sprite animated walking"
SPRITE_PIXEL_SIZE = 128
SPRITE_SCALE = 0.5  # Wall scale
PLAYER_SCALE = 0.25  # Player scale
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALE)

# Movement speed of player, in pixels per frame
MOVEMENT_SPEED = 3
GRAVITY = 0.98
PLAYER_JUMP_SPEED = 10

VIEWPORT_MARGIN = SPRITE_PIXEL_SIZE * SPRITE_SCALE
RIGHT_MARGIN = 4 * SPRITE_PIXEL_SIZE * SPRITE_SCALE


#Sprites
Walking_Sprite = "Main_character"+os.path.sep + "Sprites" + os.path.sep + "WalkingX.png"
Jumping_Sprite = "Main_character"+os.path.sep + "Sprites" + os.path.sep + "JumpingX.png"
Walk_sound = "Main_character"+os.path.sep + "StepsC.wav"
