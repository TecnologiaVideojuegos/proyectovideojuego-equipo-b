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
            arcade.load_texture(Walking_Sprite, x=0, y=0, width=240, height=520))
          # Stand left sprites
        self.player_sprite.stand_textures.append(
            arcade.load_texture(Walking_Sprite, x=0, y=0, width=240, height=520, mirrored=True))

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
        # Attack Left Sprites
        texturas = []
        for i in range(10):
            texturas.append(
                arcade.load_texture(Attack_Sprite, x=i * 236 + 50, y=0, width=900, height=600, mirrored=True))
        self.player_sprite.attack_textures.append(texturas)


        self.player_list.append(self.player_sprite)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0
        self.game_over = False

    def update_animation(self, delta_time: float = 1 / 60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.player_sprite.stand_textures[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture +=1


        if self.is_attacking:
            if self.cur_texture >= 10 * UPDATES_PER_FRAME:
                self.cur_texture = 0

            self.texture=self.player_sprite.attack_textures[self.character_face_direction][
                self.cur_texture // UPDATES_PER_FRAME]

        if self.is_jumping :
            if self.cur_texture >= 5 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.player_sprite.walk_up_textures[self.character_face_direction][
                self.cur_texture // UPDATES_PER_FRAME]

        if self.is_falling:
            if self.cur_texture >= 5 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.player_sprite.walk_down_textures[self.character_face_direction][
                (self.cur_texture+4) // UPDATES_PER_FRAME]

        else:
            if self.cur_texture >= 7 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.player_sprite.walk_textures[self.character_face_direction][
                self.cur_texture // UPDATES_PER_FRAME]

    # on key press
    def on_key_press_move_up(self, physics_engine):
        if physics_engine.can_jump():
<<<<<<< HEAD
            self.is_jumping = True
            self.change_y = PLAYER_JUMP_SPEED
=======
            self.player_sprite.change_y = PLAYER_JUMP_SPEED
>>>>>>> 4e6e2c6bbedc8bd5116872c635f88f86c2621c6f

    def on_key_press_move_left(self):
        self.change_x = -MOVEMENT_SPEED
        arcade.play_sound(self.caminar)

    def on_key_press_move_right(self):
        self.change_x = MOVEMENT_SPEED
        arcade.play_sound(self.caminar)

    #on key release
    def on_key_release_move_left(self):
        self.change_x = 0
        arcade.stop_sound(self.caminar)

    def on_key_release_move_right(self):
        self.change_x = 0
        arcade.stop_sound(self.caminar)

    def on_key_release_attack(self):
        self.is_attacking = True
