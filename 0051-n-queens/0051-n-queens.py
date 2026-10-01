class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        
        res=[]

        board=[]

        for i in range(n):
                row=[]
                for j in range(n):
                    row.append(".")
                board.append(row)

        c=[0]*n

        rd=[0]*(2*n-1)
        ld=[0]*(2*n-1)

        def solve(row):
            if row==n:
                t=[]
                for i in range(n):
                    s=""
                    for j in range(n):
                        s+=board[i][j]
                    t.append(s)
                res.append(t)
                return 
       
            for i in range(n):
                if c[i]==0 and rd[row+i]==0 and ld[row-i+n-1]==0:
                    
                    board[row][i]="Q"
                    c[i]=1
                    rd[row+i]=1
                    ld[row-i+(n-1)]=1

                    solve(row+1)

                    board[row][i]="."
                    c[i]=0
                    rd[row+i]=0
                    ld[row-i+(n-1)]=0

        solve(0)
        return res