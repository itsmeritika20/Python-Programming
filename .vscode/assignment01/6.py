#Given the coordinates (x, y) of center of a circle and its radius, write 
#a program that will determine whether a point lies inside the circle, 
#on the circle or outside the circle.

def point(x,y,r,p,q):
    dist = float((p-x)*(p-x) + (q-y)*(q-y))
    
    if (dist>=r*r):
       print("Point lies outside the circle")
    elif (dist<=r*r):
        print("Point lies inside the circle")
    elif (dist==r*r):
        print("Point lies on the boundary of the circle")
    else:
        print("Invalid input")

x = 0
y = 0
r = 0
p = 6
q = 8
point(x,y,r,p,q)
