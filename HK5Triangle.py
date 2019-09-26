"""Bella Manoim's HW 05: Updated Triangle Classification

"""

import unittest
#from __builtin__ import False

    
greeting = 'Hello, this program will determine classify triangles based on the 3 side values.'

print(greeting)

triangleType = ''

def classify_triangle(a, b, c):
	triangleType = ''
	
	#check inputs are integers
	if not(isinstance(a,int) or isinstance(b,int) or isinstance(c,int)):
		triangleType = 'This is not a valid triangle'
        
	# input must be > 0 and < 200
	if a <= 0 or b <= 0 or c <= 0:
		triangleType = 'This is not a valid triangle'
	# input must be > 0 and < 200
	elif a > 200 or b > 200 or c > 200:
		triangleType = 'This is not a valid triangle'
	elif a == b  and b == c:
		triangleType = 'This is an equilateral triangle'
	elif (a == b and b != c) or (a == c and b != c) or (b == c and b != a):
		triangleType = 'This is an isosceles triangle'
	elif (a != b) and (a != c) and (b != c):
		triangleType = 'This is a scalene triangle'
	if ((a * a) + (b * b)) == (c * c):
		triangleType = triangleType + ' and right triangle'
	elif ((b * b) + (c * c)) == (a * a):
		triangleType = triangleType + ' and right triangle'
	elif ((c * c) + (a * a)) == (b * b):
		triangleType = triangleType + ' and right triangle'

	#check if it is a valid triangle
	#the sum of any two sides must be strictly less than the third side
	if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
		triangleType = 'This is not a valid triangle'
	
	print (triangleType)
	return triangleType

try:
	classify_triangle(2, 2, 3) #isosceles
	classify_triangle(2, 3, 3) #isosceles
	classify_triangle(5, 2, 5) #isosceles
	classify_triangle(-5, 2, 5) #not valid triangle
	classify_triangle(3, 4, 5) #scalene and right
	classify_triangle(5, 4, 3) #scalene and right
	classify_triangle(4, 3, 5) #scalene and right
	classify_triangle(4, 2, 3) #scalene
	classify_triangle(2, 2, 2) #equilateral
	classify_triangle(5, 12, 13) #scalene and right
	classify_triangle(5, 5, 5) #equilateral
	classify_triangle(-5, -5, -5) #not valid triangle
	classify_triangle(0, 0, 0) #not valid triangle
	        
except:
	print ('Invalid values. Please run program again.')
    
class TestTriangles(unittest.TestCase):
	def testEquilateral(self):
		self.assertEqual(classify_triangle(6, 6, 6), 'This is an equilateral triangle')
		self.assertEqual(classify_triangle(8, 8, 8), 'This is an equilateral triangle')
    
	def testIsoceles(self): 
		self.assertEqual(classify_triangle(2, 2, 3),'This is an isosceles triangle')
		self.assertEqual(classify_triangle(2, 3, 2),'This is an isosceles triangle')
		self.assertEqual(classify_triangle(3, 2, 2),'This is an isosceles triangle')
		
	def testScalene(self):
		self.assertEqual(classify_triangle(7, 4, 10), 'This is a scalene triangle')
		self.assertEqual(classify_triangle(10, 7, 4), 'This is a scalene triangle')
    
	def testScaleneRight(self): 
		self.assertEqual(classify_triangle(3, 4, 5), 'This is a scalene triangle and right triangle')
		self.assertEqual(classify_triangle(5, 4, 3), 'This is a scalene triangle and right triangle')
		self.assertEqual(classify_triangle(5, 3, 4), 'This is a scalene triangle and right triangle')
				
	def testWrongInput(self):
		self.assertEqual(classify_triangle(-3, 8, 8), 'This is an invalid triangle')
		self.assertEqual(classify_triangle(4, 2, 2), 'This is not a triangle')
		
