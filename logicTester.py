
import unittest
import operator

from logexp import *

class TestLogicExpBase(unittest.TestCase):

    def test_streq(self):

		# build the logic expression
        exp1 = LogExp([('username', 'U104')], operator.eq, True)
        exp2 = LogExp([('computer', 'C5416')], operator.eq, True)
        exp3 = LogExp([('timestamp', '1345403')], operator.gt, True)

        texp = LogExp([exp1, exp2, exp3], operator.and_)

		# data is a dictionary
        data = [{'username': 'U104', 'computer':'C5416', 'timestamp' : '1345414'}, \
                {'username': 'U104', 'computer':'C5416', 'timestamp' : '1345314'}, \
                {'username': 'U105', 'computer':'C5417', 'timestamp' : '1345414'}, \
                {'username': 'U104', 'computer':'C5416', 'timestamp' : '1345414'}] 

		# test
        self.assertTrue(texp.eval(data[0]))
        self.assertFalse(texp.eval(data[1]))
        self.assertFalse(texp.eval(data[2]))
        self.assertTrue(texp.eval(data[3]))
	
if __name__ == "__main__":

    unittest.main()

