import arcade
from Variables import *



class Main_Character():
    """Inicializador"""

    def __init__(self):

        # Sprite lists
        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

        # Default to face-right
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0
        self.attack_texture = 0

        # Track our state
        self.jumping = False
        self.climbing = False
        self.is_on_ladder = False
        self.is_attacking = False

        # Cargar archivo de sonido caminar
        self.caminar = arcade.load_sound(Walk_sound)

        self.RIGHT_FACING = True

    def setup(self):
        "El archivo WalkingX.png lo metí directamente en la carpeta del proyecto de PyCharm"

        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.AnimatedWalkingSprite()

        # Stand Right Sprites
        self.player_sprite.stand_right_textures = []
        self.player_sprite.stand_right_textures.append(
            arcade.load_texture(Walking_Sprite, x=0, y=0, width=240, height=520))

        # Stand left sprites
        self.player_sprite.stand_left_textures = []
        self.player_sprite.stand_left_textures.append(
            arcade.load_texture(Walking_Sprite, x=0, y=0, width=240, height=520, mirrored=True))

        # Jump Right Sprites
        self.player_sprite.walk_upr_textures = []
        for i in range(9):
            self.player_sprite.walk_upr_textures.append(
                arcade.load_texture(Jumping_Sprite, x=i * 236, y=0, width=220, height=522))

        # Jump Left Sprites
        self.player_sprite.walk_upl_textures = []
        for i in range(9):
            self.player_sprite.walk_upl_textures.append(
                arcade.load_texture(Jumping_Sprite, x=i * 236, y=0, width=220, height=522, mirrored=True))

        # Fall Right Sprites
        self.player_sprite.walk_down_textures = []
        for i in range(9):
            self.player_sprite.walk_down_textures.append(
                arcade.load_texture(Jumping_Sprite, x=i * 236, y=0, width=220, height=520))

        # Walk Right Sprites
        self.player_sprite.walk_right_textures = []
        for i in range(7):
            self.player_sprite.walk_right_textures.append(
                arcade.load_texture(Walking_Sprite, x=i * 236 + 50, y=0, width=220, height=522))

        # Walk Left Sprites
        self.player_sprite.walk_left_textures = []
        for i in range(7):
            self.player_sprite.walk_left_textures.append(
                arcade.load_texture(Walking_Sprite, x=i * 236 + 50, y=0, width=220, height=520, mirrored=True))

        #Attack Sprites
        self.player_sprite.attack_textures = []
        for i in range(10):
            self.player_sprite.attack_textures.append(
                arcade.load_texture(Attack_Sprite, x=i * 236 + 50, y=0, width=900, height=600, mirrored=True))



        # Set up the player position

        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = SCREEN_HEIGHT // 2
        self.player_sprite.scale = PLAYER_SCALE

        self.player_list.append(self.player_sprite)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0
        self.game_over = False

    def on_update(self, delta_time):
        self.player_list.update()
        self.player_list.update_animation()

    def on_draw(self):

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_list.draw()

    # on key press
    def on_key_press_move_up(self, physics_engine):
        if physics_engine.can_jump():
            if self.RIGHT_FACING:
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
            else:
                self.player_sprite.change_y = PLAYER_JUMP_SPEED


    def on_key_press_move_left(self):
        self.player_sprite.change_x = -MOVEMENT_SPEED
        arcade.play_sound(self.caminar)
        self.RIGHT_FACING = False

    def on_key_press_move_right(self):
        self.player_sprite.change_x = MOVEMENT_SPEED
        arcade.play_sound(self.caminar)
        self.RIGHT_FACING = True

    #on key release
    def on_key_release_move_left(self):
        self.player_sprite.change_x = 0
        arcade.stop_sound(self.caminar)

    def on_key_release_move_right(self):
        self.player_sprite.change_x = 0
        arcade.stop_sound(self.caminar)

    def on_key_release_attack(self):
        self.is_attacking=True





