'''
Created on Jan 26, 2014

@author: Chris
'''

import unittest
from component_register import ComponentRegister

class Test(unittest.TestCase):


	def setUp(self):
		class FakeClassWithoutImplementation(ComponentRegister):
			def __init__(self):
				pass 
			
		self.test_class = FakeClassWithoutImplementation()

	def testHostClassReceivesMixinFunctions(self):
		


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()