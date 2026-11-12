
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        for row in matrix:

            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            area = self.largestRectangleArea(heights)
            max_area = max(max_area, area)

        return max_area

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        for i in range(len(heights) + 1):

            curr_height = heights[i] if i < len(heights) else 0

            while stack and curr_height < heights[stack[-1]]:

                height = heights[stack.pop()]

                width = i if not stack else i - stack[-1] - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area
