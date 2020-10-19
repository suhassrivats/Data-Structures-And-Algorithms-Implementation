class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        """
        Time Complexity: O(log n) as we are traversing level by level
        Space Complexity: O(log n) If including the space required for the
            return res object counts as space then we need O(log n) because we
            need to store the path from the root to the label
        """
        if label <= 0:
            return []

        results = []
        results.append(label)

        # Determine the level of the label
        level = 0
        while (2**(level+1)) <= label:
            level += 1

        # Find the parent of the label and insert it into our results
        while level > 0:
            level_min = 2**level
            level_max = 2**(level+1) - 1
            parent = (level_min + level_max - label) // 2
            label = parent
            results.insert(0, label)
            level -= 1

        return results
