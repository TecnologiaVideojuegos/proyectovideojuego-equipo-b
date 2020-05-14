from Sprites_clases.Scenario.Scenario_one.Scenario_one import *
from Variables import *

from Screens.Menu.Menu import *


def main():
    """ Main method """
    window = Scenario(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

def prueba():
    window = Menu(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()
main()