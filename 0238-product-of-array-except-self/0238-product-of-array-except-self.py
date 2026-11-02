
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)

        # Left products
        left = 1
        for i in range(len(nums)):
            answer[i] = left
            left *= nums[i]

        # Right products
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer
