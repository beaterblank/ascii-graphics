#version control : 1.0

#status : under testing

#usage:
#   to make a canvas
#   to draw 2d shapes
#   to use 2d translation

#working:
#   makes use of a matrix(2d list) to print pixels ie each pixel
#   can be accessed by using say pixels is the matrix pixels[y][x]
#   points to the pixel at x y position
#   we first make a matix with all empty space elements,then at any
#   point we like to mark we just insert some charecter to the list
#   as mentioned above

#importing required variables
import sys
import os
import math
import cursor
import pyautogui
import re
import numpy as np
from dataclasses import dataclass

sys.setrecursionlimit(1600)
np.seterr(divide='ignore', invalid='ignore')
#a function to clear output after every frame using lambda to map cls from os into clear
clear = lambda:os.system('cls')

#chars array raging from least visible to most visible parts
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI:,\"^`'. "
char = list(chars)
#initializing output varible
output=[]

#----------------------------------------------------------------------#
#functions to return window width and height
def width():
    return len(output[0])
def height():
    return len(output)
def aspect():
    return height()/width()
#----------------------------------------------------------------------#

#function to create a canvas
def createcanvas(width=round(pyautogui.size()[0]/8),height=round(pyautogui.size()[1]/8),fullscreen=True):
    os.system('mode con: cols='+str(int(width))+' lines='+str(int(height)))
    #making it full screen
    if(fullscreen):
        pyautogui.press("f11")
    cursor.hide()
    os.system('')
    clear()
    rows, cols = (width,height)
    for i in range(cols): 
        col = [] 
        for j in range(rows): 
            col.append(["\u001b[0m"," "]) 
        output.append(col)

    
#----------------------------------------------------------------------#
#-----------------------system_functions-------------------------------#
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#a function to clearbg which simply puts blanks into all of the 2d list
#----------------------------------------------------------------------#
def clearbg():
    points=extract()
    for j in points:
        x=j[0]
        y=j[1]
        output[x][y][1]=" "
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#extracts all the active points and returns it
#----------------------------------------------------------------------#
def extract():
    points=[]
    for i in range(len(output)):
        for j in range(len(output[i])):
            if(output[i][j][1]!=" "):
                points.append([i,j,output[i][j][0],output[i][j][1]])
    return points
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#a function to print all the elements in the 2d array
#----------------------------------------------------------------------#
def draw():
    points = extract()
    clear()
    string=''
    for j in points:
        x=j[0]
        y=j[1]
        text=output[x][y][0]+output[x][y][1]
        string+=f"\x1b7\x1b[{x+1};{y+1}f{text}\x1b8"
    sys.stdout.write(string)
    sys.stdout.flush()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#a function to check if the given point is in
#----------------------------------------------------------------------#
def in_range(x,y):
    if(y<0 or y>=len(output) or x<0 or x>=len(output[0])):
        return False
    return True
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#a function to return color at the given location
#----------------------------------------------------------------------#
def colorat(x,y):
    return int(str(re.search("\d+m",output[y][x][0])[0])[:-1])
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#-----------------------2d_drawing_functions---------------------------#
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#a function to add a pixel at a certain point
#----------------------------------------------------------------------#
def point(x,y,color,intensity=0):
    x=round(x)
    y=round(y)
    if(in_range(x,y)):
        color[0] = color[0] if(color[0]<16 and color[0]>=0) else 16
        color[1] = color[1] if(color[1]<16 and color[1]>=0) else 16
        intensity = intensity if(intensity<=69 and intensity>=0) else 69
        code = color[0]*16+color[1]
        ansi = "\u001b[38;5;"+str(code)+"m"
        output[y][x]=[ansi,char[intensity]]
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#a function to draw line
#----------------------------------------------------------------------#
def line_2d(x1,y1,x2,y2,color=[0,0],intensity=0,key=True):
    #finding change in x and y
    dx = x2-x1
    dy = y2-y1
    #setting the starting points
    x = x1
    y = y1
    #computing which direction has grater number of steps and and how many
    steps  = round(abs(dx) if(abs(dx)>abs(dy)) else abs(dy))
    if(steps>math.sqrt(width()*width()+height()*height())):
        steps = round(math.sqrt(width()*width()+height()*height()))
    #dividing the change by steps to increase then on every iteration
    if(steps>0):
        Xinc = dx/steps
        Yinc = dy/steps
        #increasing that much every steps for all the steps
        for i in range(steps+1):
            point(x,y,color,intensity)
            x = x+Xinc
            y = y+Yinc
    #if we dont wanna draw the the line as soon as it computes the points
    if(key):
        draw()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#drawing a rectangle is just 4 lines and instead of drawing 4 times we 
#can draw just once
#----------------------------------------------------------------------# 
def rect_2d(x1,y1,width,height,color=[5,5],intensity=0,key=True):
    line_2d(x1,y1,x1+width,y1,color,intensity,False)
    line_2d(x1,y1,x1,y1+height,color,intensity,False)
    line_2d(x1+width,y1,x1+width,y1+height,color,intensity,False)
    line_2d(x1,y1+height,x1+width,y1+height,color,intensity,False)
    if(key):
        draw()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#        
#function to draw the ellipse by midpoint algorithim 
#----------------------------------------------------------------------#      
def ellipse_2d(xc, yc,rx, ry,color=[0,0],intensity=0,key=True):  
    points=[]
    x = 0 
    y = ry  
    # Initial decision parameter of region 1  
    d1 = ((ry * ry) - (rx * rx * ry) +(0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y  
    # For region 1  
    while (dx < dy):  
        points.append([x+xc,y+yc])
        points.append([-x+xc,y+yc])
        points.append([x+xc,-y+yc])
        points.append([-x+xc,-y+yc])
        # Checking and updating value of  
        # decision parameter based on algorithm  
        if (d1 < 0):  
            x += 1  
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)  
        else: 
            x += 1 
            y -= 1  
            dx = dx + (2 * ry * ry)  
            dy = dy - (2 * rx * rx)  
            d1 = d1 + dx - dy + (ry * ry)  
    # Decision parameter of region 2  
    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) - 
           (rx * rx * ry * ry))  
    # Plotting points of region 2  
    while (y >= 0): 
        points.append([x+xc,y+yc])
        points.append([-x+xc,y+yc])
        points.append([x+xc,-y+yc])
        points.append([-x+xc,-y+yc])
        # Checking and updating parameter  
        # value based on algorithm  
        if (d2 > 0): 
            y -= 1  
            dy = dy - (2 * rx * rx)  
            d2 = d2 + (rx * rx) - dy  
        else: 
            y -= 1  
            x += 1  
            dx = dx + (2 * ry * ry)  
            dy = dy - (2 * rx * rx)  
            d2 = d2 + dx - dy + (rx * rx)
    for j in points:
        point(j[0],j[1],color,intensity)
    if(key):
        draw()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#function to draw an arc by rotating point 0.1 radians
#----------------------------------------------------------------------#
def arc_2d(x,y,r,a,color=[0,0],intensity=0,key=True):
    drawing= True
    i=0
    while(drawing):
        if(i>=a):
            drawing= False
        point(x+r*math.cos(i),y+r*math.sin(i),color,intensity)
        i+=0.1  
    if(key):
        draw()
#----------------------------------------------------------------------#


#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#-------------------2d_translation_functions---------------------------#
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#function to scale the the interface
#----------------------------------------------------------------------#
def scale_2d(s,color=[0,0],intensity=0,key=True):
    points = extract()
    clearbg()
    for i in points:
        nx = i[0]*s
        ny = i[1]*s
        point(nx,ny,color,intensity)
    if(key):
        draw()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#extracts the point transforms the points and adds them to the matrix
#----------------------------------------------------------------------#
def transform_2d(x,y,color=[0,0],intensity=0,key=True):
    points = extract()
    clearbg()
    for j in points:
        point(j[0]+x,j[1]+y,color,intensity)
    if(key):
        draw()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#extracts the point rotates in the xy plane adds points back
#----------------------------------------------------------------------#
def rotate_at_2d(x,y,a,color=[0,0],intensity=0,key=True):
    points = extract()
    clearbg()
    for j in points:
        m = j[0]
        n = j[1]
        m-=x
        n-=y
        k = (n*math.sin(a)+m*math.cos(a))
        l = (n*math.cos(a)-m*math.sin(a))
        k+=x
        l+=y
        point(k,l,color,intensity)
    if(key):
        draw()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#clipping alogrithims
