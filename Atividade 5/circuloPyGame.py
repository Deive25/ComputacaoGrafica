import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 640.0 / 480.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def draw_circle(radius, num_segments=100):
    glBegin(GL_LINE_LOOP)
    for i in range(num_segments):
        angle = 2.0 * math.pi * i / num_segments
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def main():
    pygame.init()
    display = (640, 480)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    init()

    x_pos = 0.0
    y_pos = 0.0
    z_pos = -5.0
    rotation = 0.0  
    scale = 1.0
    move_speed = 0.1
    rotate_speed = 5.0  
    zoom_speed = 0.1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEWHEEL:
                scale += event.y * zoom_speed
                scale = max(0.1, min(scale, 5.0))

        # Controles
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            y_pos += move_speed
        if keys[K_s]:
            y_pos -= move_speed
        if keys[K_a]:
            x_pos -= move_speed
        if keys[K_d]:
            x_pos += move_speed
        if keys[K_f]:  
            rotation -= rotate_speed
        if keys[K_r]:  
            rotation += rotate_speed
        if keys[K_z]:
            scale -= zoom_speed
            scale = max(0.1, scale)
        if keys[K_x]:
            scale += zoom_speed
            scale = min(scale, 5.0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(0.0, 0.0, z_pos)  
        glPushMatrix()
        glTranslatef(x_pos, y_pos, 0.0)  
        glRotatef(rotation, 0, 1, 0)     
        glScalef(scale, scale, 1.0)      
        glColor3f(0.0, 1.0, 0.0)        
        draw_circle(2)                   
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()