class Solution:
    def judge_circle(self, moves: str) -> bool:

        x = 0
        y = 0

        for move in moves:
            if(move=='U'):
                y+=1
            elif(move=='R'):
                x+=1
            elif(move=='D'):
                y-=1
            elif(move=='L'):
                x-=1
        return x==0 and y==0


moves = "LURP"
moves1 = "LRUD"
s = Solution()
answer = s.judge_circle(moves)
print(answer)
answer = s.judge_circle(moves1)
print(answer)