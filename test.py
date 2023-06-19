from vpython import *

scene = canvas()
Box = box(length=0.25, width=10, height=5, color=color.blue, pos=vector(-8.5, 0, 0))
pointer_x = arrow(pos=vector(-8.375, 0, 0), axis=vector(1, 0, 0), color=color.blue)
pointer_y = arrow(pos=vector(-8.375, 0, 0), axis=vector(0, 1, 0), color=color.red)
pointer_z = arrow(pos=vector(-8.375, 0, 0), axis=vector(0, 0, 1), color=color.white)

Triger = cylinder(pos=vector(-8.5, 0, -2.5), color=color.white, length=1.5)
Echo = cylinder(pos=vector(-8.5, 0, +2.5), color=color.white, length=1.5)
