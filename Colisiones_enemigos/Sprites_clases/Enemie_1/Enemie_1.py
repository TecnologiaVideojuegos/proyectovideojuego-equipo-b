import arcade

from Characters.Variables import *

class Enemie_1():
    """Inicializador"""

    def __init__(self,summon_x,summon_y):

        self.summon_x=summon_x
        self.summon_y=summon_y
        # Sprite lists
        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

        # Cargar archivo de sonido caminar
        self.caminar = arcade.load_sound(Walk_sound)

    def setup(self):
        "El archivo WalkingX.png lo metí directamente en la carpeta del proyecto de PyCharm"
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.AnimatedWalkingSprite()

        # Stand Right Sprites
        self.player_sprite.stand_right_textures = []
        self.player_sprite.stand_right_textures.append(
            arcade.load_texture(Walking_Enemie_1, x=0, y=0, width=240, height=520))

        # Stand left sprites
        self.player_sprite.stand_left_textures = []
        self.player_sprite.stand_left_textures.append(
            arcade.load_texture(Walking_Enemie_1, x=0, y=0, width=240, height=520, mirrored=True))

        # Jump Sprites
        self.player_sprite.walk_up_textures = []
        for i in range(9):
            self.player_sprite.walk_up_textures.append(
                arcade.load_texture(Jumping_Sprite, x=i * 236, y=0, width=220, height=522))

        # Fall Sprites
        self.player_sprite.walk_down_textures = []
        for i in range(9):
            self.player_sprite.walk_down_textures.append(
                arcade.load_texture(Jumping_Sprite, x=i * 236, y=0, width=220, height=520))

        # Walk Right Sprites
        self.player_sprite.walk_right_textures = []
        for i in range(7):
            self.player_sprite.walk_right_textures.append(
                arcade.load_texture(Walking_Enemie_1, x=i * 236 + 50, y=0, width=220, height=522))

        # Walk Left Sprites
        self.player_sprite.walk_left_textures = []
        for i in range(7):
            self.player_sprite.walk_left_textures.append(
                arcade.load_texture(Walking_Enemie_1, x=i * 236 + 50, y=0, width=220, height=520, mirrored=True))

        # Set up the player position

        self.player_sprite.center_x = self.summon_x
        self.player_sprite.center_y = self.summon_y
        self.player_sprite.scale = PLAYER_SCALE

        self.player_list.append(self.player_sprite)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.

    def on_draw(self):

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_list.draw()

        # Put the text on the screen.
        # Adjust the text position based on the viewport so that we don't
        # scroll the text too.
    def on_update(self, delta_time):

        self.player_list.update()
        self.player_list.update_animation()

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

    #on key press
    def on_key_press_move_up(self,physics_engine):
        if physics_engine.can_jump():
            self.player_sprite.change_y = PLAYER_JUMP_SPEED
    def on_key_press_move_left(self):
        self.player_sprite.change_x = -MOVEMENT_SPEED
        arcade.play_sound(self.caminar)
    def on_key_press_move_right(self):
        self.player_sprite.change_x = MOVEMENT_SPEED
        arcade.play_sound(self.caminar)

    #on key release
    def on_key_release_move_left(self):
        self.player_sprite.change_x = 0
        arcade.stop_sound(self.caminar)

    def on_key_release_move_right(self):
        self.player_sprite.change_x = 0
        arcade.stop_sound(self.caminar)
