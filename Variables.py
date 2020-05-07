import os.path

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Sprite animated walking"
SPRITE_PIXEL_SIZE = 128
SPRITE_SCALE = 0.5  # Wall scale
PLAYER_SCALE = 0.25  # Player scale
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALE)

# Movement speed of player, in pixels per frame
MOVEMENT_SPEED = 5
UPDATES_PER_FRAME = 7
GRAVITY = 0.4
PLAYER_JUMP_SPEED = 10

VIEWPORT_MARGIN = SPRITE_PIXEL_SIZE * SPRITE_SCALE
RIGHT_MARGIN = 4 * SPRITE_PIXEL_SIZE * SPRITE_SCALE

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1

#Sprites
#Schenario
Schenario_sprite = "Sprites_clases" + os.path.sep + "Scenario" + os.path.sep + "ESCENARIO1.png"

#Main_Character
Walking_Sprite = "Sprites_clases" + os.path.sep + "Main_character" + os.path.sep + "Sprites" + os.path.sep + "WalkingX.png"
Jumping_Sprite = "Sprites_clases" + os.path.sep + "Main_character" + os.path.sep + "Sprites" + os.path.sep + "JumpingX.png"
Walk_sound = "Sprites_clases" + os.path.sep + "Main_character" + os.path.sep + "StepsC.wav"
Attack_Sprite = "Sprites_clases" + os.path.sep + "Main_character" + os.path.sep + "Sprites" + os.path.sep + "AttackX.png"

#Enemie_1
Walking_Enemie_1 = "Sprites_clases" + os.path.sep + "Enemie_1" + os.path.sep + "Sprites" + os.path.sep + "Walking1.png"
Lightning_Enemie_1 = "Sprites_clases" + os.path.sep + "Enemie_1" + os.path.sep + "Sprites" + os.path.sep + "Lighting1.png"
