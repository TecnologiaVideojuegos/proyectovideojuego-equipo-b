import time
from Sprites_clases.Scenario.Scenario_one.Scenario_one import *
from Variables import *

from Screens.Menu.Menu import *


def main():
    """ Main method """
    Playing=True

    window = Menu(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

    if window.arrow_pos==0 :
        Scene_one = Scenario(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        Scene_one.setup()
        arcade.run()
        print("Cargando")



def Prueba():
    fin=True
    window = Menu(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    window.set_visible(False)

    Scene_one = Scenario(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    Scene_one.setup()
    Scene_one.set_visible(False)

    while fin:
        print(1)
        #if(window.al)


main()