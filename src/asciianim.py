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

#a function to clear screen after every frame using lambda to map cls from os into clear
clear = lambda:os.system('cls')
clear()

#chars array raging from least visible to most visible parts
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI:,\"^`'. "
char = list(chars)

#initializing output varible
output=[]

#function to create a canvas
def createcanvas(width,height):
    cursor.hide() 
    #seting the size of command prompt
    os.system('mode con: cols='+str(int(width))+' lines='+str(int(height)))
    #instantiating the 2d matrix
    rows, cols = (width, int(height))
    for i in range(cols): 
        col = [] 
        for j in range(rows): 
            col.append(" ") 
        output.append(col)
    #clearing whatever is on the screen 
    clear()




    
#----------------------------------------------------------------------#
#-----------------------2d_drawing_functions---------------------------#
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#a function to add a pixel at a certain point
def pointat(x,y,z=0):
    if(y>=0 and x>=0 and x<len(output[0]) and y<len(output)):
        try:
            v = char[round(z)]
        except(IndexError,ValueError):
            v = " "
        output[y][x] = v
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#a function to draw line
def line_2d(x1,y1,x2,y2,z=0,key=True):
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
    for i in range(steps):
        pointat(round(x),round(y),z)
        x = x+Xinc
        y = y+Yinc
    #if we dont wanna draw the the line as soon as it computes the points
    if(key):
        draw()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#drawing a rectangle is just 4 lines and instead of drawing 4 times we can draw just once 
def rect_2d(x1,y1,width,height,z=0,key=True):
    line_2d(x1,y1,x1+width,y1,z,False)
    line_2d(x1,y1,x1,y1+height,z,False)
    line_2d(x1+width,y1,x1+width,y1+height+1,z,False)
    line_2d(x1,y1+height,x1+width,y1+height,z,False)
    if(key):
        draw()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#        
#function to draw the ellipse by midpoint algorithim       
def ellipse_2d(rx, ry, xc, yc,z=0,key=True):  
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
        pointat(j[0],j[1],z)
    if(key):
        draw()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#function to draw an arc by rotating point 0.1 radians
def arc(x,y,r,a,z=0,key=True):
    drawing= True
    i=0
    while(drawing):
        if(i>=a):
            drawing= False
        pointat(round(x+r*math.cos(i)),round(y+r*math.sin(i)),z)
        i+=0.1  
    if(key):
        draw()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#-----------------------system_functions-------------------------------#
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#a function to print all the elements in the 2d array
def draw():
    k=1
    clear()
    for i in output:
        if(k>1):
            print()
        for j in i:
            print(j,end='')
        k+=1
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#functions to return window width and height
def width():
    return len(output)
def height():
    return len(output[0])
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#a function to clearbg which simply puts blanks into all of the 2d list
def clearbg():
    for i in range(len(output)):
        for j in range(len(output[i])):
            output[i][j]=char[0]
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#extracts all the active points and returns it
def extract():
    points=[]
    for i in range(len(output)):
        for j in range(len(output[i])):
            if(output[i][j]!=char[0]):
                points.append([i,j])
    return points
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#-------------------2d_translation_functions---------------------------#
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#function to scale the the interface
def scale(s,k=True,z=0):
    points = extract()
    clearbg()
    for i in points:
        nx = i[0]*s
        ny = i[1]*s
        pointat(round(nx),round(ny),z)
    if(k):
        draw()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#extracts the point transforms the points and adds them to the matrix
def transform_2d(x,y,z=0,key=True):
    points = extract()
    clearbg()
    for j in points:
        pointat(j[0]+x,j[1]+y,0)
    if(key):
        draw()
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#extracts the point rotates in the xy plane adds points back
def rotate_at_2d(x,y,a,z=0,key=True):
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
        pointat(k,l,z)
    if(key):
        draw()
#----------------------------------------------------------------------#
def test():
    print("working")

#----------------------------------------------------------------------#
#----------------------------------------------------------------------#
#----------------------------flood fill--------------------------------#
def floodfill(x,y,z=0):
    if(output[y][x]==" "):
        pointat(x,y,z)
        floodfill(x+1,y,z)
        floodfill(x-1,y,z)
        floodfill(x,y+1,z)
        floodfill(x,y-1,z)
#----------------------------------------------------------------------#
#----------------------------------end---------------------------------#
#----------------------------------------------------------------------#

    

