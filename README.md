# ascii-graphics


__Note__ to check the code goto [src/asciianim.py](src/asciianim.py) on running code goes into full screen u can get out of the full screen by pressing f11

__this is only available for windows operating systems right now__
(best used on windows 10)

we need to configure our command prompt to show us square texts or else
 program will give us a wroped in y direction result to do this 
*__open command prompt__
*__right click on top and goto defaults__(as shown below)

![right_click_image](/images/click.png)

*__goto fonts and select _Raster Fonts_ and of font size 8*8 and save it__ (as shown below)(take a note of your previous settings cause its highly probabable that ypu wont like this font)

![fontsize](/images/size.png)


install the software by using

__python -m pip install asciigraphics__(i didnot publish this yet after publishing this command will work)
(for now to set it up u will need wheel library so install it first by python -m pip install wheel then downlad my files from github then use command *python setup.py bdist_wheel* followed by *python -m pip install -e .* to install this locally)

import the 2d graphics and animation module by using the command

 __import asciianim as a__
 
 (could use asciianim itself but for the sake of simplicity imported as a)
 
>after importing we need to create a canvas to work on to do that
>>__a.createcanvas(_width_,_height_)__

(note that asciianim is imported as a and width and height are any positive
integers best results are produced when range of them is in between 50 to 200)
now you can use any of the follwing ways to draw on this 2d space

## __a.pointat(x,y,[z])__ 
>u can place a point on 3d space here z = 0 by default
>as u u go father away the less visible ascii charecter will be printed at that place

## __a.line_2d(x1,y1,x2,y2,[z],[key])__ 
>u can draw a line on 3d space on plane z 
>here z = 0 by default also the key is a boolean varible set to true which
>updates the screen when set to true and does not when did not set to true
>the function __draw()__ can beused to update the the screen delayed cause when 
>we are running our code on a loop and we have many line() its wise to update
>screen one instead of updating it every time line() is called
>as u u go father away the less visible ascii charecter will be printed at that place
eg

![line](images/line_2d.png)

## __a.rect_2d(x,y,w,h,[z],[key])__ 
>u can draw a rectangle on 3d space on plane z here z=0 by default also key can be used as mentioned above

![rect](images/rect.png)

## __a.ellipse_2d(rx, ry, xc, yc,[z],[key])__
>u can draw an ellipse at _xc,yc_ and with _rx,ry_ axis lengths _note for a circle rx = ry_ z and key work as mentioned above

![ellipse](images/ellipse.png)

## __a.arc_2d(x,y,r,a,z=0,key=True)__ 
>u can make an arc with center at _x,y_ and with radius _r_ and for angle a z and key work as mentioned above

![arc](images/arc.png)

## __a.fill(x,y,z)__
>flood fills from the co-ordinates given and z represents the the plane its filling in it can be used to manipulate the transpiracy the higher the z the father away the plane will be as less traspirent the fill will be

![floodfill](images/floodfill.png)

## __a.text(x,y,string)__
>places the text at the specified location

![text](images/text.png)

##__transform_2d(x,y,intensity=0,key=True)__ translates origin to given coordinate
##__a.scale_2d(s,key=True,intensity=0)__ scales the space
##__rotate_at_2d(x,y,a,intensity=0,key=True)__ rotates the space at x,y by an angle a
