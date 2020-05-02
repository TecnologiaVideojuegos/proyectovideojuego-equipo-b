import arcade
from Characters.Main_character.Main_character import *
from Characters.Variables import *

class Schenario(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Our physics engine
        self.physics_engine = None
        self.game_over = False

        self.player=None


        self.wall_list = None

    def setup(self):
        self.player = Main_Character()
        self.player.setup()

        self.wall_list = arcade.SpriteList()

        # -- Set up the walls
        # Create the ground
        for i in range(100):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALE)
            wall.bottom = 0
            wall.center_x = i * GRID_PIXEL_SIZE
            self.wall_list.append(wall)

        # Create a stair
        for row in range(5):
            for column in range(5 - (row + 1)):
                wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALE)
                wall.bottom = GRID_PIXEL_SIZE + row * GRID_PIXEL_SIZE
                wall.center_x = 300 + column * GRID_PIXEL_SIZE
                self.wall_list.append(wall)

        # Create a stair
        for row in range(7):
            for column in range(row, 0, -1):
                wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALE)
                wall.bottom = + column * GRID_PIXEL_SIZE
                wall.center_x = 1280 + row * GRID_PIXEL_SIZE
                self.wall_list.append(wall)

        # Create a stair
        for row in range(7):
            for column in range(7 - (row + 1)):
                wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALE)
                wall.bottom = GRID_PIXEL_SIZE + row * GRID_PIXEL_SIZE
                wall.center_x = 1728 + column * GRID_PIXEL_SIZE
                self.wall_list.append(wall)

        # Create a stair
        for row in range(10):
            for column in range(row, 0, -1):
                wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALE)
                wall.bottom = + column * GRID_PIXEL_SIZE
                wall.center_x = 2520 + row * GRID_PIXEL_SIZE
                self.wall_list.append(wall)

        # Set the physics_engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player.player_sprite, self.wall_list, GRAVITY)

        # Set the background color
        arcade.set_background_color(arcade.color.CADET_GREY)


    def on_update(self, delta_time):


        self.player.on_update(delta_time)

        self.physics_engine.update()

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player.player_list.draw()

        distance = self.player.right
        output = f"Distance: {distance}"
        arcade.draw_text(output, self.view_left + 10, self.view_bottom + 20,
                         arcade.color.BLACK, 14)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP or key == arcade.key.W:
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
    window = Schenario(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    window.setup()
    arcade.run()

main()