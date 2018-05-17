import collections
import random
import turtle
import time

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def info(self):
        return (self.x, self.y)
    
    def line(self, o):

        if o == "V":
            TURTLE.goto(self.x, self.y+LINE_LENGTH)
            TURTLE.pendown()
            TURTLE.goto(self.x, self.y-LINE_LENGTH)
            TURTLE.penup()

            return ((Point(self.x, self.y+LINE_LENGTH), "H"),\
                    (Point(self.x, self.y-LINE_LENGTH), "H"),)

        else:
            TURTLE.goto(self.x+LINE_LENGTH, self.y)
            TURTLE.pendown()
            TURTLE.goto(self.x-LINE_LENGTH, self.y)
            TURTLE.penup()

            return ((Point(self.x+LINE_LENGTH, self.y), "V"),\
                    (Point(self.x-LINE_LENGTH, self.y), "V"),)
        

TURTLE      = turtle.Turtle()
WINDOW      = turtle.Screen()
LINE_LENGTH = 2
START       = [(Point(0,0), "V")]
END         = collections.defaultdict(int)

RANDOMIZE   = False
CLEAN       = True
DENSITY     = (1, 10)
VARIANCE    = (0, 9)

TURTLE.setheading(90)
TURTLE.hideturtle()
TURTLE.speed(0)
TURTLE.penup()

if RANDOMIZE:
    if CLEAN:
        START = []
        
    for _ in range(random.randint(*DENSITY)):
        START.append((Point(random.randint(*VARIANCE)*LINE_LENGTH ,\
                            random.randint(*VARIANCE)*LINE_LENGTH),\
                            random.choice(["V", "H"])       ,))
        
while True:
    generation = []
    
    for _ in range(len(START)):
        point, orientation = START.pop(0)
        #END[point.info()] += 1
        L1, L2 = point.line(orientation)
        generation.append(L1)
        generation.append(L2)

    for point, orientation in generation:
        END[point.info()] += 1

    for line in generation:
        if END[line[0].info()] < 2:
            START.append(line)
