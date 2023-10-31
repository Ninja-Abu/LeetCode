import unittest
from Longest_Consequtive_Sequence import LongestSeq


class TestContainsDuplicate(unittest.TestCase):
    def test_contains_duplicate(self):
        # Create an instance of the class
        ls = LongestSeq()

        # Test with a list containing duplicates
        nums = [100, 4, 200, 1, 3, 2]
        self.assertEquals(ls.longestConsecutive(nums), 4)

        nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        self.assertEquals(ls.longestConsecutive(nums2), 9)


if __name__ == '__main__':
    unittest.main()
