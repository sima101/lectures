#copied from tests.py

import unittest
import leading #leading.py we created

class TestLeading(unittest.TestCase):
    '''Tests for leading.'''
    
    def test_word(self):
        '''test word'''
        word = 'bear'
        output = leading_substrings(word)
        expected = ['b', 'be', 'bea', 'bear']
        self.assertEqual(expected, output, 'Argument is a word')

    def test_empty(self):
        word = ''
        output = leading.leading_substrings(word)
        expected = []
        self.assertEqual(expected, output, 'Argument is empty')

    def test_running_sum_one(self):
        '''Test a one-item list.'''
        inputted = [2]
        tools.running_sum(inputted)
        output_expected = [2]
        self.assertEqual(output_expected, inputted, "The list contains one item.")

    def test_running_sum_two(self):
        '''Test a two-item list.'''
        inputted = [2, 5]
        tools.running_sum(inputted)
        output_expected = [2, 7]
        self.assertEqual(output_expected, inputted, "The list contains two items.")

    def test_running_sum_multi_neg(self):
        '''Test a list of negative values.'''
        inputted = [-1, -5, -3, -4]
        tools.running_sum(inputted)
        output_expected = [-1, -6, -9, -13]
        self.assertEqual(output_expected, inputted, "The list contains only negative values.")

    def test_running_sum_multi_zeros(self):
        '''Test a list of zeros.'''
        inputted = [0, 0, 0, 0]
        tools.running_sum(inputted)
        output_expected = [0, 0, 0, 0]
        self.assertEqual(output_expected, inputted, "Not working with zeros.")

    def test_running_sum_multi_pos(self):
        '''Test a list of positive values.'''
        inputted = [4, 2, 3, 6]
        tools.running_sum(inputted)
        output_expected = [4, 6, 9, 15]
        self.assertEqual(output_expected, inputted, "Not working with positive values.")

    def test_running_sum_multi_mix(self):
        '''Test a list of mixed values.'''
        inputted = [4, 0, 2, -5]
        tools.running_sum(inputted)
        output_expected = [4, 4, 6, 1]
        self.assertEqual(output_expected, inputted, "Not working with mixed values.")

if __name__ == '__main__':
    unittest.main()
