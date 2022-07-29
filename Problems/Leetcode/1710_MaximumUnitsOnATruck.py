class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        T: O(nlogn)
        C: O(1)
        """
        # Sort by units in descending order
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        max_units = 0
        for boxes, units in boxTypes:
            if truckSize <= boxes:
                max_units += truckSize * units
                break
            else:
                max_units += boxes * units
                truckSize -= boxes

        return max_units
