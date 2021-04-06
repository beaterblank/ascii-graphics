import asciianim as a
import time
a.createcanvas(240,135,True)
a.line_2d(10,10,30,30,[2,3])
a.rotate_at_2d(10,10,0.1,[2,3])
time.sleep(2)
a.clearbg()
input()