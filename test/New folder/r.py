import asciianim as a
a.createcanvas()
obj = a.import_obj("VideoShip.obj")
while True:
    p = obj.p
    a.rya(0.3,p)
    a.rxa(0.3,p)
    obj.p = p
    a.Draw_Object(obj,6,True,True)
    a.draw()
    a.clearbg()

input()


    
