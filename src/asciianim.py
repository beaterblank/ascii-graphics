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
#making a projection matrix
mat=[]

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
def createcanvas(width=240,height=135):
    os.system('mode con: cols='+str(int(width))+' lines='+str(int(height)))
    #making it full screen
    pyautogui.press("f11")
    cursor.hide()
    os.system('')
    rows, cols = (width,height)
    for i in range(cols): 
        col = [] 
        for j in range(rows): 
            col.append(["\u001b[0m"," "]) 
        output.append(col)

    #3d###
    for i in range(4): 
        col = [] 
        for j in range(4): 
            col.append(0.0) 
        mat.append(col)
    near = 0.1
    far = 1000
    fov = 90
    aspectratio = aspect()
    fovrad = 1/math.tan(fov*0.5/180*math.pi)
    mat[0][0] = aspectratio*fovrad
    mat[1][1] = fovrad
    mat[2][2] = far/(far-near)  
    mat[3][2] = -far*near/(far-near)
    mat[2][3] = 1.0
    
#----------------------------------------------------------------------#
#-----------------------system_functions-------------------------------#
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#a function to print all the elements in the 2d array

#----------------------------------------------------------------------#
def draw():
    k=1
    clear()
    for i in output:
        if(k>1):
            print()
        for j in i:
            print(j[0]+j[1],end='')
        k+=1
#----------------------------------------------------------------------#
#a function to clearbg which simply puts blanks into all of the 2d list
def clearbg():
    for i in range(len(output)):
        for j in range(len(output[i])):
            output[i][j][1]=" "
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#extracts all the active points and returns it
def extract():
    points=[]
    for i in range(len(output)):
        for j in range(len(output[i])):
            if(output[i][j][1]!=" "):
                points.append([i,j])
    return points

#----------------------------------------------------------------------#
def in_range(x,y):
    if(y<0 or y>len(output) or x<0 or x>len(output[0])):
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
def line_2d(x1,y1,x2,y2,color=[0,0],intensity=0,key=True):
    #finding change in x and y
    dx = x2-x1
    dy = y2-y1
    #setting the starting points
    x = x1
    y = y1
    #computing which direction has grater number of steps and and how many
    steps  = abs(dx) if(abs(dx)>abs(dy)) else abs(dy)
    #dividing the change by steps to increase then on every iteration
    Xinc = dx/steps
    Yinc = dy/steps
    #increasing that much every steps for all the steps
    for i in range(steps+1):
        point(round(x),round(y),color,intensity)
        x = x+Xinc
        y = y+Yinc
    #if we dont wanna draw the the line as soon as it computes the points
    if(key):
        draw()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#drawing a rectangle is just 4 lines and instead of drawing 4 times we can draw just once 
def rect_2d(x1,y1,width,height,color=[0,0],intensity=0,key=True):
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
        point(round(x+r*math.cos(i)),round(y+r*math.sin(i)),color,intensity)
        i+=0.1  
    if(key):
        draw()
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
        point(round(nx),round(ny),color,intensity)
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
        k = round(n*math.sin(a)+m*math.cos(a))
        l = round(n*math.cos(a)-m*math.sin(a))
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
        #gotta rewrite floodfill
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

#we render 3d objects by meshes meshes are just collection of triangles in 3d space projected on to a 2d plane
#we calculate intensity   

import math
from dataclasses import dataclass

@dataclass
class vector3d:
    x:float
    y:float
    z:float

@dataclass
class intvector2d:
    x:int
    y:int

@dataclass
class triangle:
    a:vector3d
    b:vector3d
    c:vector3d

@dataclass
class mesh:
    k:list[triangle]

def filledtriangle(a,b,c,intensity,key=False):
    line_2d(a.x,a.y,b.x,b.y,intensity,False)
    line_2d(b.x,b.y,c.x,c.y,intensity,False)
    line_2d(a.x,a.y,c.x,c.y,intensity,False)
    centeroid = intvector2d(round((a.x+b.x+c.x)/3),round((a.y+b.y+c.y)/3))
    fill(centeroid.x,centeroid.y,intensity,False)
    if(key):
        draw()

def mulvecmat(i,m):
    o = vector3d(0,0,0)
    o.x = i.x*m[0][0]+i.y*m[1][0]+i.z*m[2][0]+m[3][0]
    o.y = i.x*m[0][1]+i.y*m[1][1]+i.z*m[2][0]+m[3][1]
    o.z = i.x*m[0][2]+i.y*m[1][2]+i.z*m[2][0]+m[3][2]
    w   = i.x*m[0][3]+i.y*m[1][3]+i.z*m[2][0]+m[3][3]
    if(w!=0):
        o.x = o.x/w
        o.y = o.y/w
        o.z = o.z/w
