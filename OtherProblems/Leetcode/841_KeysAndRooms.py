class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Time Complexity: O(N+E), where N is the number of rooms, and E is the
            total number of keys.

        Space Complexity: O(N) in additional space complexity, to store stack
            and visited.
        """
        visited = set()
        stack = [0]

        while stack:
            # Get the last visited room from stack
            room = stack.pop()

            # Keep track of all the visited rooms
            visited.add(room)

            # Get a list of all keys in a particular room
            keys = rooms[room]
            for key in keys:
                if key not in visited:
                    stack.append(key)

        return len(visited) == len(rooms)
