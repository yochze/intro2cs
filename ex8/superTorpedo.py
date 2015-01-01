from torpedo import *
from objectShapes import SUPER_TORPEDO_SHAPE 

class SuperTorpedo(BaseObject):
    RADIUS = 20
    TORPEDO_LIFESPAN = 100

    def __init__(self,canvas,x,y,dx,dy,direction):
        super().__init__(canvas,x,y,dx,dy,SUPER_TORPEDO_SHAPE,direction,SuperTorpedo.RADIUS)
        self.set_color("Gold")
        self.lifespan = SuperTorpedo.TORPEDO_LIFESPAN 

    def get_life_span(self):
        return self.lifespan

    def move(self,x,y):
        self.lifespan = self.lifespan - 1
        super().move(x,y)
