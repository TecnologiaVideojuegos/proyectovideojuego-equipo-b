import time
from Sprites_clases.Scenario.Scenario_one.Scenario_one import *
from Sprites_clases.Scenario.Scenario_two.Scenario_two import *
from Variables import *

from Screens.Menu.Menu import *
from Screens.GameOver.GameOver import *

def main():
    """ Main method """
    quit=False
    window = None
    Scene_one = None
    Scene_two = None
    Game_over = None

    window = Menu(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

    if window.select and window.arrow_pos == 0:
        if Scene_one == None:
            Scene_one = Scenario_one(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        Scene_one.setup()
        arcade.run()
        if Scene_one.Game_over:
            if Game_over == None:
                Game_over = GameOver(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
            Game_over.setup()
            arcade.run()

        elif Scene_one.Game_won:
            if Scene_two == None:
                Scene_two = Scenario_two(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
            Scene_two.setup()
            arcade.run()

            if Scene_two.Game_over:
                if Game_over == None:
                    Game_over = GameOver(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
                Game_over.setup()
                arcade.run()

            else:
                print("You won")


main()