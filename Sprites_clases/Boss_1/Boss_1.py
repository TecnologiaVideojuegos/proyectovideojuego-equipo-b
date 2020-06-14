import arcade

from Variables import *
from Sprites_clases.Main_character.Main_character import *
import random

class Boss_1(arcade.Sprite):
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
        self.boss1attack_sound = arcade.load_sound(Boss1Attack_sound)

        self.dead = False

        self.boss_1_list = arcade.SpriteList()
        self.boss_1_sprite = arcade.AnimatedWalkingSprite()

        # Stand Right Sprites
        self.boss_1_sprite.stand_textures = []
        self.boss_1_sprite.stand_textures.append(
            arcade.load_texture(Stand_Boss_1, x=0, y=0, width=236, height=298))

        # Stand left Sprites
        self.boss_1_sprite.stand_textures.append(
            arcade.load_texture(Stand_Boss_1, x=0, y=0, width=236, height=298, mirrored=True))

        # Attack Sprites
        self.boss_1_sprite.attack_textures = []
        # Attack Right Sprites
        texturas = []
        for i in range(4):
            texturas.append(
                arcade.load_texture(Attack_Boss_1, x=i * 236, y=0, width=236, height=298))
        self.boss_1_sprite.attack_textures.append(texturas)
        # Attack Left Sprites
        texturas = []
        for i in range(4):
            texturas.append(
                arcade.load_texture(Attack_Boss_1, x=i * 236, y=0, width=236, height=298, mirrored=True))
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

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Standing animation
        self.cur_texture += 1

        self.texture = self.boss_1_sprite.stand_textures[self.character_face_direction]

        if self.dead:
            self.kill()
        elif self.is_attacking:
            if self.cur_texture == 40:
                self.is_attacking = False
            if self.cur_texture >= 4 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.boss_1_sprite.attack_textures[self.character_face_direction][
                self.cur_texture // UPDATES_PER_FRAME]

    def interact(self,x,y):
        if(random.randint(0,200)==0):

            self.is_attacking=True
            arcade.play_sound(self.boss1attack_sound)

        if(random.randint(0,40)==0):
            where_x = self.center_x-x
            MOVE = random.randint(100,500)
            if where_x<0:
                self.is_walking = True
                self.center_x += MOVE

            elif where_x>0:
                self.is_walking = True
                self.center_x -= MOVE

