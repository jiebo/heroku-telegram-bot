import unittest
import util


class MyTestCase(unittest.TestCase):

    def test_voting_mechanism(self):
        test_array = [0]
        message = '/option1'
        util.vote_option(message, test_array)
        self.assertEqual(test_array[0], 0)



if __name__ == '__main__':
    unittest.main()
