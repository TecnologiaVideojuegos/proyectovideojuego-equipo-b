import arcade
from Screens.Variables import *
from Sprites_clases.Scenario.Scenario_one.Scenario_one import *


class Menu(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.background = None
        self.arrow_pos=None
        self.select=False
        self.displayed_tip=-1


    def setup(self):
        self.arrow_pos = 0
        self.background=[]
        self.background.append( arcade.load_texture(Menu_sprite_1) )
        self.background.append(arcade.load_texture(Menu_sprite_2))
        self.background.append(arcade.load_texture(Menu_sprite_3 ))

        self.tips=[]
        self.tips.append(arcade.load_texture(Tip_sprite_1))
        self.tips.append(arcade.load_texture(Tip_sprite_2))
        self.tips.append(arcade.load_texture(Tip_sprite_3))
        self.tips.append(arcade.load_texture(Tip_sprite_4))

    def on_draw(self):
        arcade.start_render()
        # Draw the background texture
        if not self.select:
            arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background[self.arrow_pos])
        if self.select and self.arrow_pos == 1 :
            arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.tips[self.displayed_tip])

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            if not self.select:
                self.arrow_pos -= 1
                if self.arrow_pos < 0:
                    self.arrow_pos = 2


        elif key == arcade.key.DOWN or key == arcade.key.S:
            if not self.select:
                self.arrow_pos += 1
                if self.arrow_pos >= 3:
                    self.arrow_pos = 0


        elif key == arcade.key.ENTER:
            self.select = True
            if self.arrow_pos != 1:
                self.on_close()
            else:
                self.displayed_tip+=1
                if self.displayed_tip == 4:
                    self.displayed_tip = -1
                    self.select = False
                    self.arrow_pos = 0

