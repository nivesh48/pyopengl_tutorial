import pygame as pg
from OpenGL.GL import *

class App:
    def __init__(self):
        #initialize python
        pg.init()
        pg.display.set_mode((640, 480), pg.OPENGL|pg.DOUBLEBUF) #opengl context
        self.clock = pg.time.Clock() #control the frame rate
        glClearColor(1, 0.2, 0.2, 1)
        self.mainloop()

    def mainloop(self):
        running = True
        while (running):
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    running = False

            glClear(GL_COLOR_BUFFER_BIT) #32 bit unsigned #RGBA - 8 bit for one color components
            pg.display.flip()

            self.clock.tick(60)
        self.quit()

    def quit(self):
        pg.quit()


if __name__ == "__main__":
    myapp = App()