class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        farmlands = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    x, y = i, j
                    while x + 1 < len(land) and land[x + 1][j] == 1: x += 1
                    while y + 1 < len(land[0]) and land[i][y + 1] == 1: y += 1
                    for a in range(i, x + 1):
                        for b in range(j, y + 1):
                            land[a][b] = 0
                    farmlands.append([i, j, x, y])
        return farmlands