import arcade
from Drawings import *

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self,width,height,tittle):
        super().__init__(width,height,tittle)
        arcade.set_background_color(arcade.color.GREEN)
        # self.set_mouse_visible(False)   #Hide mouse
        """ Initializer """
        self.Object= Object(0,0)

    def on_draw(self):
        arcade.start_render()
        self.Object.draw()
    """def on_mouse_motion(self, x, y, dx, dy):     #Move when moving mouse
        self.Object.position_x=x
        self.Object.position_y=y"""
    """def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):  #move at mouse click
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.Object.position_x = x
            self.Object.position_y = y
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)"""

    def on_key_press(self, key, modifiers):
        while key == arcade.key.LEFT:
            self.Object.position_x-=10
        while key == arcade.key.RIGHT:
            self.Object.position_x+=10
        while key==arcade.key.UP:
            self.Object.position_y+=10
        while key==arcade.key.DOWN:
            self.Object.position_y-=10


class Object:
    def __init__(self,position_x,position_y):  #Contructor
        self.position_x=position_x
        self.position_y=position_y
    def draw(self):     #initializace the drawing
        little_person(self.position_x,self.position_y)
def buscar_ultima_posicion(cadena,elem):
    pos_final=-1
    for i in len(cadena):
        if(cadena[i]==elem):
            pos_final=i
    return pos_final