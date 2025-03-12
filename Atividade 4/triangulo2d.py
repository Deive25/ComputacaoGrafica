import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Variáveis de posição do triângulo
x = 0      # Centralizado
y = 0      # Centralizado
r = 0      # Rotação
z_pos = -6 # Posição Z inicial

# Variáveis de escala
ex = 2  # Escala 2x
ey = 2  # Escala 2x
ez = 2  # Escala 2x

def init():
    glClearColor(1, 1, 1, 1)  # Fundo branco
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 640/480, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)

def draw():
    glLoadIdentity()
    glTranslatef(x, y, z_pos)  # Zoom com z_pos
    glRotatef(r, 1, 1, 0)     # Rotação em X e Y
    glScalef(ex, ey, ez)
    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 0)        # Triângulo preto
    glVertex3f(0, 2, 0)       # Vértices maiores
    glVertex3f(-2, -2, 0)
    glVertex3f(2, -2, 0)
    glEnd()

def main():
    pygame.init()
    pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)
    init()
    global x, y, r, ex, ey, ez, z_pos
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_a:
                    x += 0.2   # Direita
                if event.key == K_d:
                    x += -0.2  # Esquerda
                if event.key == K_w:
                    y += 0.2
                if event.key == K_s:
                    y += -0.2
                if event.key == K_z:
                    z_pos += 0.2  # Aproxima
                if event.key == K_x:
                    z_pos -= 0.2  # Afasta
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 4:
                    ex += 0.2
                    ey += 0.2
                    ez += 0.2
                if event.button == 5:
                    ex -= 0.2
                    ey -= 0.2
                    ez -= 0.2
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)
        r -= 3  # Rotação horária
    pygame.quit()

if __name__ == "__main__":
    main()