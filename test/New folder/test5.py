import asciianim as a
a.createcanvas(100,100,True)
p1 = a.vector3d(10,10,1)
p2 = a.vector3d(80,80,1)
p3 = a.vector3d(80,10,1)
tri = a.triangle(p1,p2,p3)
centroid = a.vector3d(round((p1.x+p2.x+p3.x)/3),round((p1.y+p2.y+p3.y)/3),round((p1.z+p2.z+p3.z)/3))
a.fillmesh(tri,centroid,[10,10],10,True)
input()
