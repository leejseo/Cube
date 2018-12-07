from cube import *

if __name__ == "__main__":
    T = int(input())
    C = Cube()
    for numCase in range(T):
        C.clear()
        numQuery = int(input())
        queries = input().split()
        face = 0
        direction = 0
        for s in queries:          
            face = eval(s[0])         
            direction = eval(s[1]+'1')        
            C.turn(face, direction)
        A = C.draw_figure()
        M = A[U]
        for i in range(3):
            for j in range(3):
                print(COLOR[M[i][j]], end='')
            print()
