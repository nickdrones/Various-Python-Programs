from Tkinter import *
from FractalClass import *

class myFractalCode(Canvas):
        def __init__(self,parent):
                Canvas.__init__(self,parent,bg = "white")
                self.pack(fill=BOTH, expand=1)
                self.dimensions={}
                self.dimensions["width"] = WIDTH
                self.dimensions["height"] = HEIGHT #init dimensions of canvas
                self.dimensions["min_x"] = 5
                self.dimensions["max_x"] = self.dimensions["width"]-5
                self.dimensions["min_y"] = 5
                self.dimensions["max_y"] = self.dimensions["width"]-5
                self.dimensions["mid_x"] = (self.dimensions["min_x"]+ self.dimensions["max_x"])/2
                self.dimensions["mid_y"] = (self.dimensions["min_y"]+ self.dimensions["max_y"])/2

                self.vertex_radius = 2
                self.vertex_color = "red"

                self.point_radius = 0
                self.point_color = "black"
        def make(self, f):
                if(f=="SierpinskiTriangle"): #determine fractal to create
                        fractal = SierpinskiTriangle(self.dimensions)
                elif(f=="SierpinskiCarpet"):
                        fractal = SierpinskiCarpet(self.dimensions)
                elif(f=="Pentagon"):
                        fractal = Pentagon(self.dimensions)
                elif(f=="Hexagon"):
                        fractal = Hexagon(self.dimensions)
                elif(f=="Octagon"):
                        fractal = Octagon(self.dimensions)

                print "Generating: {}".format(f)
                for v in fractal.vertices: #draw vertices
                        self.plot(v, self.vertex_color, self.vertex_radius)

                tempPoint=Point(300,260) #Starting point is exact center of canvas
                for p in range(fractal.num_points):
                        whichOne=randint(0,len(fractal.vertices)-1) #pick one of the three directions from the center
                        tempPoint=Point.interpt(tempPoint,fractal.vertices[whichOne], fractal.r) #Make the new starting point the required midpoint
                        self.plot(tempPoint, "black", 1) #Plot midpoint small and black
                        
        def plot(self,point,color,radius): #this function plots a standard midpoint
                self.create_oval(point.x, point.y, point.x+radius*2, point.y+radius*2, outline=color, fill=color)



# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520
# the implemented fractals
FRACTALS = [ "SierpinskiTriangle", "SierpinskiCarpet", "Pentagon", "Hexagon", "Octagon" ]
# create the fractals in individual (sequential) windows
for f in FRACTALS:
        window = Tk()
        window.geometry("{}x{}".format(WIDTH, HEIGHT))
        window.title("Fractals Galore!!!")
        # create the game as a Tkinter canvas inside the window
        s = myFractalCode(window)
        # make the current fractal
        s.make(f)
        # wait for the window to close
        window.mainloop()
