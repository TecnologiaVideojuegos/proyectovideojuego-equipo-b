import arcade

from Characters.Variables import *

class Main_Character():
    """Inicializador"""

    def __init__(self):

        # Sprite lists
        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

        self.view_left = 0
        self.view_bottom = 0
        self.end_of_map = 0

        # Cargar archivo de sonido caminar
        self.caminar = arcade.load_sound(Walk_sound)

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
                arcade.load_texture(Walking_Sprite, x=i * 236 + 50, y=0, width=220, height=522))

        # Walk Left Sprites
        self.player_sprite.walk_left_textures = []
        for i in range(7):
            self.player_sprite.walk_left_textures.append(
                arcade.load_texture(Walking_Sprite, x=i * 236 + 50, y=0, width=220, height=520, mirrored=True))

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

    def on_draw(self):

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_list.draw()

        # Put the text on the screen.
        # Adjust the text position based on the viewport so that we don't
        # scroll the text too.
        distance = self.player_sprite.right
        output = f"Distance: {distance}"
        arcade.draw_text(output, self.view_left + 10, self.view_bottom + 20,
                         arcade.color.BLACK, 14)

    def on_update(self, delta_time):

        self.player_list.update()
        self.player_list.update_animation()

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # If we need to scroll, go ahead and do it.
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)
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





