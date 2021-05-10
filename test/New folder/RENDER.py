import asciianim as a
import time
a.createcanvas()
p = []

p.append(a.vector3d(0,0,0))
p.append(a.vector3d(0,0,1))
p.append(a.vector3d(0,1,0))
p.append(a.vector3d(0,1,1))
p.append(a.vector3d(1,0,0))
p.append(a.vector3d(1,0,1))
p.append(a.vector3d(1,1,0))
p.append(a.vector3d(1,1,1))



while(True):
    mesh = []
    
    mesh.append(a.triangle(p[0],p[2],p[6]))
    mesh.append(a.triangle(p[0],p[6],p[4]))
    mesh.append(a.triangle(p[4],p[6],p[7]))
    mesh.append(a.triangle(p[4],p[7],p[5]))
    mesh.append(a.triangle(p[5],p[7],p[3]))
    mesh.append(a.triangle(p[5],p[3],p[1]))
    mesh.append(a.triangle(p[1],p[3],p[2]))
    mesh.append(a.triangle(p[1],p[2],p[0]))
    mesh.append(a.triangle(p[2],p[3],p[7]))
    mesh.append(a.triangle(p[2],p[7],p[6]))
    mesh.append(a.triangle(p[5],p[1],p[0]))
    mesh.append(a.triangle(p[5],p[0],p[4]))

    for i in range(len(mesh)):
        a.triangle_3d(mesh[i],True)
    a.rxa(0.2,p)
    a.rza(0.2,p)

    a.draw()
    a.clearbg()
    time.sleep(0.05)
    
