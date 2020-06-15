import arcade
from Screens.Variables import *
from Sprites_clases.Scenario.Scenario_one.Scenario_one import *


class Next_Level_Screen(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.background = None
        self.select=False


    def setup(self):
        self.background= arcade.load_texture(Next_level_Sprite)

    def on_draw(self):
        arcade.start_render()
        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.ENTER:
            self.select = True
            self.close()