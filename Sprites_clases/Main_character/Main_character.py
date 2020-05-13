import arcade
from Variables import *

class Main_Character(arcade.Sprite):
    """Inicializador"""

    def __init__(self):
        # Set up parent class
        super().__init__()

        # Sprite lists
        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

        # Default to face-right
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0

        # Track our state
        self.is_jumping = False
        self.is_falling = False
        self.is_attacking = False
        self.is_walking = False

        self.jump_needs_reset = False

        # Cargar archivo de sonido caminar
        self.caminar = arcade.load_sound(Walk_sound)

        # Adjust the collision box. Default includes too much empty space
        # side-to-side. Box is centered at sprite center, (0, 0)
        self.points = [[-50, -250], [50, -250], [50, 250], [-50, 250]]

    def setup(self):
        "El archivo WalkingX.png lo metí directamente en la carpeta del proyecto de PyCharm"

        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.AnimatedWalkingSprite()

        # Stand Sprites
        self.player_sprite.stand_textures = []
            # Stand right sprites
        self.player_sprite.stand_textures.append(
            arcade.load_texture(Jumping_Sprite, x=0, y=0, width=240, height=520))
          # Stand left sprites
        self.player_sprite.stand_textures.append(
            arcade.load_texture(Jumping_Sprite, x=0, y=0, width=240, height=520, mirrored=True))

        # Jump Sprites
        self.player_sprite.walk_up_textures = []
        # Jump Right Sprites
        texturas=[]
        for i in range(5):
                texturas.append(
                    arcade.load_texture(Jumping_Sprite, x=i * 236, y=0, width=220, height=522))
        self.player_sprite.walk_up_textures.append(texturas)

        # Jump Left Sprites
        texturas = []
        for i in range(5):
            texturas.append(
                arcade.load_texture(Jumping_Sprite, x=i * 236, y=0, width=220, height=522, mirrored=True))
        self.player_sprite.walk_up_textures.append(texturas)

        # Fall Sprites
        self.player_sprite.walk_down_textures = []
        # Fall Right Sprites
        texturas = []
        for i in range(5,9):
            texturas.append(
                arcade.load_texture(Jumping_Sprite, x=i * 236, y=0, width=220, height=520))
        self.player_sprite.walk_down_textures.append(texturas)
        # Fall Left Sprites
        texturas = []
        for i in range(5,9):
            texturas.append(
                arcade.load_texture(Jumping_Sprite, x=i * 236, y=0, width=220, height=520, mirrored=True))
        self.player_sprite.walk_down_textures.append(texturas)

        # Walk Sprites
        self.player_sprite.walk_textures = []
        # Walk Right Sprites
        texturas = []
        for i in range(7):
            texturas.append(
                arcade.load_texture(Walking_Sprite, x=i * 236 + 50, y=0, width=220, height=522))
        self.player_sprite.walk_textures.append(texturas)

        # Walk Left Sprites
        texturas = []
        for i in range(7):
            texturas.append(
                arcade.load_texture(Walking_Sprite, x=i * 236 + 50, y=0, width=220, height=520, mirrored=True))
        self.player_sprite.walk_textures.append(texturas)

        #Attack Sprites
        self.player_sprite.attack_textures = []
        # Attack Right Sprites
        texturas = []
        for i in range(4 ):
            texturas.append(
                arcade.load_texture(Attack_Sprite, x=i * 1063, y=0, width=1063, height=600))
        self.player_sprite.attack_textures.append(texturas)
        # Attack Left Sprites
        texturas = []
        for i in range(4):
            texturas.append(
                arcade.load_texture(Attack_Sprite, x=i * 1063 , y=0, width=1063, height=600, mirrored=True))
        self.player_sprite.attack_textures.append(texturas)


        self.player_list.append(self.player_sprite)


        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
        self.scale = PLAYER_SCALE

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0
        self.game_over = False

    def update_animation(self, delta_time):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Walking animation
        self.cur_texture += 1

        # Attacking animation
        if self.is_attacking:
            self.set_to_false()
            self.is_attacking=True
            if self.cur_texture >= 4 * UPDATES_PER_FRAME:
                self.cur_texture = 0

            self.texture=self.player_sprite.attack_textures[self.character_face_direction][
                self.cur_texture // UPDATES_PER_FRAME]

        # Jumping animation
        elif self.is_jumping :
            self.set_to_false()
            self.is_jumping = True
            if self.cur_texture >= 5 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.player_sprite.walk_up_textures[self.character_face_direction][
                self.cur_texture // UPDATES_PER_FRAME]

        # Falling animation
        elif self.is_falling:
            if self.cur_texture >= 4 * UPDATES_PER_FRAME:
                self.cur_texture = 0

            self.texture = self.player_sprite.walk_down_textures[self.character_face_direction][
                self.cur_texture // UPDATES_PER_FRAME]

        #Attacking animation
        elif self.is_walking:
            self.set_to_false()
            self.is_walking = True
            if self.cur_texture >= 7 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.player_sprite.walk_textures[self.character_face_direction][
                self.cur_texture // UPDATES_PER_FRAME]
        else:
            self.texture = self.player_sprite.stand_textures[self.character_face_direction]

    # on key press
    def on_key_press_move_up(self, physics_engine):
        print(self.center_y)
        if self.physics_engine.can_jump() and not self.jump_needs_reset:
            self.is_jumping = True
            self.change_y = PLAYER_JUMP_SPEED
            self.jump_needs_reset = True

    def on_key_press_move_left(self):
        if not self.is_attacking:
            self.is_walking = True
            self.change_x = -MOVEMENT_SPEED

    def on_key_press_move_right(self):
        if not self.is_attacking:
            self.is_walking = True
            self.change_x = MOVEMENT_SPEED

    def on_key_press_attack(self):
        if not self.is_walking:
            self.is_attacking = True

    #on key release
    def on_key_release_move_left(self):
       arcade.stop_sound(self.caminar)

    def on_key_release_move_right(self):
        self.change_x = 0


    def on_key_release_attack(self):
        self.is_attacking = False


    def set_to_false(self):
        self.is_jumping = False
        self.is_falling = False
        self.is_attacking = False
        self.is_walking = False