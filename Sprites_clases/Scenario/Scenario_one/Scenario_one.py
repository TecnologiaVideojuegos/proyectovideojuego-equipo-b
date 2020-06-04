# https://stackoverflow.com/questions/59341396/cant-get-attack-animation-to-work-for-arcade-library-with-python
import arcade
from Sprites_clases.Main_character.Main_character import *
from Sprites_clases.Enemie_1.Enemie_1 import *
from Sprites_clases.Enemie_2.Enemie_2 import *
from Variables import *


class Scenario(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.background = None
        # Our physics engine
        self.physics_engine = None
        self.physics_engine_enemy1 = None
        self.physics_engine_enemy2 = None

        # Set up the player
        self.player = None
        # Set up the enemy1
        self.enemy1 = None
        self.enemy2 = None
        # Sprite lists
        self.player_list = None
        self.enemy_list = None
        self.wall_list = None
        self.background_items_list = None

        self.lista = None

        self.valor_vida = None

        self.Game_over = False

        self.view_left = 0
        self.view_bottom = 0
        self.end_of_map = 0

        # Barra vida
        self.life_bar_list = None

    def setup(self):

        self.lista = []

        self.valor_vida = 100

        #Set up the Sprites
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.background_items_list = arcade.SpriteList()
        self.life_bar_list = arcade.SpriteList()

        # Set up the player
        self.player = Main_Character()
        self.player.setup()

        # Set up the player position
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player.scale = PLAYER_SCALE

        self.player_list.append(self.player)

        # Barra de vida
        self.life_bar = arcade.Sprite(barra_vida, SPRITE_SCALE)
        self.life_bar_list.append(self.life_bar)

       # -- Set up the walls

        # Create the ground
        for i in range(125):
            wall = arcade.Sprite(":resources:images/tiles/stone.png", SPRITE_SCALE)
            wall.bottom = 0
            wall.center_x = i * GRID_PIXEL_SIZE
            self.wall_list.append(wall)

        # Create the Wall
        for posy in [0,5000, 8000]:
            for i in range(10):
                wall = arcade.Sprite(":resources:images/tiles/stone.png", SPRITE_SCALE)
                wall.bottom = 0
                wall.center_y = i * GRID_PIXEL_SIZE
                wall.center_x = posy
                self.wall_list.append(wall)



        #Añadiendo cartel gasolinera
        item = arcade.Sprite(Cartel_Gasolinera_Sprite, SPRITE_SCALE)
        item.bottom = 0
        item.center_y = 230
        item.center_x = 3200
        self.background_items_list.append(item)
        #Añadiendo semaforo rojo
        item = arcade.Sprite(Semaforo_Rojo_Sprite, SPRITE_SCALE)
        item.bottom = 0
        item.center_y = 260
        item.center_x = 5000
        self.background_items_list.append(item)
        #Añadiendo Cartel direcciones
        item = arcade.Sprite(Señal_Direcciones_Sprite, SPRITE_SCALE)
        item.bottom = 0
        item.center_y = 95
        item.center_x = 600
        self.background_items_list.append(item)



        # Set the physics_engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, self.wall_list, gravity_constant=GRAVITY)

        # Load the background image
        self.background = arcade.load_texture(Scenario_sprite)


    def on_update(self, delta_time):


        if self.valor_vida <= 0:
            self.Game_over = True
            self.close()
        else:

            self.player.is_falling = self.player.change_y < 0
            self.player_list.update_animation()

            self.physics_engine.update()


            if(len(self.enemy_list)>0):
                self.enemy_list.update_animation()
                if self.physics_engine_enemy1 != None :
                    self.physics_engine_enemy1.update()
                if self.physics_engine_enemy2 != None:
                    self.physics_engine_enemy2.update()

            self.collisions()
            self.Trigger_IA()



            # --- Manage Scrolling ---

            # Track if we need to change the viewport

            changed = False

            # Scroll left
            left_boundary = self.view_left + SCREEN_WIDTH - RIGHT_MARGIN*1.5
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


    def on_draw(self):
        arcade.start_render()
        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(-1000, 0, 9000, SCREEN_HEIGHT, self.background) #At wall ground length 20 the width is 1280
        #self.wall_list.draw()                                                                   #At wall ground lenght 100 the image witdh is 6450
        self.background_items_list.draw()
        self.player_list.draw()
        self.GUI()

        score_text = f"Vida: {self.valor_vida}"
        arcade.draw_text(score_text, self.view_left + 50, self.view_bottom + 650,
                         arcade.csscolor.BLACK, 18)


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
            self.delete_wall(700)
            self.Generate_Enemie(1, SCREEN_HEIGHT//2, SCREEN_WIDTH//2)  #posicion valida Screen hight and width //2

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = 0
            self.player.is_walking = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = 0
            self.player.is_walking = False
        #elif key == arcade.key.UP or key == arcade.key.W:
            #self.player.is_jumping = False
            #self.player.is_falling = True
            #self.player.jump_needs_reset = False


    def collisions(self):

        hit_list = arcade.check_for_collision_with_list(self.player, self.enemy_list)
        for enemie in hit_list:

            if self.player.is_attacking:
                enemie.dead = True
                self.puzzle(enemie.id)
            if not enemie.dead and enemie.is_attacking:
                # decrease the character's life
                self.valor_vida -= 0.5

    #Trigger the enemie IA
    def Trigger_IA(self):
        for enemie in self.enemy_list:
            enemie.interact(self.player.center_x, self.player.center_y)

    def puzzle(self, id):
        if self.lista == []:
            self.lista.append(id)
        elif self.lista[len(self.lista) - 1] != id:
            self.lista.append(id)
            print(self.lista)

    def Generate_Enemie(self, numero_de_Portal, pos_x, pos_y):

        if(numero_de_Portal == 0):
            if self.enemy1 == None:
                # Set up the enemy1
                self.enemy1 = Enemie_1()
            self.enemy1.setup()

            # Set up the enemy1 position
            self.enemy1.center_x = pos_x
            self.enemy1.center_y = pos_y
            self.enemy1.scale = PLAYER_SCALE

            self.enemy_list.append(self.enemy1)

            self.physics_engine_enemy1 = arcade.PhysicsEnginePlatformer(self.enemy1, self.wall_list,
                                                                        gravity_constant=GRAVITY)

        elif numero_de_Portal == 1:
            if self.enemy2 == None:
                # Set up the enemy2
                self.enemy2 = Enemie_2()
            self.enemy2.setup()

            # Set up the enemy1 position
            self.enemy2.center_x = pos_x
            self.enemy2.center_y = pos_y
            self.enemy2.scale = PLAYER_SCALE

            self.enemy_list.append(self.enemy2)

            self.physics_engine_enemy2 = arcade.PhysicsEnginePlatformer(self.enemy2, self.wall_list,
                                                                        gravity_constant=GRAVITY)

    def delete_wall(self, pos_x):
        for elem in self.wall_list:
            if elem.center_x == pos_x:
                self.wall_list.remove(elem)

    def GUI(self):
        arcade.draw_lrtb_rectangle_filled(self.view_left + 1190, self.view_left + 1210, self.view_bottom + self.valor_vida + 550, self.view_bottom + 470, arcade.color.BLUE)
        self.life_bar.bottom = self.view_bottom + 450
        self.life_bar.center_x = self.view_left + 1200
        self.life_bar_list.draw()



