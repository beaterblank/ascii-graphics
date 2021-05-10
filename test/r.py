import asciianim as a
a.createcanvas(100,100)
obj = a.import_obj("sphere.obj")
while True:
    p = obj.p
    a.rxa(0.02,p)
    obj.p = p
    a.Draw_Object(obj,False,True)
    a.draw()
    a.clearbg()

input()


    
