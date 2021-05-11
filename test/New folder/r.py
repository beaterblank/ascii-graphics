import asciianim as a
a.createcanvas()
obj = a.import_obj("VideoShip.obj")
while True:
    p = obj.p
    a.rza(0.03,p)
    obj.p = p
    a.Draw_Object(obj,2,True,False)
    a.draw()
    a.clearbg()

input()


    
