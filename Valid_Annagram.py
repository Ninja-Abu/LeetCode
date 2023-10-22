class Valid_Annagram(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        char_set = {}

        for i in s:
            if i in char_set:
                char_set[i] += 1
            else:
                char_set[i] = 1

        for j in t:
            if j in char_set:
                char_set[j] -= 1
                if char_set[j] == 0:
                    del char_set[j]
            else:
                return False

        print(char_set)
        return not bool(char_set)
