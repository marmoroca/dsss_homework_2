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
        # TODO
        pass

    def test_solve_math_problem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                pass

if __name__ == "__main__":
    unittest.main()
