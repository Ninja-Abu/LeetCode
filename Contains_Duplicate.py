class Contains_Duplicate(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsA = set()
        for i in nums:
            if i in numsA:
                return True
            numsA.add(i)
        return False