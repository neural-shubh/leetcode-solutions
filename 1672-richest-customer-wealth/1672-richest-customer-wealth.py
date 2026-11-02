
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest = 0

        for customer in accounts:
            wealth = sum(customer)

            if wealth > richest:
                richest = wealth

        return richest
