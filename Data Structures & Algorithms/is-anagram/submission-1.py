class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for n in range(len(s)):
            s_dict[s[n]] = 1 + s_dict.get(s[n], 0)
            t_dict[t[n]] = 1 + t_dict.get(t[n], 0)
        return s_dict == t_dict