import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

# Variáveis globais
pos_x = 0.0
pos_y = 0.0
zoom = -6.0
rot_x = 0.0
rot_y = 0.0
auto_rot_z = 0.0
step_size = 0.1
rotation_step = 5
auto_rot_speed = 1

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)

def draw_square_lines():
    global pos_x, pos_y, zoom, rot_x, rot_y, auto_rot_z
    glLoadIdentity()
    glTranslatef(pos_x, pos_y, zoom)
    glRotatef(rot_x, 1.0, 0.0, 0.0)
    glRotatef(rot_y, 0.0, 1.0, 0.0)
    glRotatef(auto_rot_z, 0.0, 0.0, 1.0)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()

def main():
    global pos_x, pos_y, zoom, rot_x, rot_y, auto_rot_z  # Adicionando variáveis globais
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.OPENGL)
    init()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Lidar com teclas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            pos_x += step_size
        elif keys[pygame.K_a]:
            pos_x -= step_size
        if keys[pygame.K_w]:
            pos_y += step_size
        elif keys[pygame.K_s]:
            pos_y -= step_size
        if keys[pygame.K_z]:
            if zoom < -0.1:
                zoom += 1.0
        elif keys[pygame.K_x]:
            if zoom > -100:
                zoom -= 1.0
        if keys[pygame.K_r]:
            rot_x += rotation_step
        elif keys[pygame.K_f]:
            rot_x -= rotation_step
        if keys[pygame.K_q]:
            rot_y += rotation_step
        elif keys[pygame.K_e]:
            rot_y -= rotation_step
        # Rotação automática
        auto_rot_z += auto_rot_speed
        # Desenhar
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_square_lines()
        pygame.display.flip()
        pygame.time.wait(33)  # aproximadamente 30 fps
    pygame.quit()

if __name__ == "__main__":
    main()