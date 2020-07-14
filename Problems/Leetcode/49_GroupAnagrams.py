class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time Complexity: O(n.slog(s)) // n is len of input, s is len of string
        Space Complexity (auxiliary): O(n.s) // total information content stored
            in dict
        """
        dict = {}
        for word in strs:
            key = tuple(sorted(word))
            dict[key] = dict.get(key, []) + [word]
        return dict.values()
