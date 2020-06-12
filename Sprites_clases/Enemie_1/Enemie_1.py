import arcade

from Variables import *
from Sprites_clases.Main_character.Main_character import *

class Enemie_1(arcade.Sprite):
    """Inicializador"""

    def __init__(self):

        # Set up parent class
        super().__init__()

        self.summon_x = 100
        self.summon_y = 100
        # Sprite lists
        self.enemy1_list = None

        # Set up the player
        self.enemy1_sprite = None
        self.physics_engine = None

        # Used for flipping between image sequences
        self.cur_texture = 0

        self.id = 0
        # Default to face-right
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0

        ####
        self.position_x = Main_Character.center_x
        self.position_y = Main_Character.center_y

        self.is_walking = False
        self.is_attacking = False


    def setup(self):
        self.dead = False
        self.dead_light = False
        self.enemy1_list = arcade.SpriteList()
        self.enemy1_sprite = arcade.AnimatedWalkingSprite()

        # Stand Right Sprites
        self.enemy1_sprite.stand_textures = []
        self.enemy1_sprite.stand_textures.append(
            arcade.load_texture(Lightning_Enemie_1, x=0, y=0, width=120, height=260))

        # Stand left Sprites
        self.enemy1_sprite.stand_textures.append(
            arcade.load_texture(Lightning_Enemie_1, x=0, y=0, width=120, height=260, mirrored=True))

        # Walk Right Sprites
        self.enemy1_sprite.walk_textures = []
        texturas = []
        for i in range(7):
            texturas.append(
                arcade.load_texture(Walking_Enemie_1, x=i * 118 + 25, y=0, width=110, height=260))
        self.enemy1_sprite.walk_textures.append(texturas)

        # Walk Left Sprites
        texturas = []
        for i in range(7):
            texturas.append(
                arcade.load_texture(Walking_Enemie_1, x=i * 118 + 25, y=0, width=110, height=260, mirrored=True))
        self.enemy1_sprite.walk_textures.append(texturas)


        # Dead Sprites
        self.enemy1_sprite.dead_textures = []
        # Dead Right Sprites
        texturas = []
        for i in range(9):
            texturas.append(
                arcade.load_texture(Lightning_Enemie_1, x=i * 118, y=0, width=110, height=260))
        self.enemy1_sprite.dead_textures.append(texturas)
        # Dead Left Sprites
        texturas = []
        for i in range(9):
            texturas.append(
                arcade.load_texture(Lightning_Enemie_1, x=i * 118, y=0, width=110, height=260, mirrored=True))
        self.enemy1_sprite.dead_textures.append(texturas)

        # Light Sprite
        self.enemy1_sprite.light_textures = []
        # Light Right Sprite
        texturas = []
        for i in range(1):
            texturas.append(
                arcade.load_texture(Lightning_Enemie_1, x=944, y=0, width=110, height=260))
        self.enemy1_sprite.light_textures.append(texturas)
        # Light Left Sprite
        texturas = []
        for i in range(1):
            texturas.append(
                arcade.load_texture(Lightning_Enemie_1, x=944, y=0, width=110, height=260, mirrored=True))
        self.enemy1_sprite.light_textures.append(texturas)


        self.enemy1_list.append(self.enemy1_sprite)
        # Set up the player position

        self.center_x = self.summon_x
        self.center_y = self.summon_y
        self.scale = PLAYER_SCALE

    def Load(self):
        self.dead = False
        self.dead_light = False

    def on_draw(self):

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the Sprites.
        self.enemy1_list.draw()


    def on_update(self):

        self.enemy1_list.update()

        self.enemy1_list.update_animation()


    def update_animation(self, delta_time):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Standing animation
        self.cur_texture += 1

        self.texture = self.enemy1_sprite.stand_textures[self.character_face_direction]

        # Light stand
        if self.dead_light:
            self.texture = self.enemy1_sprite.light_textures[self.character_face_direction]

        # Dead animation
        if self.dead:
            if self.cur_texture == 36:
                self.kill()
            if self.cur_texture >= 9 * UPDATES_PER_FRAME_Enemies:
                self.cur_texture = 0
            self.texture = self.enemy1_sprite.dead_textures[self.character_face_direction][
                self.cur_texture // UPDATES_PER_FRAME_Enemies]
        # Walking animation
        elif self.is_walking:
            if self.cur_texture >= 7 * UPDATES_PER_FRAME_Enemies:
                self.cur_texture = 0
            self.texture = self.enemy1_sprite.walk_textures[self.character_face_direction][
                self.cur_texture // UPDATES_PER_FRAME_Enemies]

        # Light animation
        elif self.dead_light:
            if self.cur_texture >= 1 * UPDATES_PER_FRAME_Enemies:
                self.cur_texture = 0
            self.texture = self.enemy1_sprite.light_textures[self.character_face_direction][
                self.cur_texture // UPDATES_PER_FRAME_Enemies]


    def interact(self, x, y):
        if self.dead_light or self.dead:
            self.change_x = 0
        else:
            where_x = self.center_x-x
            where_y = self.center_y-y
            if -20 < where_x and where_x< 20 and -5<where_y and where_y<5:
                self.is_walking = False
                self.is_attacking = True
            elif where_x < 0:
                self.is_attacking = False
                self.is_walking = True
                self.change_x = MOVEMENT_SPEED_ENEMIE_1

            elif where_x > 0:
                self.is_attacking = False
                self.is_walking = True
                self.change_x = -MOVEMENT_SPEED_ENEMIE_1


