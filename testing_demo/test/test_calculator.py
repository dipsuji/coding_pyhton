import unittest

import testing_demo.code.calculator


class calcTestCase(unittest.TestCase):

    def test_calc(self):
        result = testing_demo.code.calculator.add(10, 5)

        # OPUPUT - pass test case
        # OK
        self.assertEqual(result, 15)
        self.assertEqual(testing_demo.code.calculator.subtract(10, 5), 5)
        self.assertEqual(testing_demo.code.calculator.multiply(10, 5), 50)
        self.assertEqual(testing_demo.code.calculator.divide(10, 5), 2)

        # this give test fail - OUTPUT
        # FAILED (failures=1)
        # 15 != 20
        # Expected :20
        # Actual   :15

    #     self.assertEqual(calc.add(15, 5), 15)

    #  you can do in different method also
    # when we use in different methode if different test cases then in oupput they shows number of test cases.
    # when we run four method then it gives in output - Ran 4 test, OK/

    def test_sub(self):
        # OPUPUT - pass test case
        # OK
        result = testing_demo.code.calculator.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        # OPUPUT - pass test case
        # OK
        result = testing_demo.code.calculator.multiply(10, 5)
        self.assertEqual(result, 50)

    #
    def test_divide(self):
        # OPUPUT - pass test case
        # OK
        result = testing_demo.code.calculator.divide(10, 5)
        self.assertEqual(result, 2)
