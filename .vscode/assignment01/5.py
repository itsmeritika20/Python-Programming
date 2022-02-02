#Given 3 points (x1, y1), (x2, y2) and (x3, y3) Write a program to check 
#if all the 3 points fall on straight line.
	
def collinear(x1, y1, x2, y2, x3, y3):
	m1 = ((y2-y1)/(x2-x1))
	m2 = ((y3-y1)/(x3-x1))
	if(m1 == m2):
		print("The points are fall on straight line.")
	else:
		print("The points are not fall on straight line.")

collinear(2, 4, 3, 5, 6, 8)