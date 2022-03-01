import sys
import rospy 
import rostest
import unittest
from simple_rostest.srv import AddTwoInts

class TestTwoInts(unittest.TestCase): 
	def setUp(self,):
		rospy.wait_for_service('add_two_ints')
		self.add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
	def test_add_two_ints_service(self,): 
		x = 5 
		y = 6
		resp = self.add_two_ints(x,y) 
		self.assertEqual(x+y, resp.sum)

if __name__ == "__main__": 
	rostest.run('simple_rostest', 'add_two_ints', TestTwoInts, sys.argv)
