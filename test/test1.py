import asciianim as a
a.createcanvas(100,100)
p1 = a.vector3d(0,0,0)
p2 = a.vector3d(0,0,1)
p3 = a.vector3d(0,1,0)
p4 = a.vector3d(0,1,1)
p5 = a.vector3d(1,0,0)
p6 = a.vector3d(1,0,1)
p7 = a.vector3d(1,1,0)
p8 = a.vector3d(1,1,1)
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
t7 = a.triangle(p2,p8,)
t8 = a.triangle()
#top
t9 = a.triangle()
t10 = a.triangle()
#bottom
t11 = a.triangle()
t12 = a.triangle()

mesh = a.mesh()

input()