import arcade

from Variables import *
from Sprites_clases.Main_character.Main_character import *


class Enemie_2(arcade.Sprite):
    """Inicializador"""

    def __init__(self):

        # Set up parent class
        super().__init__()
        # Sprite lists
        self.enemy2_list = None

        self.id=1
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

        self.is_walking = False
        self.is_attacking = False


    def setup(self):
        self.dead = False
        self.enemy2_list = arcade.SpriteList()
        self.enemy2_sprite = arcade.AnimatedWalkingSprite()

        # Stand Right Sprites
        self.enemy2_sprite.stand_textures = []
        self.enemy2_sprite.stand_textures.append(
            arcade.load_texture(Lightning_Enemie_2, x=0, y=0, width=240, height=520))

        # Stand left Sprites
        self.enemy2_sprite.stand_textures.append(
            arcade.load_texture(Lightning_Enemie_2, x=0, y=0, width=240, height=520, mirrored=True))

        # Walk Right Sprites
        self.enemy2_sprite.walk_textures = []
        texturas = []
        for i in range(7):
            texturas.append(
                arcade.load_texture(Walking_Enemie_2, x=i * 236 + 50, y=0, width=220, height=520))
        self.enemy2_sprite.walk_textures.append(texturas)

        # Walk Left Sprites
        texturas = []
        for i in range(7):
            texturas.append(
                arcade.load_texture(Walking_Enemie_2, x=i * 236 + 50, y=0, width=220, height=520, mirrored=True))
        self.enemy2_sprite.walk_textures.append(texturas)

        # Dead Sprites
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

        self.scale = PLAYER_SCALE


    def Load(self):
        self.dead = False
    def on_draw(self):

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the Sprites.
        self.enemy2_list.draw()

    def on_update(self):

        self.enemy2_list.update()
        self.enemy2_list.update_animation()


    def update_animation(self, delta_time):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Walking animation
        self.cur_texture += 1

        self.texture = self.enemy2_sprite.stand_textures[self.character_face_direction]

        # Dead animation
        if self.dead:
            if self.cur_texture == 90:
                self.kill()
            if self.cur_texture >= 9 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.enemy2_sprite.dead_textures[self.character_face_direction][
                self.cur_texture // UPDATES_PER_FRAME]
        # Walking animation
        elif self.is_walking:
            if self.cur_texture >= 7 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.enemy2_sprite.walk_textures[self.character_face_direction][
                self.cur_texture // UPDATES_PER_FRAME]

    def interact(self,x,y):
        if self.dead:
            self.change_x=0
        else:
            where_x=self.center_x-x
            where_y=self.center_y-y
            if -20 < where_x and where_x< 20 and -5<where_y and where_y<5 :
                self.is_walking = False
                self.is_attacking = True
            elif where_x<0:
                self.is_walking = True
                self.change_x = MOVEMENT_SPEED_ENEMIE_2

            elif where_x>0:
                self.is_walking = True
                self.change_x = -MOVEMENT_SPEED_ENEMIE_2