#----------------------------------------------------------------------#
def Liang_Barsky(x1,y1,x2,y2,xmin,ymin,xmax,ymax):
    dx=x2-x1
    dy=y2-y1
    p1,p2,p3,p4 = -dx,dx,-dy,dy
    p=[p1,p2,p3,p4]
    q1,q2,q3,q4 = x1-xmin,xmax-x1,y1-ymin,ymax-y1
    q=[q1,q2,q3,q4]
    r=[0,0,0,0]
    u1=[0]
    u2=[1]
    for k in range(4):
        if((p[k]==0 and q[k]<0) ):
            return [x1,ymin,x1,ymax]
        if((p[k]==0 and q[k]>=0) ):
            return [x1,y1,x2,y2]
        r[k]=q[k]/p[k]
        if(p[k]<0):
            u1.append(r[k])
        else:
            u2.append(r[k])
    U1=max(u1)
    U2=min(u2)
    if(U1<U2):
        x_1 = x1+U1*dx
        y_1 = y1+U1*dy
        x_2 = x1+U2*dx
        y_2 = y1+U2*dy
        return [x_1,y_1,x_2,y_2]
    else:
        return [x1,y1,x2,y2]
def clipline(x1,y1,x2,y2,xmin,ymin,xmax,ymax,outcol=[3,3],incol=[2,2],bodercol=[10,10],debug=False):
    k = Liang_Barsky(x1,y1,x2,y2,xmin,ymin,xmax,ymax)
    rect_2d(xmin,ymin,xmax-xmin,ymax-ymin,bodercol,0,False)
    line_2d(x1,y1,k[0],k[1],outcol,0,False)
    line_2d(k[2],k[3],k[0],k[1],incol,0,False)
    line_2d(x2,y2,k[2],k[3],outcol,False)
def pside(xmin,ymin,xmax,ymax,p1):
    if(p1[0]==xmin):
        s1=1
    if(p1[1]==ymin):
        s1=2
    if(p1[0]==xmax):
        s1=3
    if(p1[1]==ymax):
        s1=4
def findvor(xmin,ymin,xmax,ymax,p1,p2):
    s1,s2=pside(xmin,ymin,xmax,ymax,p1),pside(xmin,ymin,xmax,ymax,p1)
    if(s1==s2):
        return p1
def clippoly(xmin,ymin,xmax,ymax,outcol,incol,bodercol,*points):
    p=[]
    f1=False
    f2=False
    ctr=0
    rect_2d(xmin,ymin,xmax-xmin,ymax-ymin,bodercol,0,False)
    for k in points:
        if(ctr==0):
            temp=k
        p.append(k)
        ctr+=1
    p.append(temp)
    for i in range(len(p)-1):
        x1=p[i][0]
        x2=p[i+1][0]
        y1=p[i][1]
        y2=p[i+1][1]
        k = Liang_Barsky(x1,y1,x2,y2,xmin,ymin,xmax,ymax)        
        if(x1==k[0] and y1==k[1] and x2==k[2] and y2 ==k[3]):
            line_2d(x1,y1,x2,y2,outcol,0,False)
        else:
            line_2d(k[0],k[1],k[2],k[3],incol,0,False)
            line_2d(x1,y1,k[0],k[1],outcol,0,False)
            line_2d(x2,y2,k[2],k[3],outcol,0,False)
    draw()
#----------------------------------------------------------------------#
#----------------------------flood fill--------------------------------#
#----------------------------------------------------------------------#
def is_valid(x,y,pc,nc):
    if(in_range(x,y)):
        if(colorat(x,y)!=pc or colorat(x,y)==nc):
            return False
    return True

