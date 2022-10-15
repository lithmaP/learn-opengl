from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import random


def myInit():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # RGBA
    # glColor3f(225.0, 225.0, 225.0) #RGB
    # glPointSize(5.0)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    gluOrtho2D(0, 550, 0, 550)  # left - 0 , right- 500 , bottom -0 , top- 500
    # enable blending for creating gradients


# def planets():
#     posx, posy = 450, 450
#     sides = 32
#     radius = 1
#     glBegin(GL_POLYGON)
#     for i in range(sides):
#         cosine = radius * cos(i * 2 * pi / sides) + posx
#         sine = radius * sin(i * 2 * pi / sides) + posy
#         glVertex2f(cosine, sine)s
#     glEnd()

def draw_planet_1():  # moon
    # glClear(GL_COLOR_BUFFER_BIT)
    # create a circle with many triangles
    glColor3f(1, 1, 0.8)
    pos_x, pos_y, radius = 400.0, 400.0, 45.0
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(pos_x, pos_y)

    for i in range(361):
        glVertex2f(
            radius * cos(pi * i / 180.0) + pos_x, radius * sin(pi * i / 180.0) + pos_y
        )
    glEnd()


def draw_planet_2():  # other_planet
    # glClear(GL_COLOR_BUFFER_BIT)
    # create a circle with many triangles
    glColor3f(0.2, 0.4, 1)
    pos_x, pos_y, radius = 120.0, 300.0, 20.0
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(pos_x, pos_y)

    for i in range(361):
        glVertex2f(
            radius * cos(pi * i / 180.0) + pos_x, radius * sin(pi * i / 180.0) + pos_y
        )
    glEnd()


def draw_planet_3():  # earth
    # glClear(GL_COLOR_BUFFER_BIT)
    # create a circle with many triangles
    pos_x, pos_y, radius = 60.0, -10.0, 200.0
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(pos_x, pos_y)
    glColor3f(0.2, 0.8, 0.2)
    for i in range(361):
        glVertex2f(
            radius * cos(pi * i / 180.0) + pos_x, radius * sin(pi * i / 180.0) + pos_y
        )
    glEnd()


def space():
    glPointSize(2.0)
    glBegin(GL_POINTS)
    for _ in range(0, 300):
        isOn = bool(random.getrandbits(1))
        if isOn:
            glColor3f(1, 0.70, 0.30)
        else:

            glColor3f(1, 1, 0.9)
        # glColor3f(1, 1, 0.9)
        glVertex2f(random.randint(0, 550), random.randint(0, 550))

    glEnd()

    glFlush()


def draw_rocket():

    # Rocket_body
    glBegin(GL_POLYGON)
    glColor3f(0.82, 0.82, 0.76) # DARK GREY
    glVertex2f(250.0, 435.0)
    glColor3f(0.39, 0.39, 0.39)
    glVertex2f(220.0, 350.0)
    glVertex2f(220.0, 150.0)
    glVertex2f(280.0, 150.0)
    glVertex2f(280.0, 350.0)
    glEnd()

    # top triangle
    # glBegin(GL_TRIANGLE_STRIP)
    # glColor3f(0.82, 0.82, 0.76)  # LIGHT GREY
    #
    # glVertex2f(280.0, 350.0)
    # glVertex2f(220.0, 350.0)
    # glEnd()

    # bottom big smoke triangle
    glBegin(GL_POLYGON)
    glColor3f(255, 204, 0)
    glVertex2f(220.0, 150.0)
    glColor3f(0.87, 0.4, 0.23)
    glVertex2f(190.0, 90.0)
    glColor3f(1, 0.5, 0.0)
    glVertex2f(220.0, 110.0)
    glVertex2f(250.0, 30.0)
    glColor3f(255, 204, 0)
    glVertex2f(280.0, 110.0)
    glVertex2f(310.0, 90.0)
    glVertex2f(280.0, 150.0)
    glEnd()

    # body-left triangle
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(0.9, 0.0, 0.0)
    glVertex2f(220.0, 150.0)
    glVertex2f(220.0, 250.0)
    glVertex2f(170.0, 150.0)
    glEnd()

    # body-right triangle
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(0.9, 0.0, 0.0)
    glVertex2f(280.0, 150.0)
    glVertex2f(280.0, 250.0)
    glVertex2f(330.0, 150.0)
    glEnd()

    # body-middle triangle
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(0.9, 0.0, 0.0)
    glVertex2f(250.0, 250.0)
    glVertex2f(245.0, 150.0)
    glVertex2f(255.0, 150.0)
    glEnd()

    #rocket-window-outer-circle
    pos_x, pos_y, radius = 250.0, 325.0, 20.0
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(pos_x, pos_y)
    glColor3f(1, 1, 1)
    for i in range(361):
        glVertex2f(
            radius * cos(pi * i / 180.0) + pos_x, radius * sin(pi * i / 180.0) + pos_y
        )
    glEnd()

    # rocket-window-inner-circle
    pos_x, pos_y, radius = 250.0, 325.0, 17.0
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(pos_x, pos_y)
    glColor3f(0.6, 0.8, 1)
    for i in range(361):
        glVertex2f(
            radius * cos(pi * i / 180.0) + pos_x, radius * sin(pi * i / 180.0) + pos_y
        )
    glEnd()



def falling_star():
    glBegin(GL_LINE_STRIP);
    glColor3f(1, 1, 1)
    glVertex2f(400, 100);
    glVertex2f(420, 120);
    glVertex2f(440, 140);
    glVertex2f(450, 150);
    glEnd();

    glBegin(GL_LINE_STRIP);
    glColor3f(1, 1, 1)
    glVertex2f(400, 500);
    glVertex2f(420, 520);
    glVertex2f(440, 540);

    glEnd();

    glBegin(GL_LINE_STRIP);
    glColor3f(1, 1, 1)
    glVertex2f(110, 400);
    glVertex2f(120, 410);
    glVertex2f(130, 420);
    glVertex2f(140, 430);
    glVertex2f(150, 440);
    glVertex2f(160, 450);
    glVertex2f(170, 460);
    glVertex2f(180, 470);
    glVertex2f(190, 480);
    glVertex2f(200, 490);
    glEnd();


def displayScene():
    draw_planet_1()
    draw_planet_2()
    draw_planet_3()
    draw_rocket()
    falling_star()
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Rocket_modified")
    myInit()
    space()
    glutDisplayFunc(displayScene)
    glutMainLoop()
