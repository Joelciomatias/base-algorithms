from typing import List
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[' '] * n for _ in range(m)]
        

        for g in guards:
            grid[g[0]][g[1]] = 'g'

        for g in walls:
            grid[g[0]][g[1]] = 'w'

        def walk(r, c):
            
            for row in range(r+1, m):
                if grid[row][c] in ['g','w']:
                    break
                grid[row][c] = 'x'
            
            for row in reversed(range(0, r)):
                if grid[row][c] in ['g','w']:
                    break
                grid[row][c] = '^'

            for col in range(c+1, n):
                if grid[r][col] in ['g','w']:
                    break
                grid[r][col] = '>'
            
            for col in reversed(range(0, c)):
                if grid[r][col] in ['g','w']:
                    break
                grid[r][col] = '<'



        for r,c in guards:
            walk(r,c)
        res = 0
        for row in grid:
            for col in row:
                if col == ' ':
                    res +=1
        return res

    


        
m = 4
n = 6
guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]
print(Solution().countUnguarded(m,n,guards,walls))