def fill(x,y,Nc,fillc=[0,0],intensity=0,key=True,Pc=[0,0]):
    pc = Pc[0]*16+Pc[1]
    nc = Nc[0]*16+Nc[1]

    queue = []
    queue.append([x,y])
    point(x,y,fillc,intensity)

    while queue:
        cur_pix=queue.pop()
        px = cur_pix[0]
        py = cur_pix[1]
        if(is_valid(px+1,py,pc,nc)):
            point(px+1,py,fillc,intensity)
            queue.append([px+1,py])
        if(is_valid(px-1,py,pc,nc)):
            point(px-1,py,fillc,intensity)
            queue.append([px-1,py])
        if(is_valid(px,py+1,pc,nc)):
            point(px,py+1,fillc,intensity)
            queue.append([px,py+1])
        if(is_valid(px,py-1,pc,nc)):
            point(px,py-1,fillc,intensity)
            queue.append([px,py-1])
    if(key):
        draw()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#----------------------------------text--------------------------------#
#----------------------------------------------------------------------#

def char_at(x,y,char,color=[0,0]):
    color[0] = color[0] if(color[0]<16 and color[0]>=0) else 16
    color[1] = color[1] if(color[1]<16 and color[1]>=0) else 16
    code = color[0]*16+color[1]
    ansi = "\u001b[38;5;"+str(code)+"m"
    if(y>=0 and x>=0 and x<len(output[0]) and y<len(output)):
        output[y][x][1] = char
        output[y][x][0] = ansi

def text(x,y,string,color=[0,1],key=True):
    for char in string:
        if(x>width()):
            y+=1
            x=0
        char_at(x,y,char,color)
        x+=1
    if(key):
        draw()
#----------------------------------------------------------------------#
#----------------------------------------------------------------------#

             
#----------------------------------------------------------------------#
#----------------------------------end---------------------------------#
#----------------------------------------------------------------------#



#----------------------------------------------------------------------#
#-----------------------------3d start---------------------------------#
#----------------------------------------------------------------------#


#----------------------------------------------------------------------#
#making required data structures
#----------------------------------------------------------------------#
@dataclass
class intvector2d:
    x:int
    y:int

@dataclass
class vector3d:
    x:float
    y:float
    z:float

@dataclass
class triangle:
    a:vector3d
    b:vector3d
    c:vector3d

@dataclass
class mesh:
    k:list[triangle]

@dataclass
class index:
    a:int
    b:int
    c:int

@dataclass
class obj:
    p:list[vector3d]
    i:list[index]
#----------------------------------------------------------------------#
#debug printer for vector3d
#----------------------------------------------------------------------#
def dprin(p,e=" "):
    print([round(p.x,2),round(p.y,2),round(p.z,2)],end=e)
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#convert a point from 3d to 2d    
#----------------------------------------------------------------------#   
def to2d(ii,at = 8,near=0.1,far=1000,angle=math.pi/2):
    a = aspect()
    #transling away from us in z axis
    i = vector3d(0,0,0)
    i.x = ii.x
    i.y = ii.y
    i.z = ii.z+at
    #projection matrix
    f = 1/math.tan(angle/2)
    q = far/(far-near)
    o = vector3d(0,0,0)
    w = i.z
    o.x = a*f*i.x
    o.y = f*i.y
    o.z = (i.z*q-near*q)
    #normalizing
    if(w!=0):
        o.x /= w
        o.y /= w
        o.z /= w
    #scaling to our veiwing space
    o.x = (o.x+1)*0.5*(width()-1)
    o.y = (o.y+1)*0.5*(height()-1)
    return [o,i]
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#fill a triangle
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#main
#----------------------------------------------------------------------#
def fillmesh(tri,centeroid,fillc,intensity,key=False):
    space = []
    rows, cols = (width(),height())
    for i in range(cols): 
        col = [] 
        for j in range(rows): 
            col.append(0) 
        space.append(col)
    points=[]
    points.extend(lineforfill(round(tri.a.x),round(tri.a.y),round(tri.b.x),round(tri.b.y)))
    points.extend(lineforfill(round(tri.b.x),round(tri.b.y),round(tri.c.x),round(tri.c.y)))
    points.extend(lineforfill(round(tri.c.x),round(tri.c.y),round(tri.a.x),round(tri.a.y)))
    for item in points:
        if(item[0]<width() and item[1]<height() and item[0]>=0 and item[1]>=0):
            space[item[1]][item[0]]=1

    x = round(centeroid.x)
    y = round(centeroid.y)

    floodFill(space,width(),height(),x,y,0,1)
    for i in range(cols): 
        for j in range(rows): 
            if(space[i][j]==1):
                point(j,i,fillc,intensity)
    if(key):
        draw()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#draw the boundaries
