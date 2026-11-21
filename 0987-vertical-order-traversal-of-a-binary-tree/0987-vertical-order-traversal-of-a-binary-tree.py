
from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root):
        if root is None:
            return []

        nodes = []
        queue = deque([(root, 0, 0)])

        while queue:
            node, row, col = queue.popleft()
            nodes.append((col, row, node.val))

            if node.left:
                queue.append((node.left, row + 1, col - 1))

            if node.right:
                queue.append((node.right, row + 1, col + 1))

        nodes.sort()

        result = []
        previous_col = None

        for col, row, value in nodes:
            if col != previous_col:
                result.append([])
                previous_col = col

            result[-1].append(value)

        return result
