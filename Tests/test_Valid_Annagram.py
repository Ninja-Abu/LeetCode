import unittest
from Valid_Annagram import Valid_Annagram


class TestContainsDuplicate(unittest.TestCase):
    def test_is_Anagram(self):
        # Create an instance of the Contains_Duplicate class
        cd = Valid_Annagram()

        # Test an anagram
        s1 = "anagram"
        t1 = "nagaram"
        self.assertTrue(cd.isAnagram(s1, t1))

        # Test not an anagram
        s2 = "rat"
        t2 = "car"
        self.assertFalse(cd.isAnagram(s2, t2))


if __name__ == '__main__':
    unittest.main()
