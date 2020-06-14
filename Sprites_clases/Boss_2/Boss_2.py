import time
from builtins import print

import arcade

from Variables import *
from Sprites_clases.Main_character.Main_character import *
import random

class Boss_2(arcade.Sprite):
    """Inicializador"""

    def __init__(self):

        # Set up parent class
        super().__init__()

        self.center_x = 0
        self.center_y = 0
        # Sprite lists
        self.boss_1_list = None

        # Set up the player
        self.boss_1_sprite = None
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
        self.dead = True
        self.avaible=False



    def setup(self):
        self.dead = False

        self.valor_vida = 50
        self.points = [[-50, -250], [50, -250], [50, 250], [-50, 250]]

        self.boss_1_list = arcade.SpriteList()
        self.boss_1_sprite = arcade.AnimatedWalkingSprite()

        # Stand Right Sprites
        self.boss_1_sprite.stand_textures = []
        self.boss_1_sprite.stand_textures.append(
            arcade.load_texture(Stand_Boss_2, x=0, y=0, width=236, height=298))

        # Stand left Sprites
        self.boss_1_sprite.stand_textures.append(
            arcade.load_texture(Stand_Boss_2, x=0, y=0, width=236, height=298, mirrored=True))

        # Attack Sprites
        self.boss_1_sprite.attack_textures = []
        # Attack Right Sprites
        texturas = []
        for i in range(3):
            texturas.append(
                arcade.load_texture(Attack_Boss_2, x=i * 236, y=0, width=236, height=298))
        self.boss_1_sprite.attack_textures.append(texturas)
        # Attack Left Sprites
        texturas = []
        for i in range(3):
            texturas.append(
                arcade.load_texture(Attack_Boss_2, x=i * 236, y=0, width=236, height=298, mirrored=True))
        self.boss_1_sprite.attack_textures.append(texturas)

        self.boss_1_list.append(self.boss_1_sprite)
        # Set up the player position

        self.scale = PLAYER_SCALE

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0
        self.game_over = False

    def on_draw(self):
        if not self.dead:
            # This command has to happen before we start drawing
            arcade.start_render()

            # Draw all the Sprites.
            self.boss_1_list.draw()


    def on_update(self):

        self.boss_1_list.update()

        self.boss_1_list.update_animation()


    def update_animation(self, delta_time):

        # This boss always look left
        self.character_face_direction = RIGHT_FACING
        # Standing animation
        self.cur_texture += 1

        self.texture = self.boss_1_sprite.stand_textures[self.character_face_direction]

        if self.dead:
            self.texture = self.boss_1_sprite.attack_textures[self.character_face_direction][2]
            time.sleep(0.5)
            self.kill()


        elif self.is_attacking:

            if self.cur_texture == 5:
                self.is_attacking = False

            if self.cur_texture >= 3 * UPDATES_PER_FRAME_BOSS_2:
                self.cur_texture = 0
            self.texture = self.boss_1_sprite.attack_textures[self.character_face_direction][

                self.cur_texture // UPDATES_PER_FRAME_BOSS_2]

    def interact(self, x, y):
        where_x = self.center_x - x
        if abs(where_x) < 300:
            if random.randint(0, 150) == 0:
                self.is_attacking = True



