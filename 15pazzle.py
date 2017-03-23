import numpy as np

#direct = np.array([[0,-1],[0,1],[]])
up = 0
down = 1
right = 2
left = 3

puzzle = [[2,5,6,4],
          [10,9,7,13],
          [11,1,8,3],
          [15,14,12,16]]

pos = np.array([3,3])
depth = 0

operations = np.zeros(80)

solve_return = 0

next_direct = np.array([0,0])

def puzzle_correct():
    for i in range(15):
        if puzzle[i/4][i%4] > puzzle[(i+1)/4][(i+1)%4]:
            return -1
    return 1

def solve_puzzle():
    '''今の操作の状態より下層の状態の中に上手く行くものがあれば帰らずプログラムを終了させる
    なければ、帰ってくる関数'''
    global next_direct,depth,operations
    nextpos = pos + next_direct
    if 0 <= nextpos[0] <= 3 and 0 <= nextpos[1] <= 3 and depth <= 80:
        puzzle[pos[0]][pos[1]] = puzzle[nextpos[0]][nextpos[1]]
        puzzle[nextpos[0]][nextpos[1]] = 16
        if puzzle_correct() == 1:
            print("finish solve:", puzzle, "\n operation is\n", operations)
            exit()
    else:
        return
    for i,dir in enumerate(np.array([[0,-1],[0,1],[1,0],[-1,0]])):
        next_direct = dir
        operations[depth] = i
        depth += 1
        solve_puzzle()
        depth -= 1
    return

 for i,dir in enumerate(np.array([[0,-1],[0,1],[1,0],[-1,0]])):
        next_direct = dir
        operations[depth] = i
        depth += 1
        solve_puzzle()
        depth -= 1


