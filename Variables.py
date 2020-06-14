import os.path


#Varialbles for character movements and Sprites

#Screen Variables
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Sprite animated walking"


SPRITE_PIXEL_SIZE = 128
SPRITE_SCALE = 0.5  # Wall scale
PLAYER_SCALE = 0.5  # Player scale
BOSS_SCALE = 3
BOSS_SCALE_2 = 1
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALE)

# Movement speed of player, in pixels per frame
MOVEMENT_SPEED = 100
MOVEMENT_SPEED_ENEMIE_1 = 3.25
MOVEMENT_SPEED_ENEMIE_2 = 4


UPDATES_PER_FRAME = 8
UPDATES_PER_FRAME_BOSS_2 = 2
UPDATES_PER_FRAME_Main_Char=5
UPDATES_PER_FRAME_Main_Char_Soul=4
UPDATES_PER_FRAME_Enemies=4
GRAVITY = 1.5
MOVEMENT_SPEED = 5
UPDATES_PER_FRAME = 10
GRAVITY = 0.4

PLAYER_JUMP_SPEED = 10

VIEWPORT_MARGIN = SPRITE_PIXEL_SIZE * SPRITE_SCALE
RIGHT_MARGIN = 4 * SPRITE_PIXEL_SIZE * SPRITE_SCALE*2

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1


#Main_Character
Walking_Sprite = "Sprites_clases" + os.path.sep + "Main_character" + os.path.sep + "Sprites" + os.path.sep + "WalkingX.png"
Jumping_Sprite = "Sprites_clases" + os.path.sep + "Main_character" + os.path.sep + "Sprites" + os.path.sep + "JumpingX.png"
Attack_Sprite = "Sprites_clases" + os.path.sep + "Main_character" + os.path.sep + "Sprites" + os.path.sep + "AttackX.png"
Collecting_life_Sprite = "Sprites_clases" + os.path.sep + "Main_character" + os.path.sep + "Sprites" + os.path.sep + "LightingX.png"

# Sprtes "small"
Walking_Sprite1 = "Sprites_clases" + os.path.sep + "Main_character" + os.path.sep + "Sprites" + os.path.sep + "WalkingX1.png"
Jumping_Sprite1 = "Sprites_clases" + os.path.sep + "Main_character" + os.path.sep + "Sprites" + os.path.sep + "JumpingX1.png"
Attack_Sprite1 = "Sprites_clases" + os.path.sep + "Main_character" + os.path.sep + "Sprites" + os.path.sep + "AttackX1.png"


#Enemie_1
Walking_Enemie_1 = "Sprites_clases" + os.path.sep + "Enemie_1" + os.path.sep + "Sprites" + os.path.sep + "Walking0.png"
Lightning_Enemie_1 = "Sprites_clases" + os.path.sep + "Enemie_1" + os.path.sep + "Sprites" + os.path.sep + "Lighting0.png"

#Enemie_1
Walking_Enemie_2 = "Sprites_clases" + os.path.sep + "Enemie_2" + os.path.sep + "Sprites" + os.path.sep + "Walking1.png"
Lightning_Enemie_2 = "Sprites_clases" + os.path.sep + "Enemie_2" + os.path.sep + "Sprites" + os.path.sep + "Lighting1.png"

#Boss_1
Stand_Boss_1="Sprites_clases" + os.path.sep + "Boss_1" + os.path.sep + "Sprites" + os.path.sep + "BOSS0.png"
Attack_Boss_1="Sprites_clases" + os.path.sep + "Boss_1" + os.path.sep + "Sprites" + os.path.sep + "BOSSANIMATION.png"

#Boss_2
Stand_Boss_2="Sprites_clases" + os.path.sep + "Boss_2" + os.path.sep + "Sprites" + os.path.sep + "BOSS1.png"
Attack_Boss_2="Sprites_clases" + os.path.sep + "Boss_2" + os.path.sep + "Sprites" + os.path.sep + "BOSS1attack.png"


#Background Sprites
barra_vida = "Screens" + os.path.sep + "Background_items" + os.path.sep + "barra de vida.png"


#Scenario sprites

#Scenario one
Scenario_1_background_sprite = "Sprites_clases" + os.path.sep + "Scenario" + os.path.sep + "Scenario_one" + os.path.sep + "Sprites" + os.path.sep + "LEVEL1BACK.png"
Scenario_1_foreground1_sprite = "Sprites_clases" + os.path.sep + "Scenario" + os.path.sep + "Scenario_one" + os.path.sep + "Sprites" + os.path.sep + "LEVEL1FRONT.png"
Scenario_1_foreground2_sprite = "Sprites_clases" + os.path.sep + "Scenario" + os.path.sep + "Scenario_one" + os.path.sep + "Sprites" + os.path.sep + "LEVEL1FRONTLIGHTS.png"

#Scenario two
Scenario_2_background_sprite_true = "Sprites_clases" + os.path.sep + "Scenario" + os.path.sep + "Scenario_two" + os.path.sep + "Sprites" + os.path.sep + "LEVEL2BACKTRUE.png"
Scenario_2_foreground_sprite = "Sprites_clases" + os.path.sep + "Scenario" + os.path.sep + "Scenario_two" + os.path.sep + "Sprites" + os.path.sep + "LEVEL2FRONT.png"
Scenario_2_background_sprite_false = "Sprites_clases" + os.path.sep + "Scenario" + os.path.sep + "Scenario_two" + os.path.sep + "Sprites" + os.path.sep + "LEVEL2BACK.png"


# Music
Walk_sound = "Music" + os.path.sep + "StepsC.wav"
Attack_sound = "Music" + os.path.sep + "Golpe1.wav"
Jump_sound = "Music" + os.path.sep + "SaltoC.wav"
light_sound = "Music" + os.path.sep + "Coger luz.wav"
EnemieGenertes_sound = "Music" + os.path.sep + "common_enemy_generation_sound.wav"
Light_sound = "Music" + os.path.sep + "Coger luz.wav"
Ambiente_sound = "Music" + os.path.sep + "AMBIENT.wav"
Tension_sound = "Music" + os.path.sep + "AmbienteTension.wav"
Puzzle_sound = "Music" + os.path.sep + "PuzzlesoundN.wav"