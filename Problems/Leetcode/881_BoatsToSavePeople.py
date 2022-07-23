class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  # O(NlogN)
        boats = 0
        left, right = 0, len(people)-1
        while left <= right:
            remaining_weight = limit - people[right]
            right -= 1
            boats += 1
            if left <= right and people[left] <= remaining_weight:
                left += 1
        return boats
