import arcade
Walking_Sprite="Sprites\WalkingX.png"
Jumping_Sprite="Sprites\JumpingX.png"
Walk_sound="StepsC"

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Sprite animated walking"
SPRITE_PIXEL_SIZE = 128
SPRITE_SCALE = 0.5  # Wall scale
PLAYER_SCALE = 0.25  # Player scale
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALE)

# Movement speed of player, in pixels per frame
MOVEMENT_SPEED = 3
GRAVITY = 0.98
PLAYER_JUMP_SPEED = 10

VIEWPORT_MARGIN = SPRITE_PIXEL_SIZE * SPRITE_SCALE
RIGHT_MARGIN = 4 * SPRITE_PIXEL_SIZE * SPRITE_SCALE


class Main_Character():
    """Inicializador"""

    def __init__(self,Walking_Sprite, Jumping_Sprite, Walk_sound,wall_list):
        self.Walking_Sprite = Walking_Sprite
        self.Jumping_Sprite = Jumping_Sprite

        self.player_list = None

        # variable that holds the player sprite
        self.player = None

        self.wall_list=wall_list
        # Our physics engine
        self.physics_engine = None
        self.game_over = False
        self.view_left = 0
        self.view_bottom = 0
        self.end_of_map = 0

        # Cargar archivo de sonido caminar
        self.caminar = arcade.load_sound(Walk_sound)

    def setup(self):
        "El archivo WalkingX.png lo metí directamente en la carpeta del proyecto de PyCharm"
        self.player_list = arcade.SpriteList()
        self.player = arcade.AnimatedWalkingSprite()

        # Stand Right Sprites
        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(
            arcade.load_texture(self.Walking_Sprite, x=0, y=0, width=240, height=520))

        # Stand left sprites
        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(
            arcade.load_texture(self.Walking_Sprite, x=0, y=0, width=240, height=520, mirrored=True))

        # Jump Sprites
        self.player.walk_up_textures = []
        for i in range(9):
            self.player.walk_up_textures.append(
                arcade.load_texture(self.Jumping_Sprite, x=i * 236, y=0, width=220, height=522))

        # Fall Sprites
        self.player.walk_down_textures = []
        for i in range(9):
            self.player.walk_down_textures.append(
                arcade.load_texture(self.Jumping_Sprite, x=i * 236, y=0, width=220, height=520))

        # Walk Right Sprites
        self.player.walk_right_textures = []
        for i in range(7):
            self.player.walk_right_textures.append(
                arcade.load_texture(self.Walking_Sprite, x=i * 236 + 50, y=0, width=220, height=522))

        # Walk Left Sprites
        self.player.walk_left_textures = []
        for i in range(7):
            self.player.walk_left_textures.append(
                arcade.load_texture(self.Walking_Sprite, x=i * 236 + 50, y=0, width=220, height=520, mirrored=True))

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, self.wall_list, GRAVITY)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player.scale = PLAYER_SCALE

        self.player_list.append(self.player)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0
        self.game_over = False

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()

        # Put the text on the screen.
        # Adjust the text position based on the viewport so that we don't
        # scroll the text too.
        distance = self.player.right
        output = f"Distance: {distance}"
        arcade.draw_text(output, self.view_left + 10, self.view_bottom + 20,
                         arcade.color.BLACK, 14)

    def on_update(self, delta_time):

        self.physics_engine.update()
        self.player_list.update()
        self.player_list.update_animation()

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player.left < left_boundary:
            self.view_left -= left_boundary - self.player.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_MARGIN
        if self.player.right > right_boundary:
            self.view_left += self.player.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player.top > top_boundary:
            self.view_bottom += self.player.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player.bottom
            changed = True

        # If we need to scroll, go ahead and do it.
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = -MOVEMENT_SPEED
            arcade.play_sound(self.caminar)
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = MOVEMENT_SPEED
            arcade.play_sound(self.caminar)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = 0
            arcade.stop_sound(self.caminar)
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = 0
            arcade.stop_sound(self.caminar)


