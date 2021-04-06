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
import keyboard
import re

sys.setrecursionlimit(1600)

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
def createcanvas(width=240,height=135,fullscreen=False):
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
def clearbg():
    points=extract()
    for j in points:
        x=j[0]
        y=j[1]
        output[x][y][1]=" "
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#extracts all the active points and returns it
def extract():
    points=[]
    for i in range(len(output)):
        for j in range(len(output[i])):
            if(output[i][j][1]!=" "):
                points.append([i,j,output[i][j][0],output[i][j][1]])
    return points
#----------------------------------------------------------------------#
#a function to print all the elements in the 2d array

#----------------------------------------------------------------------#
def draw():
    points = extract()
    clear()
    for j in points:
        x=j[0]
        y=j[1]
        text=output[x][y][0]+output[x][y][1]
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
        sys.stdout.flush()
#----------------------------------------------------------------------#
def in_range(x,y):
    if(y<0 or y>=len(output) or x<0 or x>=len(output[0])):
        return False
    return True
#----------------------------------------------------------------------#
def colorat(x,y):
    return int(str(re.search("\d+m",output[y][x][0])[0])[:-1])

#----------------------------------------------------------------------#
#-----------------------2d_drawing_functions---------------------------#
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#a function to add a pixel at a certain point
def point(x,y,color,intensity=0):
    x=round(x)
    y=round(y)
    if(in_range(x,y)):
        color[0] = color[0] if(color[0]<16 and color[0]>=0) else 16
        color[1] = color[1] if(color[1]<16 and color[1]>=0) else 16
        intensity = intensity if(intensity<=69 and intensity>=0) else 69
        code = color[0]*16+color[1]
        ansi = "\u001b[38;5;"+str(code)+"m"
        output[y][x]=[ansi,char[0]]
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#a function to draw line
def line_2d(x1,y1,x2,y2,color=[0,0],intensity=0,key=True):
    #finding change in x and y
    dx = x2-x1
    dy = y2-y1
    #setting the starting points
    x = x1
    y = y1
    #computing which direction has grater number of steps and and how many
    steps  = round(abs(dx) if(abs(dx)>abs(dy)) else abs(dy))
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
#drawing a rectangle is just 4 lines and instead of drawing 4 times we can draw just once 
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
def transform_2d(x,y,color,intensity=0,key=True):
    points = extract()
    clearbg()
    for j in points:
        point(j[0]+x,j[1]+y,color,intensity)
    if(key):
        draw()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#extracts the point rotates in the xy plane adds points back
def rotate_at_2d(x,y,a,color,intensity=0,key=True):
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

#----------------------------------------------------------------------#
#----------------------------flood fill--------------------------------#
#----------------------------------------------------------------------#
def is_valid(x,y,pc,nc):
    if(in_range(x,y)):
        if(colorat(x,y)!=pc or colorat(x,y)==nc):
            return False
    return True

def fill(x,y,Pc,Nc,fillc,key=True):
    pc = Pc[0]*16+Pc[1]
    nc = Nc[0]*16+Nc[1]

    queue = []
    queue.append([x,y])
    point(x,y,fillc)

    while queue:
        cur_pix=queue.pop()
        px = cur_pix[0]
        py = cur_pix[1]
        if(is_valid(px+1,py,pc,nc)):
            point(px+1,py,fillc)
            queue.append([px+1,py])
        if(is_valid(px-1,py,pc,nc)):
            point(px-1,py,fillc)
            queue.append([px-1,py])
        if(is_valid(px,py+1,pc,nc)):
            point(px,py+1,fillc)
            queue.append([px,py+1])
        if(is_valid(px,py-1,pc,nc)):
            point(px,py-1,fillc)
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
#2d algorithims#
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
#----------------------------------end---------------------------------#
#----------------------------------------------------------------------#



#----------------------------------------------------------------------#
#-----------------------------3d start---------------------------------#
#----------------------------------------------------------------------#

#we render 3d objects by meshes meshes are just collection of triangles in 3d space projected on to a 2d plane
#we calculate intensity   

import math
from dataclasses import dataclass
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

def line_3d(x1,y1,z1,x2,y2,z2,color=[0,0],key=True):
    #finding change in x and y
    dx = x2-x1
    dy = y2-y1
    dz = z2-z1
    #setting the starting points
    x = x1
    y = y1
    z = z1
    #computing which direction has grater number of steps and and how many
    steps  = round(abs(dx) if(abs(dx)>abs(dy)) else abs(dy))
    #dividing the change by steps to increase then on every iteration
    if(steps>0):
        Xinc = dx/steps
        Yinc = dy/steps
        Zinc = dz/steps
        #increasing that much every steps for all the steps
        for i in range(steps+1):
            point(x,y,color,round(z))
            x = x+Xinc
            y = y+Yinc
            z = z+Zinc
    #if we dont wanna draw the the line as soon as it computes the points
    if(key):
        draw()

def triangle_3d(tri,intensity=0,key=False,fillkey=False):
    a=to2d(tri.a)
    b=to2d(tri.b)
    c=to2d(tri.c)

    line_3d(a.x,a.y,a.z,b.x,b.y,b.z,[10,10],False)
    line_3d(b.x,b.y,b.z,c.x,c.y,c.z,[10,10],False)
    line_3d(a.x,a.y,a.z,c.x,c.y,c.z,[10,10],False)

    centeroid = intvector2d(round((a.x+b.x+c.x)/3),round((a.y+b.y+c.y)/3))

    if(fillkey):
        fill(centeroid.x,centeroid.y,intensity,False)
    if(key):
        draw()
    
def to2d(i,f=100):
    w=width()
    h=height()
    x=i.x
    y=i.y
    z=i.z
    x = ((z*w)/(2*f))+x-((z*x)/(f))
    y = ((z*h)/(2*f))+y-((z*y)/(f))
    o = vector3d(x,y,z)
    return o

def rx(a,p):
    o=p
    o.y=p.y*math.cos(a)-p.z*math.sin(a)
    o.z=p.y*math.sin(a)+p.z*math.cos(a)
    return o
def ry(a,p):
    o=p
    o.x=p.x*math.cos(a)+p.z*math.sin(a)
    o.z=-p.x*math.sin(a)+p.z*math.cos(a)
    return o
def rz(a,p):
    o=p
    o.x=p.x*math.cos(a)-p.y*math.sin(a)
    o.y=p.x*math.sin(a)+p.y*math.cos(a)
    return o