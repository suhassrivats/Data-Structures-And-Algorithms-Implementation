import collections

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        Time Complexity: Because we know all candidates will be visited after
        at most 10000 iterations, so time complexity is O(10000) = O(1). But if
        counts of digits increase from 4 to n, its time complexity will become
        O(10^n).

        Space complexity: Because there are two directions for rotating digits
        and there are 4 digits in this lock, the queue should support up to 8
        element in it. Therefore, space complexity is O(2*4) = O(8) = O(1). And
        again, if counts of digits increase from 4 to n, its space complexity
        will become O(2*n) = O(n).
        """
        dead_set = set(deadends)
        queue = collections.deque([('0000', 0)])
        visited = set('0000')

        while queue:
            (string, steps) = queue.popleft()

            # Return the number of steps if target combination is possible
            if string == target:
                return steps

            # Make sure our digits combination is not one of the deadends
            elif string in dead_set:
                continue

            # Since there are 4 locks (digits)
            for i in range(4):
                digit = int(string[i])
                # Every digit can be rotated 1-step in both directions. Ex:
                # For 0000: 9000 & 1000 are combinations by rotating 1st digit
                for move in [-1, 1]:
                    # new_digit will give +1 or -1 of a current digit. Ex: if
                    # digit is 0, new_digit will be 1 or 9 based on move
                    new_digit = (digit + move) % 10

                    # Form a digits combination based on new_digit
                    new_string = string[:i] + str(new_digit) + string[i+1:]

                    # Make sure that the combination does not exist already
                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append((new_string, steps+1))
        return -1
