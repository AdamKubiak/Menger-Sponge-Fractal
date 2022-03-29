class Box:
    def __init__(self, x,y,z,s):
        self.x = x
        self.y = y
        self.z = z
        self.s = s
    
    def show(self):
        pushMatrix()
        translate(self.x,self.y,self.z)
        fill(255)
        noStroke()
        box(self.s)
        popMatrix()
    
    def generate(self):
        boxes = []
        for x in range(-1,2):
            for y in range(-1,2):
                for z in range(-1,2):
                    sum = abs(x)+abs(y)+abs(z)
                    newR = self.s/3
                    if sum>1:
                        b = Box(self.x+x*newR,self.y+y*newR,self.z+z*newR,newR)
                        boxes.append(b)
        return boxes            



a = 0


sponge = []
def setup():
    size(400,400,P3D)
    b = Box(0.0,0.0,0.0,200.0)
    sponge.append(b)

def mousePressed():
    global sponge
    next = []
    for b in sponge:
        newBoxes = b.generate()
        next.extend(newBoxes)
    
    sponge = next

def draw():
    global a
    background(51)
    #stroke(255)
    noFill()
    lights()
    translate(width/2,height/2)
    rotateX(a)
    rotateY(a*0.3)
    rotateZ(a*0.1)
    for i in sponge:
        i.show()
    a += 0.01
    
    
    
