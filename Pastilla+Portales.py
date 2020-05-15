import os.path
import arcade
"""MAIN CHARACTER"""
from Sprites_clases.Main_character.Main_character import *
"""VARIABLES"""
from Variables import *


"""SCENARIO"""
class Scenario(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.background = arcade.set_background_color(arcade.color.BLACK)
        # Our physics engine
        self.physics_engine = None

        # Set up the player
        self.player = None

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.pill_list = None
        self.portal_list= None

        self.jump_needs_reset = False

    def setup(self):
        #Set up the Sprites
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.pill_list = arcade.SpriteList()
        self.portal_list = arcade.SpriteList()
        # Set up the player
        self.player = Main_Character()
        self.player.setup()
        # Set up the player position
        self.player.center_x = SCREEN_WIDTH // 4
        self.player.center_y = SCREEN_HEIGHT // 4
        self.player.scale = PLAYER_SCALE

        self.player_list.append(self.player)

        # Create the pill(en este caso una moneda)
        pill = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALE)
        pill.center_x = SCREEN_WIDTH // 2
        pill.center_y = SCREEN_HEIGHT // 8
        pill.scale = 0.5
        self.pill_list.append(pill)

        #Create the portals(en este caso dos puertas)
        for i in range(2):
            portal=arcade.Sprite(":resources:images/tiles/doorClosed_mid.png",SPRITE_SCALE)
            portal.center_x=100+i*1080
            portal.center_y=120
            portal.scale=1
            self.portal_list.append(portal)

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
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, self.wall_list, GRAVITY)
        # Load the background image
        self.background = arcade.load_texture(Scenario_sprite)

    def on_update(self, delta_time):
        self.pill_list.update()
        pill_hit_list = arcade.check_for_collision_with_list(self.player, self.pill_list)
        for pill in pill_hit_list:
            pill.remove_from_sprite_lists()
        self.player.is_falling = self.player.change_y < 0
        self.player_list.update_animation()
        self.physics_engine.update()

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.pill_list.draw()
        if len(self.pill_list) == 0:
            # Draw the background texture
            arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
            self.portal_list.draw()
            self.wall_list.draw()
            self.player_list.draw()

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

def main():
    """ Main method """
    window = Scenario(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

main()

