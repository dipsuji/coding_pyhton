import unittest

from testing_demo.code.name_adder_use import formatted_name, formatted_name2


# OUTPUT- Ran 2 tests
class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        result = formatted_name("pete", "seeger")
        self.assertEqual(result, "Pete Seeger")

    # # failing test demo -
    def test_first_middle_last_name(self):
        #     result1 = formatted_name1("pete", "seeger")
        #     self.assertEqual(result1, "Pete Seeger")

        # changing for making right test case-
        result2 = formatted_name2("raymond", "reddington", "red")
        self.assertEqual(result2, "Raymond Red Reddington")
