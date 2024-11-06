import unittest
from math_quiz import create_random_number, create_random_operator, solve_math_problem


class TestMathGame(unittest.TestCase):

    def test_create_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = create_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_create_random_operator(self):
        #Test that create_random_operator generates one of the valid operators.
        valid_operators = {'+', '-', '*', '/'}
        for _ in range(1000):  # Test a large number of random operators
            rand_op = create_random_operator()       
            self.assertIn(rand_op, valid_operators)

    def test_solve_math_problem(self):
        #Test that solve_math_problem returns the correct answer and formatted problem.
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (9, 4, '-', '9 - 4', 5),
            (8, 2, '*', '8 * 2', 16)
        ]
        
        for n1, n2, op, expected_problem, expected_answer in test_cases:
            problem, answer = solve_math_problem(n1, n2, op)
            self.assertEqual(problem, expected_problem, f"Expected problem string '{expected_problem}', but got '{problem}'")
            self.assertEqual(answer, expected_answer, f"Expected answer {expected_answer}, but got {answer}")


if __name__ == "__main__":
    unittest.main()
