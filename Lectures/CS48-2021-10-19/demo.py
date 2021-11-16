"""
An `image` is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).
Given a coordinate `(sr, sc)` representing the starting pixel (row and column)
of the flood fill, and a pixel value `newColor`, "flood fill" the image.
To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels (also
with the same color as the starting pixel), and so on. Replace the color of all
of the aforementioned pixels with the newColor.
At the end, return the modified image.
Example 1:
```plaintext
Input:
image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels
connected by a path of the same color as the starting pixel are colored with
the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.
```
Notes:
- The length of `image` and `image[0]` will be in the range `[1, 50]`.
- The given starting pixel will satisfy `0 <= sr < image.length` and
`0 <= sc < image[0].length`.
- The value of each color in `image[i][j]` and `newColor` will be an integer in
`[0, 65535]`.


get the max rows and the max cols?
get the current color

check if the current color is the same as the new color
  return the input

do a dft passing in the starting row and col

# dft
check if the color of the image at current row and current col are the same as the current color
  - set the current pixel to the new color
  - check if the row is greater than or equal to 1: call dft passing in row - 1 and col
  - check if row + 1 is less than the max rows: call dft passing in row + 1 and col
  - check if col is greater than or equal to 1: call dft passing row and col - 1
  - check if col + 1 is less than the max cols: call dft passing in row and col + 1


return the image back to the caller

"""


def flood_fill(image, sr, sc, new_color):  # Linear time complexity, Constant space complexity
    """
    Inputs:
    image -> List[List[int]]
    sr -> int
    sc -> int
    new_color -> int
    Output:
    List[List[int]]
    """
    max_cols = len(image[0])  # O(1)
    max_rows = len(image)  # O(1)

    old_color = image[sr][sc]  # O(1)

    if old_color == new_color:  # O(1)
        return image  # O(1)

    def dft(r, c):  # O(n) where n is the width * height of all pixels containing the old_color
        if image[r][c] == old_color:
            image[r][c] = new_color

            # get neighbors
            if r >= 1:
                # north
                dft(r - 1, c)
            # south
            if r + 1 < max_rows:
                dft(r + 1, c)
            # west
            if c >= 1:
                dft(r, c - 1)
            # east
            if c + 1 < max_cols:
                dft(r, c + 1)

    dft(sr, sc)

    return image


# tests
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
