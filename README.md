# ascii-graphics


__Note__ to check the code goto [src/asciianim.py](src/asciianim.py) on running code goes into full screen u can get out of the full screen by pressing f11

__this is only available for windows operating systems right now__
(best used on windows 10)(could work on other operating systems -   not tested)

we need to configure our command prompt to show us square texts or else
program will give us a wroped in y direction result to do this 
*__open command prompt__
*__right click on top and goto defaults__
*__goto fonts and select _Raster Fonts_ and of font size 8*8 and save it__ 
(take a note of your previous settings cause its highly probabable that you wont like this font

install the software by using
__python -m pip install asciigraphics__ or in some systems
__py -m pip install asciigraphics__ or 
__pip install asciigraphics__ 


## Usage :

__Note:__
__*variable*__ implies it has a default vaule

create a new python file

then first we need to import the module
__import asciigraphics as a__

then we need to create canvas we can do that with function
__a.createcanvas()__
this creates a full screen canvas if u want to edit size and fulscreeness the arguments are
__a.createcanvas(*width,height,bool_fullscreen*)__

__a.draw()__  updates the screen
__a.clearbg()__ clear the screen

### 2d

__a.point(x,y,*color,intensity*)__ places a point with given color and intensity at a given position

__Note :__
intensity ranges from 0 to 68 int values
color ranges from [0,0] to [15,15] int array values

__a.line_2d(x1,y1,x2,y2,*color,intensity,key*)__ draws a line for given points,if key is set to true updates after drawing the 
line automatically if set to false we need to update it manually usefull for speed when u draw multiple lines u can update all of them at once

__a.rect_2d(x1,y1,width,height,*color,intensity,key*)__ draws a rectangle with given width and height @ position x,y

__a.ellipse_2d(xc, yc,rx, ry,*color,intensity,key*)__ draws a ellipse at xc,yc with radius rx,ry

__a.arc_2d(x,y,r,a,*color,intensity,key*)__ draws an arc

__a.scale_2d(s,*color,intensity,key*)__ scales the whole 2d space

__a.transform_2d(x,y,*color,intensity,key*)__ transform the whole 2d space

__a.rotate_at_2d(x,y,a,*color,intensity,key*)__ rotates the whole 2d space

__a.fill(x,y,Nc,*fillc,intensity,key,Pc*)__ Nc is boder color and fillc is the fillcolor

__a.text(x,y,string,*color,key*)__ puts a text at given location with warping


### 3d

make a 3d object in blender export it as an obj file and while exporting only tick the option triangulate faces and untick anything else to make sure this can import it 

to import the obj file u can use the the function

__obj = a.import_obj("*(file location)*..../objfile.obj")__

u can draw this object with the function

__a.Draw_Object(obj,*at,showmesh,fillkey,key,light,camera*)__

this will draw the object at distance __at__ if showmesh is set to true it will showmesh and fillkey is set to true it will 
fill the mesh 

__Note :__ here light and camera are of type vector3d created a by dataclass ie to change the light direction make a variable 
__l = a.vector3d((float),(float),(float))__

and hence this will draw the object

to rotate the points array we have function

__a.rxa(angle,points)__
__a.rya(angle,points)__
__a.rza(angle,points)__

to rotate points in obj variable

__p = obj.p__
__rxa(angle,p)__ or __a.rya(angle,p)__ or __a.rza(angle,p)__
__obj.p = p__

this will rotate points by a given angle




