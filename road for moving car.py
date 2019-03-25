from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def MyInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60 , 1 , 1 , 30)
    gluLookAt(8,9,10,
              0,0,0,
    0,1,0)

    glClearColor(0.8,0.7,0,1)
    glClear(GL_COLOR_BUFFER_BIT)

def XYZ():

    glEnd()

x=0
angle=0
forward=0
def draw():
    global angle
    global x
    global forward


    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

# pavement left
    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(-22, 1, -2.7)
    glScale(0.8, 0.2, 0.2)
    glutSolidCube(5)


    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-18, 1, -2.7)
    glScale(0.8, 0.2, 0.2)
    glutSolidCube(5)


    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(-14, 1, -2.7)
    glScale(0.8, 0.2, 0.2)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-10, 1, -2.7)
    glScale(0.8, 0.2, 0.2)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(-6, 1, -2.7)
    glScale(0.8, 0.2, 0.2)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-2, 1, -2.7)
    glScale(0.8, 0.2, 0.2)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(2, 1, -2.7)
    glScale(0.8, 0.2, 0.2)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(6, 1, -2.7)
    glScale(0.8, 0.2, 0.2)
    glutSolidCube(5)



    #road
    glLoadIdentity()

    glBegin(GL_QUADS)
    glColor3f(0.8,0.9,0.9)
    glVertex(10, 0, -3)
    glVertex(-26, 0, -3)
    glVertex(-20, 0, 3)
    glVertex(10, 0, 3)



    glColor3f(1,1,1)
    glVertex(10, 0, -1)
    glVertex(-20, 0, -1)
    glVertex(-20, 0, 1)
    glVertex(10, 0, 1)




    glEnd()




 # body
    glLoadIdentity()
    glColor3f(1, 0, 0)
    glTranslate(x,0,0)
    glScale(1, 0.25, 0.5)
    glutWireCube(5)

    glLoadIdentity()
    glTranslate(x,5*0.25,0)
    glScale(0.5, 0.25, 0.5)
    glutWireCube(5)

    # light

    glLoadIdentity()
    glColor3f(0.8, 1, 0)
    glTranslate(x + 2.8, 0, 1)
    glutWireSphere(0.3, 100, 100)

    glLoadIdentity()
    glColor3f(0.8, 1, 0)
    glTranslate(x + 2.8, 0, -0.8)
    glutWireSphere(0.3, 100, 100)


#wheels

    glColor3f(1,0,1)
    glLoadIdentity()
    glTranslate(x+1.25,-5*0.25*.5,5*0.5*0.5)
    glRotate(angle,0,0,1)

    glutWireTorus(0.15,0.5,12,10)

    glColor3f(1, 0, 1)
    glLoadIdentity()
    glTranslate(x+-1.25, -5 * 0.25 * .5, 5 * 0.5 * 0.5)
    glRotate(angle, 0, 0, 1)

    glutWireTorus(0.15, 0.5, 12, 10)

    glColor3f(1, 0, 1)
    glLoadIdentity()
    glTranslate(x+1.25, -5 * 0.25 * .5, -5 * 0.5 * 0.5)
    glRotate(angle, 0, 0, 1)

    glutWireTorus(0.15, 0.5, 12, 10)

    glColor3f(1, 0, 1)
    glLoadIdentity()
    glTranslate(x+-1.25, -5 * 0.25 * .5, 5 * 0.5 * -0.5)
    glRotate(angle, 0, 0, 1)

    glutWireTorus(0.15, 0.5, 12, 10)

#pavement right



    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-10,0,3.2)
    glScale(0.8, 0.2, 0.2)
    glutSolidCube(5)


    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(-6,0,3.2)
    glScale(0.8, 0.2, 0.2)
    glutSolidCube(5)






    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-2,0,3.2)
    glScale(0.8, 0.2, 0.2)
    glutSolidCube(5)



    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(2,0,3.2)
    glScale(0.8, 0.2, 0.2)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(6,0,3.2)
    glScale(0.8, 0.2, 0.2)
    glutSolidCube(5)


    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(10,0,3.2)
    glScale(0.8, 0.2, 0.2)
    glutSolidCube(5)








    glutSwapBuffers()
    glBegin(GL_LINES)

    if forward:
        angle-=0.1
        x+=0.002
        if x>5:
            forward=False
    else:
        angle+=0.1
        x-=0.002
        if x<-5:
            forward=True











    glEnd()

glutInit()

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(700, 700)
glutCreateWindow(b"Moving Car program")
glutDisplayFunc(draw)
glutIdleFunc(draw)
MyInit()
glutMainLoop()