#----------------------------------------------------------------------#
def lineforfill(x1,y1,x2,y2):
    points = []
    dx = x2-x1
    dy = y2-y1
    x = x1
    y = y1
    steps  = round(abs(dx) if(abs(dx)>abs(dy)) else abs(dy))
    if(steps>math.sqrt(width()*width()+height()*height())):
        steps = round(math.sqrt(width()*width()+height()*height()))
    if(steps>0):
        Xinc = dx/steps
        Yinc = dy/steps
        for i in range(steps+1):
            points.append([round(x),round(y)])
            x = x+Xinc
            y = y+Yinc
    return points
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#flood fill
#----------------------------------------------------------------------#
def isValid(screen, m, n, x, y, prevC, newC):
    if (x<0 or x>= m or y<0 or y>= n):
        return False
    if(screen[y][x]!= prevC or screen[y][x]== newC):
        return False
    return True
def floodFill(screen,m, n, x, y, prevC, newC):
    queue = []
    if(isValid(screen,m,n,x,y,prevC,newC)):
        queue.append([x, y])
        screen[y][x] = newC
    while queue:
        currPixel = queue.pop()
        posX = currPixel[0]
        posY = currPixel[1]
        if isValid(screen, m, n,posX + 1, posY,prevC, newC):
            screen[posY][posX+1] = newC
            queue.append([posX + 1, posY])
        if isValid(screen, m, n,posX-1, posY,  prevC, newC):
            screen[posY][posX-1]= newC
            queue.append([posX-1, posY])
        if isValid(screen, m, n,posX, posY + 1,prevC, newC):
            screen[posY + 1][posX]= newC
            queue.append([posX, posY + 1])
        if isValid(screen, m, n,  posX, posY-1,prevC, newC):
            screen[posY-1][posX]= newC
            queue.append([posX, posY-1])
    filled = True
    for i in range(len(screen)):
        for j in range(len(screen[i])):
            if(screen[i][j]==prevC):
                filled = False
    if(filled):
        for i in range(len(screen)):
            for j in range(len(screen[i])):
                screen[i][j]=prevC
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#draw a mesh
#----------------------------------------------------------------------#
def triangle_3d(tri,at,showmesh=True,fillkey=False,mc=[1,1],fc=[10,10],key=False,light=vector3d(0.5,0.5,0.5),camera=vector3d(0,0,0)):
    #we convert the 3d triangle into 2d triangle
    a=to2d(tri.a,at)[0]
    b=to2d(tri.b,at)[0]
    c=to2d(tri.c,at)[0]
    d=to2d(tri.a,at)[1]
    e=to2d(tri.b,at)[1]
    f=to2d(tri.c,at)[1]

    #calculating normal
    l1 = vector3d(0,0,0)
    l1.x  = e.x - d.x
    l1.y  = e.y - d.y
    l1.z  = e.z - d.z
    l2 = vector3d(0,0,0)
    l2.x  = f.x - d.x
    l2.y  = f.y - d.y
    l2.z  = f.z - d.z
    normal = vector3d(0,0,0)
    normal.x = l1.y*l2.z-l1.z*l2.y
    normal.y = l1.z*l2.x-l1.x*l2.z
    normal.z = l1.x*l2.y-l1.y*l2.x

    #calculating centroid of the triangle
    centeroid = vector3d(round((a.x+b.x+c.x)/3),round((a.y+b.y+c.y)/3),round((a.z+b.z+c.z)/3))
    #make a new triangle
    newtri = triangle(a,b,c)
    
    #normalizing normal and deciding if to render the triangle
    n = np.array([normal.x,normal.y,normal.z])
    l = np.array([light.x,light.y,light.z])
    d = np.array([d.x-camera.x,d.y-camera.y,d.z-camera.z])
    n = n/np.linalg.norm(n)
    l = l/np.linalg.norm(l)
    d = d/np.linalg.norm(d)
    if(n[0]*d[0]+n[1]*d[1]+n[2]*d[2]<0):
        intensity=round((n.dot(l)+1)*34)
        if(fillkey):
            fillmesh(newtri,centeroid,fc,intensity,False)
        if(showmesh):
            line_2d(a.x,a.y,b.x,b.y,mc,0,False)
            line_2d(b.x,b.y,c.x,c.y,mc,0,False)
            line_2d(a.x,a.y,c.x,c.y,mc,0,False)
    if(key):
        draw()
    return 
