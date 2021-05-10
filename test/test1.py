import asciianim as a
import time
import keyboard
import math
import threading
a.createcanvas(135,135)
#points
x=0
y=0
z=0
s=1
p1 = a.vector3d((0+x)*s,(0+y)*s,(0+z)*s)
p2 = a.vector3d((0+x)*s,(0+y)*s,(1+z)*s)
p3 = a.vector3d((0+x)*s,(1+y)*s,(0+z)*s)
p4 = a.vector3d((0+x)*s,(1+y)*s,(1+z)*s)
p5 = a.vector3d((1+x)*s,(0+y)*s,(0+z)*s)
p6 = a.vector3d((1+x)*s,(0+y)*s,(1+z)*s)
p7 = a.vector3d((1+x)*s,(1+y)*s,(0+z)*s)
p8 = a.vector3d((1+x)*s,(1+y)*s,(1+z)*s)
b=math.pi/6
def rotatex(b):
    global p1,p2,p3,p4,p5,p6,p7,p8
    p1=a.rx(b,p1)
    p2=a.rx(b,p2)
    p3=a.rx(b,p3)
    p4=a.rx(b,p4)
    p5=a.rx(b,p5)
    p6=a.rx(b,p6)
    p7=a.rx(b,p7)
    p8=a.rx(b,p8)
def rotatey(b):
    global p1,p2,p3,p4,p5,p6,p7,p8
    p1=a.ry(b,p1)
    p2=a.ry(b,p2)
    p3=a.ry(b,p3)
    p4=a.ry(b,p4)
    p5=a.ry(b,p5)
    p6=a.ry(b,p6)
    p7=a.ry(b,p7)
    p8=a.ry(b,p8)
def rotatez(b):
    global p1,p2,p3,p4,p5,p6,p7,p8
    p1=a.rz(b,p1)
    p2=a.rz(b,p2)
    p3=a.rz(b,p3)
    p4=a.rz(b,p4)
    p5=a.rz(b,p5)
    p6=a.rz(b,p6)
    p7=a.rz(b,p7)
    p8=a.rz(b,p8)

theta=0.01
while(True):
    #triangles
    #south
    rotatez(theta)
    rotatex(theta/2)
    t1 = a.triangle(p1,p3,p7)
    t2 = a.triangle(p1,p7,p5)
    #east
    t3 = a.triangle(p5,p7,p8)
    t4 = a.triangle(p5,p8,p6)
    #north
    t5 = a.triangle(p6,p8,p4)
    t6 = a.triangle(p6,p4,p2)
    #west
    t7 = a.triangle(p2,p4,p3)
    t8 = a.triangle(p2,p3,p1)
    #top
    t9 = a.triangle(p3,p4,p8)
    t10 = a.triangle(p3,p8,p7)
    #bottom
    t11 = a.triangle(p6,p2,p1)
    t12 = a.triangle(p6,p1,p5)
    #mesh
    k =[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12]
    mesh = a.mesh(k)
    for i in range(12):
        a.triangle_3d(mesh.k[i],True)
    a.draw()
    a.clearbg()
    time.sleep(0.05)    
input()