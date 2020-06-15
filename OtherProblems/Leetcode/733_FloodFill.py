class Solution:
    def floodFill(self, image: List[List[int]], sr: int,
                  sc: int, newColor: int) -> List[List[int]]:
        """
        Time Complexity:
            => O(M x N) // length of (rows * col) (OR)
            => O(n) // n is the number of pixels in the image
        Space Complexity:
            Input Space: O(n)
            Auxiliary Space: O(n) size of the implicit call stack when calling dfs.
        """
        # If newColor is the same as the starting_pixel, then there is nothing
        # to do. Simply return the image as it is.
        if newColor == image[sr][sc]:
            return image

        # Get values for rows, cols and starting_pixel
        rows = len(image)
        cols = len(image[0])
        starting_pixel = image[sr][sc]

        # DFS call
        self.dfs(image, sr, sc, newColor, rows, cols, starting_pixel)

        return image

    def dfs(self, image, sr, sc, newColor, rows, cols, starting_pixel):

        # Handle boundary cases
        if sr < 0 or sr >= rows or sc < 0 or sc >= cols:
            return
        # If adjacent elements are not same as the starting_pixel
        elif image[sr][sc] != starting_pixel:
            return

        # Update the pixel value to newColor
        image[sr][sc] = newColor

        # Check all its adjacent elements. Note that pixel value will be updated
        # only if the adjacent values are same the starting_pixel value
        self.dfs(image, sr-1, sc, newColor, rows, cols, starting_pixel)  # Top
        self.dfs(image, sr+1, sc, newColor, rows, cols, starting_pixel)  # Bottom
        self.dfs(image, sr, sc-1, newColor, rows, cols, starting_pixel)  # Left
        self.dfs(image, sr, sc+1, newColor, rows, cols, starting_pixel)  # Right
