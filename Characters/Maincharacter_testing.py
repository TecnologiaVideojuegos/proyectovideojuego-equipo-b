from Main_character import Main_character
import sprite_paths
import arcade
from Characters.Main_character.Main_character import Main_Character

SCREEN_TITLE = "Sprite animated walking"
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
SPRITE_PIXEL_SIZE = 128
SPRITE_SCALE = 0.5  # Wall scale
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALE)


class Schenario(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.CADET_GREY)
        self.wall_list = None

    def setup(self):

        self.wall_list = arcade.SpriteList()

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

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()

        distance = self.player.right
        output = f"Distance: {distance}"
        arcade.draw_text(output, self.view_left + 10, self.view_bottom + 20,
                         arcade.color.BLACK, 14)
def main():
    """ Main method """
    window = Schenario(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    window.setup()
    player = Main_Character(sprite_paths.Walking_Sprite,sprite_paths.Jumping_Sprite, sprite_paths.Walk_sound,window.wall_list)
    player.setup()
    arcade.run()
main()