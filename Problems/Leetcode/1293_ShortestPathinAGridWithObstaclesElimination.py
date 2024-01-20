from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Directions we use to change our location
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Queue for BFS traversal
        q = deque()
        # Append starting details to queue. (row, col, steps, k)
        q.append((0,0,0,k))
        # Use a set to track the locations we have visited
        seen = set()

        while q:
            r,c,steps,rk = q.popleft()
            # If we are at the finish, return the steps
            if r==rows-1 and c==cols-1:
                return steps
            # Keep traversing otherwise
            else:
                for x,y in directions:
                    nr = r+y
                    nc = c+x

                    # If the location is on board and has not been visited
                    if (nr>=0 and nr<rows) and (nc>=0 and nc<cols) and (nr, nc, rk) not in seen:
                        # If its a blocker but we still have k left, we'll go there and k-=1
                        if grid[nr][nc] == 1 and rk > 0:
                            seen.add((nr, nc, rk))
                            q.append((nr, nc, steps + 1, rk - 1))
                        # Otherwise continue on if its a 0 - free location
                        elif grid[nr][nc] == 0:
                            seen.add((nr, nc, rk))
                            q.append((nr,nc,steps+1,rk))

        # If we don't hit the end in our traversal we know it's not possible.
        return -1
