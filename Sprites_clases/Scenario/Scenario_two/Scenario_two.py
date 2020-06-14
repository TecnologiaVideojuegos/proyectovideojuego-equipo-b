import arcade
from Sprites_clases.Main_character.Main_character import *
from Sprites_clases.Enemie_1.Enemie_1 import *
from Sprites_clases.Enemie_2.Enemie_2 import *
from Sprites_clases.Boss_2.Boss_2 import *
from Variables import *
import time
import random


class Scenario_two(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.background = None
        # Our physics engine
        self.physics_engine = None
        self.physics_engine_enemy01 = None
        self.physics_engine_enemy02 = None
        self.physics_engine_enemy11 = None
        self.physics_engine_enemy22 = None

        # Set up the player
        self.player = None
        # Set up the enemy1
        self.enemy01 = None
        self.enemy02 = None
        self.enemy11 = None
        self.enemy22 = None
        self.boss2 = None
        # Sprite lists
        self.player_list = None
        self.enemy_list = None
        self.wall_list = None
        self.background_items_list = None

        self.lista = None
        self.sol_puzzle1 = None
        self.sol_puzzle2 = None
        self.valor_vida = None

        self.Game_over = False
        self.Game_won = False

        self.view_left = 0
        self.view_bottom = 0
        self.end_of_map = 0

        # Barra vida
        self.life_bar_list = None

        # Phase activation variables
        self.Reached_wall = False
        self.Move_back = False
        self.Summon_Enemies = False
        self.dead_enemie1 = True
        self.dead_enemie2 = True
        self.dead_boss2 = True
        self.Cross_Semaphore = False
        self.Summon_Boss = False
        self.End_level = False
        self.Easter_egg = False

    def setup(self):

        self.lista = []
        self.sol_puzzle1 = [1, 1, 1, 1, 0, 0]
        self.sol_puzzle2 = [0, 1, 0, 1]

        self.valor_vida = 100

        # Set up the Sprites
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.background_items_list = arcade.SpriteList()
        self.life_bar_list = arcade.SpriteList()

        self.enemy11 = Enemie_1()
        self.enemy11.setup()

        self.enemy22 = Enemie_2()
        self.enemy22.setup()

        self.enemy01 = Enemie_1()
        self.enemy01.setup()

        self.enemy02 = Enemie_2()
        self.enemy02.setup()

        self.boss2 = Boss_2()
        self.boss2.setup()

        # Set up the player
        self.player = Main_Character()
        self.player.setup()

        # Set up the player position
        self.player.center_x = 65
        self.player.center_y = 100
        self.player.scale = PLAYER_SCALE

        self.player_list.append(self.player)

        # Barra de vida
        self.life_bar = arcade.Sprite(barra_vida, SPRITE_SCALE)
        self.life_bar_list.append(self.life_bar)

        # -- Set up the walls

        # Create the ground
        for i in range(145):
            wall = arcade.Sprite(":resources:images/tiles/stone.png", SPRITE_SCALE)
            wall.bottom = 10
            wall.type = "ground"
            wall.center_x = i * GRID_PIXEL_SIZE
            self.wall_list.append(wall)

        # Create the Wall
        for posy in [(0, "wall"), (4300, "Sema"), (7400, "Boss"), (8000, "wall")]:
            for i in range(10):
                wall = arcade.Sprite(":resources:images/tiles/stone.png", SPRITE_SCALE)
                wall.bottom = 0
                wall.type = posy[1]
                wall.center_y = i * GRID_PIXEL_SIZE
                wall.center_x = posy[0]
                self.wall_list.append(wall)

        # Set the physics_engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, self.wall_list, gravity_constant=GRAVITY)

        # Load the background image
        self.background_true = arcade.load_texture(Scenario_2_background_sprite_true)
        self.background_false = arcade.load_texture(Scenario_2_background_sprite_false)
        self.foreground = arcade.load_texture(Scenario_2_foreground_sprite)

    def on_update(self, delta_time):
        try:
            if self.valor_vida <= 0:
                self.Game_over = True
                self.close()
            else:

                self.player.is_falling = self.player.change_y < 0
                self.player_list.update_animation()

                self.physics_engine.update()

                if self.End_level:
                    if self.player.center_x > 7900:
                        self.Game_won = True
                        self.close()
                elif self.Easter_egg:
                    self.Game_won = True
                    self.delete_boss_wall()
                    if self.player.center_x > 7900:
                        self.close()
                elif self.Summon_Boss:
                    self.Cross_Semaphore = False
                    self.Summon_Enemie()
                elif self.Cross_Semaphore:
                    self.Summon_Enemies = False
                    self.Summon_Boss = self.player.center_x > 5000
                elif self.Summon_Enemies:
                    self.Reached_wall = False
                    self.Summon_Enemie()
                elif self.Reached_wall and self.player.center_x < 4000:
                    self.Summon_Enemies = True
                    self.player.center_x = 2134
                elif self.player.center_x > 4000:
                    self.Reached_wall = True
                # print(self.player.center_x)"""

                if (len(self.enemy_list) > 0):
                    self.enemy_list.update_animation()
                    if self.physics_engine_enemy01 != None:
                        self.physics_engine_enemy01.update()
                    if self.physics_engine_enemy02 != None:
                        self.physics_engine_enemy02.update()
                    if self.physics_engine_enemy11 != None:
                        self.physics_engine_enemy11.update()
                    if self.physics_engine_enemy22 != None:
                        self.physics_engine_enemy22.update()
                    self.Trigger_IA()
                    self.collisions()
                    if self.boss2.valor_vida <= 0:
                        self.Level_Pased()
                        self.Summon_Boss=False
                        self.Easter_egg =True
                # print(self.player.center_x)

                # --- Manage Scrolling ---

                # Track if we need to change the viewport

                changed = False

                # Scroll left
                left_boundary = self.view_left + SCREEN_WIDTH - RIGHT_MARGIN * 1.5
                if self.player.left < left_boundary:
                    self.view_left -= left_boundary - self.player.left
                    changed = True

                # Scroll right
                right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_MARGIN
                if self.player.right > right_boundary:
                    self.view_left += self.player.right - right_boundary
                    changed = True

                # Scroll up
                top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
                if self.player.top > top_boundary:
                    self.view_bottom += self.player.top - top_boundary
                    changed = True

                # Scroll down
                bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
                if self.player.bottom < bottom_boundary:
                    self.view_bottom -= bottom_boundary - self.player.bottom
                    changed = True

                # If we need to scroll, go ahead and do it.
                if changed:
                    arcade.set_viewport(self.view_left,
                                        SCREEN_WIDTH + self.view_left,
                                        self.view_bottom,
                                        SCREEN_HEIGHT + self.view_bottom)
        except:
            None


    def on_draw(self):
        try:
            arcade.start_render()
            # Draw the background texture
            if self.Easter_egg:
                arcade.draw_lrwh_rectangle_textured(-700, 10, 9200, SCREEN_HEIGHT,
                                                self.background_true)  # At wall ground length 20 the width is 1280
            else:
                arcade.draw_lrwh_rectangle_textured(-700, 10, 9200, SCREEN_HEIGHT,
                                                    self.background_false)
            # self.wall_list.draw()                                                                   #At wall ground lenght 100 the image witdh is 6450
            self.background_items_list.draw()
            self.player_list.draw()
            self.enemy_list.draw()
            arcade.draw_lrwh_rectangle_textured(-700, 10, 9200, SCREEN_HEIGHT,
                                                self.foreground)
            self.GUI()
            if len(self.lista) > 0:
                score_text = ""
                for i in self.lista:
                    score_text += "%d " % (i)
                arcade.draw_text(score_text, self.view_left + 50, self.view_bottom + 650,
                                 arcade.csscolor.WHITE, 18)
        except:
            None

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.SPACE:
            self.player.on_key_press_attack()

        elif key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump() and not self.player.jump_needs_reset:
                self.player.is_jumping = True
                self.player.change_y = PLAYER_JUMP_SPEED
                self.player.jump_needs_reset = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.on_key_press_move_left()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.on_key_press_move_right()
        elif key == arcade.key.X:
            # self.player.is_collecting_life = True
            # self.Generate_Enemie(1, self.player.center_x, 500)
            self.delete_wall()
            self.Generate_Enemie(2, self.player.center_x-50, 200)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = 0
            self.player.is_walking = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = 0
            self.player.is_walking = False
        # elif key == arcade.key.UP or key == arcade.key.W:
        # self.player.is_jumping = False
        # self.player.is_falling = True
        # self.player.jump_needs_reset = False

    def collisions(self):

        hit_list = arcade.check_for_collision_with_list(self.player, self.enemy_list)
        for enemie in hit_list:
            if self.player.is_attacking and not enemie.dead and enemie != self.boss2:
                self.puzzle(enemie.id)
                enemie.dead = True
            elif self.player.is_attacking and not enemie.dead and enemie == self.boss2:
                self.boss2.valor_vida -= 0.5
            if enemie != self.boss2 and enemie.dead_light and(
                    self.player.center_x >= enemie.center_x - 10 and self.player.center_x <= enemie.center_x + 10):
                self.player.is_collecting_life = True
                enemie.collected = True
                if (self.valor_vida < 80):
                    self.valor_vida += 10
            elif enemie!=self.boss2 and not enemie.dead:
                # decrease the character's life
                self.valor_vida -= 0.5

    # Trigger the enemie IA
    def Trigger_IA(self):
        for enemie in self.enemy_list:
            enemie.interact(self.player.center_x, self.player.center_y)
            if enemie == self.boss2 and enemie.is_attacking and abs(self.player.center_x-self.boss2.center_x)<300:
                self.player.center_x -= 500

    def puzzle(self, id):
        if self.Summon_Enemies:
            if len(self.lista) == len(self.sol_puzzle1)-1:
                self.lista.append(id)
                if self.lista == self.sol_puzzle1:
                    self.Cross_Semaphore = True
                    self.delete_wall()
                    self.lista = []
                    self.Level_Pased()
                else:

                    self.lista = []
            else:
                self.lista.append(id)
                i = len(self.lista) - 1
                if not self.lista[i] == self.sol_puzzle1[i]:
                    self.lista = []

        elif self.Summon_Boss:
            if len(self.lista) == len(self.sol_puzzle2)-1:
                self.lista.append(id)
                if self.lista == self.sol_puzzle2:
                    self.Cross_Semaphore = True
                    self.delete_wall()
                    self.lista = []
                    self.Summon_Boss = False
                    self.End_level = True
                    self.Level_Pased()
                    self.delete_boss_wall()
                else:

                    self.lista = []
            else:
                self.lista.append(id)
                i = len(self.lista) - 1
                if not self.lista[i] == self.sol_puzzle2[i]:
                    self.lista = []


    def Summon_Enemie(self):
        if self.Summon_Enemies and self.player.center_x > 600:
            if random.randint(0, 175) == 0:
                range = random.randint(-500, 500)
                if range >= 0:
                    minim = 600
                else:
                    minim = -600
                if self.player.center_x + minim + range > 3000:
                    self.Generate_Enemie(0, 2950, 200)
                else:
                    self.Generate_Enemie(0, self.player.center_x + minim + range, 200)

            if random.randint(0, 175) == 0:
                range = random.randint(-500, 500)
                if range >= 0:
                    minim = 600
                else:
                    minim = -600
                if self.player.center_x + minim + range > 3000:
                    self.Generate_Enemie(1, 2950, 200)
                else:
                    self.Generate_Enemie(1, self.player.center_x + minim + range, 200)

        elif self.Summon_Boss and self.player.center_x > 600:
            if random.randint(0, 155) == 0:
                range = random.randint(-500, 500)
                if range >= 0:
                    minim = 600
                else:
                    minim = -600
                if self.player.center_x + minim + range > 6300:
                    self.Generate_Enemie(0, 6300 + minim + range, 200)
                else:
                    self.Generate_Enemie(0, self.player.center_x + minim + range, 200)

            if random.randint(0, 155) == 0:
                range = random.randint(-500, 500)
                if range >= 0:
                    minim = 600
                else:
                    minim = -600
                if self.player.center_x + minim + range > 6300:
                    self.Generate_Enemie(1, 600 + minim + range, 200)
                else:
                    self.Generate_Enemie(1, self.player.center_x + minim + range, 200)

            elif self.dead_boss2:
                self.Generate_Enemie(2, self.player.center_x, 0)


    def Generate_Enemie(self, numero_de_Portal, pos_x, pos_y):

        if (numero_de_Portal == 0):
            alive1 = False
            alive2 = False
            for enemi in self.enemy_list:
                if enemi == self.enemy01:
                    alive1 = True
                if enemi == self.enemy11:
                    alive2 = True
            if not alive1:
                if self.enemy01 == None:
                    # Set up the enemy1
                    self.enemy01 = Enemie_1()
                    self.enemy01.setup()
                self.enemy01.Load()
                # Set up the enemy1 position
                self.enemy01.center_x = pos_x
                self.enemy01.center_y = pos_y
                self.enemy01.scale = PLAYER_SCALE

                self.enemy_list.append(self.enemy01)

                self.physics_engine_enemy01 = arcade.PhysicsEnginePlatformer(self.enemy01, self.wall_list,
                                                                            gravity_constant=GRAVITY)

            elif not alive2:
                if self.enemy11 == None:
                    # Set up the enemy1
                    self.enemy11 = Enemie_1()
                    self.enemy11.setup()
                self.enemy11.Load()
                # Set up the enemy1 position
                self.enemy11.center_x = pos_x
                self.enemy11.center_y = pos_y
                self.enemy11.scale = PLAYER_SCALE

                self.enemy_list.append(self.enemy11)

                self.physics_engine_enemy11 = arcade.PhysicsEnginePlatformer(self.enemy11, self.wall_list,
                                                                        gravity_constant=GRAVITY)

        elif numero_de_Portal == 1:
            alive1 = False
            alive2 = False
            for enemi in self.enemy_list:
                if enemi == self.enemy02:
                    alive1 = True
                if enemi == self.enemy22:
                    alive2 = True
            if not alive1:
                if self.enemy02 == None:
                    # Set up the enemy1
                    self.enemy02 = Enemie_1()
                    self.enemy02.setup()
                self.enemy02.Load()
                # Set up the enemy1 position
                self.enemy02.center_x = pos_x
                self.enemy02.center_y = pos_y
                self.enemy02.scale = PLAYER_SCALE

                self.enemy_list.append(self.enemy02)

                self.physics_engine_enemy02 = arcade.PhysicsEnginePlatformer(self.enemy02, self.wall_list,
                                                                             gravity_constant=GRAVITY)

            elif not alive2:
                if self.enemy22 == None:
                    # Set up the enemy1
                    self.enemy22 = Enemie_1()
                    self.enemy22.setup()
                self.enemy22.Load()
                # Set up the enemy1 position
                self.enemy22.center_x = pos_x
                self.enemy22.center_y = pos_y
                self.enemy22.scale = PLAYER_SCALE

                self.enemy_list.append(self.enemy22)

                self.physics_engine_enemy22 = arcade.PhysicsEnginePlatformer(self.enemy22, self.wall_list,
                                                                             gravity_constant=GRAVITY)
        elif numero_de_Portal == 2:
            # Set up the enemy1 position
            self.boss2.center_x = 7400
            self.boss2.center_y = 200
            self.boss2.scale = BOSS_SCALE_2
            self.dead_boss2 = False
            self.enemy_list.append(self.boss2)

    def delete_wall(self):
        for i in range(3):
            for elem in self.wall_list:
                if elem.type == "Sema":
                    self.wall_list.remove(elem)

    def delete_boss_wall(self):
        for i in range(3):
            for elem in self.wall_list:
                if elem.type == "Boss":
                    self.wall_list.remove(elem)

    def Level_Pased(self):
        for enemi in self.enemy_list:
            enemi.dead = True

    def GUI(self):
        arcade.draw_lrtb_rectangle_filled(self.view_left + 1195, self.view_left + 1206,
                                          self.view_bottom + self.valor_vida * 1.8 + 480, self.view_bottom + 475,
                                          (250, 18, 201))
        arcade.draw_circle_filled(self.view_left + 1200, self.view_bottom + 475, radius=6, color=(250, 18, 201))
        self.life_bar.bottom = self.view_bottom + 450
        self.life_bar.center_x = self.view_left + 1200
        self.life_bar_list.draw()