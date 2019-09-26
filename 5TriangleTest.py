"""Bella Manoim's HW 05: Updated Triangle Classification
   Unit Test
"""

import unittest
from HK5Triangle import classify_triangle

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
		self.assertEqual(classify_triangle(-3, 8, 8), 'This is not a valid triangle')
		self.assertEqual(classify_triangle(4, 2, 2), 'This is not a valid triangle')
		self.assertEqual(classify_triangle(2.5, 3, 3.2), 'This is not a valid triangle')
		self.assertEqual(classify_triangle(300, 300, 300), 'This is not a valid triangle')		
