class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sum = []
        for i in range (0,len(accounts)):
            total = 0
            for j in range (0,len(accounts[i])):
                total += accounts[i][j]
            sum.append(total)

        return max(sum)
        