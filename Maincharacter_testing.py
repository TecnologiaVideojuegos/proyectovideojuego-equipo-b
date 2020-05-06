# https://stackoverflow.com/questions/59341396/cant-get-attack-animation-to-work-for-arcade-library-with-python
import arcade
from Sprites_clases.Main_character.Main_character import *
from Variables import *


class Schenario(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.background = None
        # Our physics engine
        self.physics_engine = None
        self.game_over = False
        self.player = None
        self.wall_list = None

    def setup(self):
        self.player = Main_Character()
        self.player.setup()

        self.wall_list = arcade.SpriteList()

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
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player.player_sprite, self.wall_list, GRAVITY)
        # Load the background image
        self.background = arcade.load_texture(Schenario_sprite)

    def on_update(self, delta_time):

        self.player.on_update(delta_time)
        self.physics_engine.update()

    def on_draw(self):
        arcade.start_render()
        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        self.wall_list.draw()
        self.player.player_list.draw()




    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP or key == arcade.key.W or key == arcade.key.SPACE:
            self.player.on_key_press_move_up(self.physics_engine)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.on_key_press_move_left()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.on_key_press_move_right()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player.on_key_release_move_left()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.on_key_release_move_right()


def main():
    """ Main method """
    window = Schenario(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


main()
