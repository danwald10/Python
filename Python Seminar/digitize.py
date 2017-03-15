# -*- coding: utf-8 -*-
"""
@author: Daniel D. Hammer
Datum: 10.11.2015

Digitalisieren von Kurven

Die Koordinaten des Datenpunkten eines Diagramms, das in einer 
Bilddatei vorliegt, in physikalische Einheiten umgewandelt werden
und in einem File abgespeichert werden.
Das Programm wurde auf dem File Nel07a.png gezeigt.


Verwendung:

onecurve=1 ->eine Kurve wird digitalisiert, sonst zwei

Der erste Klick definiert den Ursprung.

Der zweite Klick definiert die Achsen
(Punkt in Einheiten angegeben, in unserem Fall ist es: x=40,y=15)

Die nächsten 10 Clicks sind Kurvenpunkte.

Falls zwei Kurven, dann noch weitere 10 Clicks digitalisieren die zweite.

File wird als "digitized_curve.png" gespeichert, wenn onecurve=1, sonst 
es heißt "digitized_curves.png".

"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def setaxes(event):
    global x2,y2
    x1.append(event.xdata-xorigin)
    y1.append(-(event.ydata-yorigin))
    if(x1[1]!=0 and y1[1]!=0):
        fig.canvas.mpl_disconnect(cid2)
        x2,y2=x1[1],y1[1]
    

def setorigin(event):
    global origin
    origin =(event.xdata, event.ydata)
    fig.canvas.mpl_disconnect(cid1)
    
def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata

    global coords
    coords.append((ix, iy))
    
    if (onecurve==0):
        global coords1
        coords1.append((ix, iy))

    if onecurve!=0 and len(coords) == 12:
        fig.canvas.mpl_disconnect(cid3)
    
    if (onecurve==0):
        if len(coords1) == 22:
            fig.canvas.mpl_disconnect(cid3)
            
              
xF=40
yF=15
x_label='Angle in Degrees'
y_label='mm'
onecurve=1

x1,y1=[],[] 
coords = []
coords1= []
origin= ()
x2,y2=5,5


fig=plt.figure()
ax = fig.add_subplot(111)
img=mpimg.imread('./Nel07a.png')
imgplot=plt.imshow(img)  

cid1=fig.canvas.mpl_connect('button_press_event', setorigin)
cid2=fig.canvas.mpl_connect('button_press_event', setaxes)     
cid3=fig.canvas.mpl_connect('button_press_event', onclick)
plt.show(1)

xorigin,yorigin=origin

kx=x2/xF
ky=y2/yF

xvals=[]
yvals=[]

if (onecurve==0):
    xvals1=[]
    yvals1=[]

for pair in coords:
    xval,yval=pair
    xvals.append((xval-xorigin)/kx)
    yvals.append((-(yval-yorigin))/ky)
if (onecurve==0):
    for pair in coords1:
        xval,yval=pair
        xvals1.append((xval-xorigin)/kx)
        yvals1.append((-(yval-yorigin))/ky)
 
for i in range(2):
    del xvals[0]
    del yvals[0]
    if (onecurve==0):
        del xvals1[0]
        del yvals1[0]

if (onecurve==0):
    for i in range(10):
        del xvals1[0]
        del yvals1[0]
        
if (onecurve==0):
    for i in range(10):
        del xvals[10]
        del yvals[10]

if (onecurve==0):
    plt.figure(1)
    plt.subplot(211)
    plt.title('1st Curve')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(xvals,yvals, marker='x', markersize=10)
    plt.subplot(212)
    plt.title('2st Curve')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(xvals1,yvals1, marker='x', markersize=10)
    plt.savefig('digitized_curves.png')
else:
    plt.figure(1)
    plt.subplot(211)
    plt.title('Curve')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(xvals,yvals, marker='x', markersize=10)
    plt.savefig('digitized_curve.png')

