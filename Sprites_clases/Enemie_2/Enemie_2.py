import arcade

from Variables import *
from Sprites_clases.Main_character.Main_character import *


class Enemie_2(arcade.Sprite):
    """Inicializador"""

    def __init__(self, summon_x, summon_y):

        # Set up parent class
        super().__init__()

        self.summon_x = summon_x
        self.summon_y = summon_y
        # Sprite lists
        self.enemy2_list = None

        # Set up the player
        self.enemy2_sprite = None
        self.physics_engine = None

        # Used for flipping between image sequences
        self.cur_texture = 0

        # Default to face-right
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0

        ####
        self.position_x = Main_Character.center_x
        self.position_y = Main_Character.center_y

        self.dead = False

    def setup(self):
        "El archivo WalkingX.png lo metí directamente en la carpeta del proyecto de PyCharm"
        self.enemy2_list = arcade.SpriteList()
        self.enemy2_sprite = arcade.AnimatedWalkingSprite()

        # Stand Right Sprites
        self.enemy2_sprite.stand_right_textures = []
        self.enemy2_sprite.stand_right_textures.append(
            arcade.load_texture(Walking_Enemie_2, x=0, y=0, width=240, height=520))

        # Stand left Sprites
        self.enemy2_sprite.stand_left_textures = []
        self.enemy2_sprite.stand_left_textures.append(
            arcade.load_texture(Walking_Enemie_2, x=0, y=0, width=240, height=520, mirrored=True))

        # Walk Right Sprites
        self.enemy2_sprite.walk_right_textures = []
        for i in range(7):
            self.enemy2_sprite.walk_right_textures.append(
                arcade.load_texture(Walking_Enemie_2, x=i * 236 + 50, y=0, width=220, height=522))

        # Walk Left Sprites
        self.enemy2_sprite.walk_left_textures = []
        for i in range(7):
            self.enemy2_sprite.walk_left_textures.append(
                arcade.load_texture(Walking_Enemie_2, x=i * 236 + 50, y=0, width=220, height=520, mirrored=True))

        self.enemy2_list.append(self.enemy2_sprite)

        self.enemy2_sprite.dead_textures = []
        # Dead Right Sprites
        texturas = []
        for i in range(9):
            texturas.append(
                arcade.load_texture(Lightning_Enemie_2, x=i * 236, y=0, width=220, height=520))
        self.enemy2_sprite.dead_textures.append(texturas)
        # Dead Left Sprites
        texturas = []
        for i in range(9):
            texturas.append(
                arcade.load_texture(Lightning_Enemie_2, x=i * 236, y=0, width=220, height=520, mirrored=True))
        self.enemy2_sprite.dead_textures.append(texturas)


        self.enemy2_list.append(self.enemy2_sprite)

        # Set up the player position

        self.center_x = self.summon_x
        self.center_y = self.summon_y
        self.scale = PLAYER_SCALE

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0
        self.game_over = False

    def on_draw(self):

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the Sprites.
        self.enemy2_list.draw()

        # Put the text on the screen.
        # Adjust the text position based on the viewport so that we don't
        # scroll the text too.

    def on_update(self):

        self.enemy2_list.update()
        self.enemy2_list.update_animation()

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

    def update_animation(self, delta_time):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Walking animation
        self.cur_texture += 1

        self.texture = self.enemy2_sprite.stand_right_textures[self.character_face_direction]

        # Dead animation
        if self.dead:
            if self.cur_texture == 90:
                self.kill()
            if self.cur_texture >= 9 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.enemy2_sprite.dead_textures[self.character_face_direction][
                self.cur_texture // UPDATES_PER_FRAME]
