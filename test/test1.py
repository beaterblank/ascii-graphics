import asciianim as a
import time
a.createcanvas(100,100)
#points
p1 = a.vector3d(25,25,0)
p2 = a.vector3d(25,25,50)
p3 = a.vector3d(25,75,0)
p4 = a.vector3d(25,75,50)
p5 = a.vector3d(75,25,0)
p6 = a.vector3d(75,25,50)
p7 = a.vector3d(75,75,0)
p8 = a.vector3d(75,75,50)
i=0
while(True):
    p1=a.rx(0.01,a.ry(0.02,a.rz(0.015,p1)))
    p2=a.rx(0.01,a.ry(0.02,a.rz(0.015,p2)))
    p3=a.rx(0.01,a.ry(0.02,a.rz(0.015,p3)))
    p4=a.rx(0.01,a.ry(0.02,a.rz(0.015,p4)))
    p5=a.rx(0.01,a.ry(0.02,a.rz(0.015,p5)))
    p6=a.rx(0.01,a.ry(0.02,a.rz(0.015,p6)))
    p7=a.rx(0.01,a.ry(0.02,a.rz(0.015,p7)))
    p8=a.rx(0.01,a.ry(0.02,a.rz(0.015,p8)))
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
    mesh = a.mesh(k)
    for i in range(12):
        a.triangle_3d(mesh.k[i])
    a.draw()
    a.clearbg()