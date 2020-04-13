import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Sprite animated walking"
MOVEMENT_SPEED = 5
SPRITE_SCALE=1

class MyGame(arcade.Window):
    """Inicializador"""
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.CADET_GREY)

        self.player_list = None
        self.player = None

    def setup(self):
        "El archivo WalkingX.png lo metí directamente en la carpeta del proyecto de PyCharm"
        self.player_list = arcade.SpriteList()
        self.player = arcade.AnimatedWalkingSprite()

        self.player.stand_right_textures=[]
        self.player.stand_right_textures.append(arcade.load_texture("WalkingX.png", x=0, y=0, width=240, height=520))

        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(arcade.load_texture("WalkingX.png", x=0, y=0, width=240, height=520,mirrored=True))

        self.player.walk_right_textures = []
        for i in range(7):
            self.player.walk_right_textures.append(arcade.load_texture("WalkingX.png", x=i*236, y=0, width=240, height=522))

        self.player.walk_left_textures = []
        for i in range(7):
            self.player.walk_left_textures.append(arcade.load_texture("WalkingX.png", x=i*236, y=0, width=240, height=520, mirrored=True))

        self.player.center_x= SCREEN_WIDTH//2
        self.player.center_y=SCREEN_HEIGHT//2
        self.player.scale=SPRITE_SCALE

        self.player_list.append(self.player)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()

    def on_update(self,delta_time):
        self.player_list.update()
        self.player_list.update_animation()

    def on_key_press(self,key,modifiers):

        if key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self,key,modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT,SCREEN_TITLE)
    window.setup()
    arcade.run()

main()
