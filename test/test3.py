import asciianim as a 
a.createcanvas(240,135,True)
def conv(x,y):
    o=a.intvector2d(x,y)
    o.x=p.x*240/1920
    o.y=p.y*135/1080
    return o
p1=[]
while(True):
    p=a.pyautogui.position()
    q=conv(p.x,p.y)
    a.point(round(q.x),round(q.y),[15,15])
    a.draw()
