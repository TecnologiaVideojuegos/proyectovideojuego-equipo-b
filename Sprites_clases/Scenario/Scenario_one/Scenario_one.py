# https://stackoverflow.com/questions/59341396/cant-get-attack-animation-to-work-for-arcade-library-with-python
import arcade
from Sprites_clases.Main_character.Main_character import *
from Sprites_clases.Enemie_1.Enemie_1 import *
from Variables import *

class Scenario(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.background = None
        # Our physics engine
        self.physics_engine = None

        # Set up the player
        self.player = None
        # Set up the enemies
        self.enemy_1 = None
        self.enemy_2 = None
        # Sprite lists
        self.player_list = None
        self.wall_list = None

        self.jump_needs_reset = False

    def setup(self):
        #Set up the Sprites
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player
        self.player = Main_Character()
        self.player.setup()
        # Set up the player position
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player.scale = PLAYER_SCALE

        self.player_list.append(self.player)

        # Set up the enemy_1                                
        self.enemy_1 = Enemie_1()
        self.enemy_1.setup()

        self.player_list.append(self.enemy_1)

        # -- Set up the walls

        # Create the ground
        for i in range(20):
            wall = arcade.Sprite(":resources:images/tiles/stone.png", SPRITE_SCALE)
            wall.bottom = 0
            wall.center_x = i * GRID_PIXEL_SIZE
            self.wall_list.append(wall)

        # Create the Wall
        for posy in [0, 20]:
            for i in range(10):
                wall = arcade.Sprite(":resources:images/tiles/stone.png", SPRITE_SCALE)
                wall.bottom = 0
                wall.center_y = i * GRID_PIXEL_SIZE
                wall.center_x = posy * GRID_PIXEL_SIZE
                self.wall_list.append(wall)

        # Set the physics_engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_list, self.wall_list, GRAVITY)
        # Load the background image
        self.background = arcade.load_texture(Scenario_sprite)

    def on_update(self, delta_time):
        self.player.is_falling = self.player.change_y < 0
        self.player_list.update_animation()
        self.physics_engine.update()

    def on_draw(self):
        arcade.start_render()
        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.wall_list.draw()
        self.player_list.draw()

    def collision(self):
        pass
        # hit_list = arcade.check_for_collision_with_list(self.player, self.enemie1)
        # for self.enemie1 in hit_list:
            # decrease the character's life
            # if is attacking:
                # kill enemie1

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.SPACE :
            self.player.on_key_press_attack()

        elif key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump() and not self.jump_needs_reset:
                # self.player.is_jumping = True
                self.player.change_y = PLAYER_JUMP_SPEED
                self.jump_needs_reset = False

        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.on_key_press_move_left()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.on_key_press_move_right()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = 0
            self.player.is_walking = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = 0
            self.player.is_walking = False
        elif key == arcade.key.UP or key == arcade.key.W:
            # self.player.is_jumping = False
            # self.player.is_falling = True
            self.jump_needs_reset = False
        elif key == arcade.key.SPACE:
            self.player.is_attacking = False
