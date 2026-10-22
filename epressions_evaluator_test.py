# Testing from unittest

import unittest
from expression_evaluator import evaluate, tokenize

class TestEvaluator(unittest.TestCase): 

    # Testing arithmetic expressions and ops.

    def test_assignment(self):
        ''' Testing PEMDAS'''
        self.assertEqual(50, evaluate("10 + 20 * 2"))

    def test_single_num(self):
        ''' Testing single digits getting passed '''
        self.assertEqual(7, evaluate("7"))
    
    def test_single_negative(self):
        ''' Testing isolated negative numbers'''
        self.assertEqual(-42, evaluate("-42"))
    
    def test_no_spaces(self):
        ''' Testing an expression for when there are no spaces '''
        self.assertEqual(11, evaluate("3+4*2"))
    
    def test_extra_spaces(self):
        ''' Testing extra spaces in the expression '''
        self.assertEqual(7, evaluate("  3  +  4   "))
    
    def test_left_to_right_sub(self):
        ''' Testing expressions go from left to right '''
        self.assertEqual(3, evaluate("10 - 5 - 2"))

    def test_left_to_right_division(self):
        ''' Testing expressions to go left to right for division as well '''
        self.assertEqual(5, evaluate("100 / 10 / 2"))
    
    def test_negative_operand(self):
        ''' Test negative operand '''
        self.assertEqual(-20, evaluate("10 * -2"))
    
    def test_minus_negative(self):
        ''' Test subtracting neg. numbers '''
        self.assertEqual(15, evaluate("10 - -5"))
    
    def test_all_operators(self):
        ''' Ensuring all operators work when combined together '''
        self.assertEqual(12, evaluate("2 + 3 * 4 - 10 / 5"))
    
    def test_max_boundary(self):
        ''' Making sure the test are within range '''
        self.assertTrue("2147483647")

    def test_min_boundary(self):
        ''' Testing the min boundary of your expression '''
        self.assertTrue(evaluate("-2147483648"))

    # Invalid test:
    # Needed examples/ tutorial on assertRaises()
    # Unittest - Unit Testing Framework. Python documentation. (n.d.-c). https://docs.python.org/3/library/unittest.html 
    def test_non_numeric_operand(self):
        ''' Test case handling for error handling regarding non numeric operands'''
        with self.assertRaises(ValueError):
            evaluate("foo / 30 + 7")

    def test_invalid_operator(self):
        ''' Test invalid operators error handling '''
        with self.assertRaises(ValueError):
            evaluate("10 % 3")
    
    def test_two_numbers_in_a_row(self):
        ''' Test error handling for two nums in a row '''
        with self.assertRaises(ValueError):
            evaluate("10 20")

    def test_two_operands_in_a_row(self):
        ''' Error handling for two operands in the same row '''
        with self.assertRaises(ValueError):
            evaluate("10 + * 3")
    
    def test_trailing_operator(self):
        '''Test trailing operators and its error handling '''
        with self.assertRaises(ValueError):
            evaluate("5 +")
    
    def test_leading_operator(self):
        ''' Test error handling for leading operators '''
        with self.assertRaises(ValueError):
            evaluate("* 5")
    
    def test_empty_string(self):
        ''' Test empty string error handling '''
        with self.assertRaises(ValueError):
            evaluate("")
    
    def test_only_spaces(self):
        ''' Test error handling for spaces '''
        with self.assertRaises(ValueError):
            evaluate("  ")
    
    def test_decimals(self):
        ''' Error handling for decimals in expressions '''
        with self.assertRaises(ValueError):
            evaluate("3.5 + 1")
    
    def test_too_large(self):
        ''' Testing too large expressions/ error handling '''
        with self.assertRaises(ValueError):
            evaluate("2147483648")

    def test_too_small(self):
        ''' Testing expression error handling that are too small '''
        with self.assertRaises(ValueError):
            evaluate("-2147483649")

    def test_separated_sign(self):
        ''' Testing error handling for separated signs '''   
        with self.assertRaises(ValueError):
            evaluate("10 * - 5")

    def test_divide_by_zero(self):
        ''' Error handling for dividing by zero'''
        with self.assertRaises(ZeroDivisionError):
            evaluate("10 / 0")

    def test_divide_by_negative_zero(self):
        ''' Test for dividing by a negative zero ''' 
        with self.assertRaises(ZeroDivisionError):
            evaluate("5 / -0")
    


# Help for testing such as dummy information and naming conventions are from:
# https://claude.ai/share/109eeec1-dbb6-4124-bf4a-e1b18a97d145
# No code is provided. That is all created by me!





if __name__ == "__main__":
    unittest.main()