import arcade
from Screens.Variables import *
from Sprites_clases.Scenario.Scenario_one.Scenario_one import *


class GameOver(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.background = None
        self.Image=None
        self.select=False
        # Used for flipping between image sequences
        self.cur_texture = 0

    def setup(self):
        self.background=[]
        self.background.append( arcade.load_texture(Game_over_sprite1) )
        self.background.append(arcade.load_texture(Game_over_sprite2))

    def on_draw(self):
        arcade.start_render()
        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background[self.cur_texture])

    def on_update(self, delta_time: float):
        if random.randint(0,20)==0:
            self.cur_texture += 1

        if self.cur_texture > 1 :
            self.cur_texture = 0


    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.select = True
            self.on_close()
