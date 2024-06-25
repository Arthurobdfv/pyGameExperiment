import pygame as pg
import moderngl as mgl
import sys
from Modules.model import *

class GraphicsEngine:
    def __init__(self, win_size=(1600,900)):
        # init pygame modules
        pg.init()
        self.WIN_SIZE = win_size
        # Specifies use og OpenGL 3,3
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        # create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # detect and use existing opengl context
        self.ctx = mgl.create_context()
        self.clock = pg.time.Clock() 
        self.scene = Triangle(self)
        self.set_back_color()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()

    def set_back_color(self,color=(0.08, 0.16, 0.18)):
        self.background_color = color

    def render(self):
        self.ctx.clear(color=self.background_color)
        pg.display.flip()            

    def run(self):
        while True:
            self.check_events() 
            # Render scene
            self.render()
            self.clock.tick(60)

            
print(__name__)
if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()