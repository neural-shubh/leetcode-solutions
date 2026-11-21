
class Solution:
    def longestPath(self, parent, s):
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        maximum = 1

        def dfs(node):
            nonlocal maximum

            longest = 0
            second_longest = 0

            for child in children[node]:
                child_length = dfs(child)

                if s[child] == s[node]:
                    continue

                if child_length > longest:
                    second_longest = longest
                    longest = child_length

                elif child_length > second_longest:
                    second_longest = child_length

            maximum = max(
                maximum,
                1 + longest + second_longest
            )

            return 1 + longest

        dfs(0)
        return maximum
