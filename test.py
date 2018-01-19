import unittest
import util


class MyTestCase(unittest.TestCase):

    def test_voting_mechanism_failure(self):
        test_array = [0]
        message = '/option1'
        util.vote_option(message, test_array)
        self.assertEqual(test_array[0], 1)

    def test_voting_mechanism_success(self):
        test_array = [0]
        message = '/option1'
        util.vote_option(message, test_array)
        self.assertEqual(test_array[0], 0)

if __name__ == '__main__':
   log_file = 'log_file.txt'
   f = open(log_file, "w")
   runner = unittest.TextTestRunner(f)
   unittest.main(testRunner=runner)
   f.close()
