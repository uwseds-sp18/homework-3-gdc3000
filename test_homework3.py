import unittest
from entropy import entropy
import numpy as np

class PrimeTest(unittest.TestCase):
    def test_oneshot(self):
	  entries = [
		[0,[1]],
		[0.69314718,[.5,.5]],
	  ]
	  
	  outcome=True
	  for entry in entries:
		ans = entry[0]
		prob = entry[1]
		if not np.isclose(entropy(prob),ans):
		    outcome=False
	  self.assertTrue(outcome)
	  
    def test_break(self):
	  self.assertTrue(False)

    def test_pattern(self):
	  test1 = list([.1 for i in range(0,10)]),
	  test2 = list([.01 for i in range(0,100)])
	  self.assertTrue(entropy(test1) < entropy(test2))

if __name__ == '__main__':
    unittest.main()
