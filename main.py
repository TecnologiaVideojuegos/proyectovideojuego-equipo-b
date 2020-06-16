import time
from Sprites_clases.Scenario.Scenario_one.Scenario_one import *
from Sprites_clases.Scenario.Scenario_two.Scenario_two import *
from Variables import *

from Screens.Menu.Menu import *
from Screens.GameOver.GameOver import *
from Screens.Next_level_screen.Next_level_screen import *

def main():
    """ Main method """
    quit = False
    window = None
    Scene_one = None
    Scene_two = None
    Game_over = None
    Next_level_screen = None

    window = Menu(SCREEN_WIDTH, SCREEN_HEIGHT, "Menu")
    window.setup()
    arcade.run()

    if window.select and window.arrow_pos == 0:
        if Scene_one == None:
            Scene_one = Scenario_two(SCREEN_WIDTH, SCREEN_HEIGHT, "Level 1")
        Scene_one.setup()
        arcade.run()
        if Scene_one.Game_over:
            if Game_over == None:
                Game_over = GameOver(SCREEN_WIDTH, SCREEN_HEIGHT, "Game over")
            Game_over.setup()
            arcade.run()
        elif Scene_one.Game_won:
            time.sleep(1)
            Next_level_screen = Next_Level_Screen(SCREEN_WIDTH, SCREEN_HEIGHT, "hiting next level")
            Next_level_screen.setup()
            arcade.run()
            if Next_level_screen.select:
                if Scene_two == None:
                    Scene_two = Scenario_two(SCREEN_WIDTH, SCREEN_HEIGHT, "Level 2")
                    Scene_two.setup()
                    arcade.run()
                if Scene_two.Game_over:
                    if Game_over == None:
                        Game_over = GameOver(SCREEN_WIDTH, SCREEN_HEIGHT, "Game over")
                    Game_over.setup()
                    arcade.run()
                else:
                    print("You won")

main()
