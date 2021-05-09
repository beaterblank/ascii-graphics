import asciianim as a
import time
import keyboard
a.createcanvas(240,135,True)
#points
x=50
y=10
z=0
s=1
p1 = a.vector3d((25+x)*s,(25+y)*s,(0+z)*s)
p2 = a.vector3d((25+x)*s,(25+y)*s,(50+z)*s)
p3 = a.vector3d((25+x)*s,(75+y)*s,(0+z)*s)
p4 = a.vector3d((25+x)*s,(75+y)*s,(50+z)*s)
p5 = a.vector3d((75+x)*s,(25+y)*s,(0+z)*s)
p6 = a.vector3d((75+x)*s,(25+y)*s,(50+z)*s)
p7 = a.vector3d((75+x)*s,(75+y)*s,(0+z)*s)
p8 = a.vector3d((75+x)*s,(75+y)*s,(50+z)*s)
#normals
#south
n1 = a.normal(p1,p3,p7)
n2 = a.normal(p1,p7,p5)
#east
n3 = a.normal(p5,p7,p8)
n4 = a.normal(p5,p8,p6)
#north
n5 = a.normal(p6,p8,p4,False)
n6 = a.normal(p6,p4,p2,False)
#west
n7 = a.normal(p2,p8,p3,False)
n8 = a.normal(p2,p3,p1,False)
#top
n9 = a.normal(p3,p4,p8)
n10 = a.normal(p3,p8,p7)
#bottom
n11 = a.normal(p6,p2,p1,False)
n12 = a.normal(p6,p1,p5,False)
def rotatex(b):
    global p1,p2,p3,p4,p5,p6,p7,p8
    global n1,n2,n3,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12
    p1=a.rx(b,p1)
    p2=a.rx(b,p2)
    p3=a.rx(b,p3)
    p4=a.rx(b,p4)
    p5=a.rx(b,p5)
    p6=a.rx(b,p6)
    p7=a.rx(b,p7)
    p8=a.rx(b,p8)

    n1=a.rx(b,n1)
    n2=a.rx(b,n2)
    n3=a.rx(b,n3)
    n4=a.rx(b,n4)
    n5=a.rx(b,n5)
    n6=a.rx(b,n6)
    n7=a.rx(b,n7)
    n8=a.rx(b,n8)
    n9=a.rx(b,n9)
    n10=a.rx(b,n10)
    n11=a.rx(b,n11)
    n12=a.rx(b,n12)

def rotatey(b):
    global p1,p2,p3,p4,p5,p6,p7,p8
    global n1,n2,n3,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12
    p1=a.ry(b,p1)
    p2=a.ry(b,p2)
    p3=a.ry(b,p3)
    p4=a.ry(b,p4)
    p5=a.ry(b,p5)
    p6=a.ry(b,p6)
    p7=a.ry(b,p7)
    p8=a.ry(b,p8)

    n1=a.ry(b,n1)
    n2=a.ry(b,n2)
    n3=a.ry(b,n3)
    n4=a.ry(b,n4)
    n5=a.ry(b,n5)
    n6=a.ry(b,n6)
    n7=a.ry(b,n7)
    n8=a.ry(b,n8)
    n9=a.ry(b,n9)
    n10=a.ry(b,n10)
    n11=a.ry(b,n11)
    n12=a.ry(b,n12)
def rotatez(b):
    global p1,p2,p3,p4,p5,p6,p7,p8
    global n1,n2,n3,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12
    p1=a.rz(b,p1)
    p2=a.rz(b,p2)
    p3=a.rz(b,p3)
    p4=a.rz(b,p4)
    p5=a.rz(b,p5)
    p6=a.rz(b,p6)
    p7=a.rz(b,p7)
    p8=a.rz(b,p8)

    n1=a.rz(b,n1)
    n2=a.rz(b,n2)
    n3=a.rz(b,n3)
    n4=a.rz(b,n4)
    n5=a.rz(b,n5)
    n6=a.rz(b,n6)
    n7=a.rz(b,n7)
    n8=a.rz(b,n8)
    n9=a.rz(b,n9)
    n10=a.rz(b,n10)
    n11=a.rz(b,n11)
    n12=a.rz(b,n12)

def movx(b):
    global p1,p2,p3,p4,p5,p6,p7,p8
    global n1,n2,n3,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12
    p1.x+=b
    p2.x+=b
    p3.x+=b
    p4.x+=b
    p5.x+=b
    p6.x+=b
    p7.x+=b
    p8.x+=b

    n1.x+=b
    n2.x+=b
    n3.x+=b
    n4.x+=b
    n5.x+=b
    n6.x+=b
    n7.x+=b
    n8.x+=b
    n9.x+=b
    n10.x+=b
    n11.x+=b
    n12.x+=b

def movy(b):
    global p1,p2,p3,p4,p5,p6,p7,p8
    global n1,n2,n3,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12
    p1.y+=b
    p2.y+=b
    p3.y+=b
    p4.y+=b
    p5.y+=b
    p6.y+=b
    p7.y+=b
    p8.y+=b

    n1.y+=b
    n2.y+=b
    n3.y+=b
    n4.y+=b
    n5.y+=b
    n6.y+=b
    n7.y+=b
    n8.y+=b
    n9.y+=b
    n10.y+=b
    n11.y+=b
    n12.y+=b

def movz(b):
    global p1,p2,p3,p4,p5,p6,p7,p8
    global n1,n2,n3,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12
    p1.z+=b
    p2.z+=b
    p3.z+=b
    p4.z+=b
    p5.z+=b
    p6.z+=b
    p7.z+=b
    p8.z+=b

    n1.z+=b
    n2.z+=b
    n3.z+=b
    n4.z+=b
    n5.z+=b
    n6.z+=b
    n7.z+=b
    n8.z+=b
    n9.z+=b
    n10.z+=b
    n11.z+=b
    n12.z+=b

while(True):
    time.sleep(0.03)
    if keyboard.is_pressed('a'):
        rotatex(0.02)
    if keyboard.is_pressed('s'):
        rotatey(0.02)
    if keyboard.is_pressed('d'):
        rotatez(0.02)
    if keyboard.is_pressed('q'):
        rotatex(-0.02)
    if keyboard.is_pressed('w'):
        rotatey(-0.02)
    if keyboard.is_pressed('e'):
        rotatez(-0.02)
    if keyboard.is_pressed('r'):
        movx(2)
    if keyboard.is_pressed('t'):
        movy(2)
    if keyboard.is_pressed('y'):
        movz(2)
    if keyboard.is_pressed('f'):
        movx(-2)
    if keyboard.is_pressed('g'):
        movy(-2)
    if keyboard.is_pressed('h'):
        movz(-2)
    #triangles
    #south
    t1 = a.triangle(p1,p3,p7)
    t2 = a.triangle(p1,p7,p5)
    #east
    t3 = a.triangle(p5,p7,p8)
    t4 = a.triangle(p5,p8,p6)
    #north
    t5 = a.triangle(p6,p8,p4)
    t6 = a.triangle(p6,p4,p2)
    #west
    t7 = a.triangle(p2,p8,p3)
    t8 = a.triangle(p2,p3,p1)
    #top
    t9 = a.triangle(p3,p4,p8)
    t10 = a.triangle(p3,p8,p7)
    #bottom
    t11 = a.triangle(p6,p2,p1)
    t12 = a.triangle(p6,p1,p5)
    #mesh
    k =[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12]
    l =[n1,n2,n3,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12]
    mesh = a.mesh(k)
    for i in range(12):
        a.triangle_3d(mesh.k[i],l[i],True)
    a.draw()
    a.clearbg()
    
