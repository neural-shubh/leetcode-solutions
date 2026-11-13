from collections import deque

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:

        queue = deque(students)
        i = 0
        unable = 0

        while queue and unable < len(queue):

            if queue[0] == sandwiches[i]:
                queue.popleft()
                i += 1
                unable = 0

            else:
                queue.append(queue.popleft())
                unable += 1

        return len(queue)