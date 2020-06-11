import time
from Sprites_clases.Scenario.Scenario_one.Scenario_one import *
from Variables import *

from Screens.Menu.Menu import *


def main():
    """ Main method """


    window = Menu(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

    if window.select and window.arrow_pos == 0:
        Scene_one = Scenario(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        Scene_one.setup()
        arcade.run()


main()