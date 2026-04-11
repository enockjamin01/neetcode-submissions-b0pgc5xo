from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])
        q=deque()
        #Top and bottom
        for i in range(n):
            if board[0][i]=="O":
                q.append((0,i))
                board[0][i]="Y"
            if board[m-1][i]=="O":
                q.append((m-1,i))
                board[m-1][i]="Y"
        #Left and Right
        for i in range(m):
            if board[i][0]=="O":
                q.append((i,0))
                board[i][0]="Y"
            if board[i][n-1]=="O":
                q.append((i,n-1))
                board[i][n-1]="Y"
        visited=set()
        while q:
            i,j=q.popleft()
            visited.add((i,j))
            for k,l in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if k>=0 and l>=0 and k<m and l<n and board[k][l]=="O" and (k,l) not in visited:
                    board[k][l]="Y"
                    q.append((k,l))
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"
        for i in range(m):
            for j in range(n):
                if board[i][j]=="Y":
                    board[i][j]="O"
        



                
            