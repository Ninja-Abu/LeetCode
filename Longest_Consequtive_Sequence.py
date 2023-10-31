class LongestSeq(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        length = 0
        longest = 0

        for n in numSet:
            # We check if its the first element of a set by n - 1
            if (n - 1) not in numSet:
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest
