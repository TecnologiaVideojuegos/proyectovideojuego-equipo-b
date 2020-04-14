import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Sprite animated walking"
SPRITE_SCALE=0.5

# Movement speed of player, in pixels per frame
MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

class MyGame(arcade.Window):
    """Inicializador"""
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.CADET_GREY)

        self.player_list = None

        self.wall_list = None
        #variable that holds the player sprite
        self.player = None

        # Our physics engine
        self.physics_engine = None


    def setup(self):
        "El archivo WalkingX.png lo metí directamente en la carpeta del proyecto de PyCharm"
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.player = arcade.AnimatedWalkingSprite()

        #Stand Right Sprites
        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture("JumpingX.png", x=0, y=0, width=240, height=520))

        #Stand left sprites
        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(
            arcade.load_texture("JumpingX.png", x=0, y=0, width=240, height=520, mirrored=True))

        #Jump Sprites
        self.player.walk_up_textures = []
        for i in range(9):
            self.player.walk_up_textures.append(
                arcade.load_texture("JumpingX.png", x=i * 236, y=0, width=220, height=522))

        #Fall Sprites
        self.player.walk_down_textures = []
        for i in range(9):
            self.player.walk_down_textures.append(
                arcade.load_texture("JumpingX.png", x=i * 236, y=0, width=220, height=520))

        # Walk Right Sprites
        self.player.walk_right_textures = []
        for i in range(7):
            self.player.walk_right_textures.append(arcade.load_texture("WalkingX.png", x=i*236+50, y=0, width=220, height=522))

        # Walk Left Sprites
        self.player.walk_left_textures = []
        for i in range(7):
            self.player.walk_left_textures.append(arcade.load_texture("WalkingX.png", x=i*236+50, y=0, width=220, height=520, mirrored=True))

            # Create the ground
            # This shows using a loop to place multiple sprites horizontally
            for x in range(0, 1250, 64):
                wall = arcade.Sprite(":resources:images/tiles/grassMid.png", 0.5)
                wall.center_x = x
                wall.center_y = 32
                self.wall_list.append(wall)


        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,self.wall_list,GRAVITY)

        self.player.center_x= SCREEN_WIDTH//2
        self.player.center_y=SCREEN_HEIGHT//2
        self.player.scale=SPRITE_SCALE

        self.player_list.append(self.player)

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()

    def on_update(self,delta_time):

        self.physics_engine.update()
        self.player_list.update()
        self.player_list.update_animation()

    def on_key_press(self,key,modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self,key,modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = 0


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT,SCREEN_TITLE)
    window.setup()
    arcade.run()

main()