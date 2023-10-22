import unittest
from Contains_Duplicate import Contains_Duplicate


class TestContainsDuplicate(unittest.TestCase):
    def test_contains_duplicate(self):
        # Create an instance of the Contains_Duplicate class
        cd = Contains_Duplicate()

        # Test with a list containing duplicates
        nums_with_duplicates = [1, 2, 3, 4, 1]
        self.assertTrue(cd.containsDuplicate(nums_with_duplicates))

        # Test with a list containing no duplicates
        nums_no_duplicates = [1, 2, 3, 4, 5]
        self.assertFalse(cd.containsDuplicate(nums_no_duplicates))


if __name__ == '__main__':
    unittest.main()