#----------------------------------------------------------------------#


#----------------------------------------------------------------------#
#to find the average z value in a triangle
#----------------------------------------------------------------------#
def avgz(tri):
    return (tri.a.z+tri.a.z+tri.a.z)/3
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#to sort the given mesh according to their average z values 
#                                                  - Painters algorithim
#----------------------------------------------------------------------#
def sortmesh(m):
    for i in range(0,len(m.k)):
        for j in range(i+1,len(m.k)):
            tri1 = m.k[i]
            tri2 = m.k[j]
            if(avgz(tri1)<avgz(tri2)):
                temp = m.k[i]  
                m.k[i] = m.k[j]   
                m.k[j] = temp
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#draw an entire meshes
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
def drawmesh(m,at=8,showmesh=True,fillkey=False,mc=[1,1],fc=[10,10],key=False,light=vector3d(0.5,0.5,0.5),camera=vector3d(0,0,0)):
    for i in range(len(m.k)):
        tri = m.k[i]
        triangle_3d(tri,at,showmesh,fillkey,mc,fc,key,light,camera)
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#draw an entire object
#----------------------------------------------------------------------#
#----------------------------------------------------------------------#
def Draw_Object(obj,at=8,showmesh = True,fillkey=False,mc=[1,1],fc=[10,10],key=False,light=vector3d(0.5,0.5,0.5),camera=vector3d(0,0,0)):
    me=[]
    for j in range(len(obj.i)):
        tri = triangle(obj.p[obj.i[j].a],obj.p[obj.i[j].b],obj.p[obj.i[j].c])
        me.append(tri)
    m = mesh(me)
    sortmesh(m)
    drawmesh(m,at,showmesh,fillkey,mc,fc,key,light,camera)
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#

#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#rotation algorithims
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
def rx(a,p):
    o=vector3d(0,0,0)
    o.x=p.x
    o.y=p.y*math.cos(a)-p.z*math.sin(a)
    o.z=p.y*math.sin(a)+p.z*math.cos(a)
    return o
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
def ry(a,p):
    o=vector3d(0,0,0)
    o.x=p.x*math.cos(a)+p.z*math.sin(a)
    o.y=p.y
    o.z=-p.x*math.sin(a)+p.z*math.cos(a)
    return o
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
def rz(a,p):
    o=vector3d(0,0,0)
    o.x=p.x*math.cos(a)-p.y*math.sin(a)
    o.y=p.x*math.sin(a)+p.y*math.cos(a)
    o.z=p.z
    return o
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#rotate an array of points
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
def rxa(a,p):
    for i in range(len(p)):
        p[i]=rx(a,p[i])
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
def rya(a,p):
    for i in range(len(p)):
        p[i]=ry(a,p[i])
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
def rza(a,p):
    for i in range(len(p)):
        p[i]=rz(a,p[i])
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#

#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#importing object from obj file
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
def import_obj(filename):
    id = []
    points = []
    indexes = []
    with open(filename,"r") as fi:
        for ln in fi:
            if ln.startswith("v"):
                id.append(ln[2:-1])
    for i in id:
        arr = i.split(" ")
        arr = [float(numeric_string) for numeric_string in arr]
        p = vector3d(arr[0],arr[1],arr[2])
        points.append(p)
    id=[]
    with open(filename,"r") as fi:
        for ln in fi:
            if ln.startswith("f"):
                id.append(ln[2:-1])
    for i in id:
        arr = i.split(" ")
        arr = [int(numeric_string) for numeric_string in arr]
        p = index(arr[0]-1,arr[1]-1,arr[2]-1)
        indexes.append(p)
    object_0 = obj(points,indexes)
    return object_0
#----------------------------------------------------------------------#


#----------------------------------------------------------------------#
#----------------------------------------------------------------------#
#----------------------------------------------------------------------#
#----------------------------------------------------------------------#
#----------------------------------------------------------------------#
#----------------------------------------------------------------------#
#----------------------------------------------------------------------#
