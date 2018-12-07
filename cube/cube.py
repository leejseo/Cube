from constant import *
class Cube:
    corner_face = [
        [U, F, L], [U, R, F], [U, B, R], [U, L, B],
        [D, B, L], [D, L, F], [D, F, R], [D, R, B]
    ]
    edge_face = [
        [U, B], [U, R], [U, F], [U, L],
        [B, L], [B, R], [F, R], [F, L],
        [D, B], [D, R], [D, F], [D, L]
    ]
    corner_cycle = [
        [0,3,2,1], [4,5,6,7], [0,1,6,5], [2,3,4,7], [0,5,4,3], [1,2,7,6]
    ]
    edge_cycle = [
        [0,1,2,3], [8,11,10,9], [2,6,10,7], [0,4,8,5], [3,7,11,4], [1,5,9,6]
    ]
    corner_offset_orientation = [
        [0,0,0,0], [0,0,0,0], [1,2,1,2], [1,2,1,2], [2,1,2,1], [1,2,1,2]
    ]
    edge_offset_orientation = [
        [0,0,0,0], [0,0,0,0], [1,1,1,1], [1,1,1,1], [0,0,0,0], [0,0,0,0]
    ]
    corner_face_index = [
        [(2,0), (0,0), (0,2)],
        [(2,2), (0,0), (0,2)],
        [(0,2), (0,0), (0,2)],
        [(0,0), (0,0), (0,2)],
        [(2,0), (2,2), (2,0)],
        [(0,0), (2,2), (2,0)],
        [(0,2), (2,2), (2,0)],
        [(2,2), (2,2), (2,0)]
    ]
    edge_face_index = [
        [(0,1),(0,1)],
        [(1,2),(0,1)],
        [(2,1),(0,1)],
        [(1,0),(0,1)],
        [(1,2),(1,0)],
        [(1,0),(1,2)],
        [(1,2),(1,0)],
        [(1,0),(1,2)],
        [(2,1),(2,1)],
        [(1,2),(2,1)],
        [(0,1),(2,1)],
        [(1,0),(2,1)]        
    ]
    corner_position_rotate = [[0]*8 for i in range(6)]
    edge_position_rotate =  [[0]*12 for i in range(6)]
    
    
    def __clear(self):
        self.corner_position = [0,1,2,3,4,5,6,7]
        self.corner_orientation = [0,0,0,0,0,0,0,0]
        self.edge_position = [0,1,2,3,4,5,6,7,8,9,10,11]
        self.edge_orientation = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    def __init__(self):
        self.__clear()
        for face in range(6):
            for j in range(8): self.corner_position_rotate[face][j] = j
            for k in range(4):
                fr = self.corner_cycle[face][k]
                to = self.corner_cycle[face][(k+1)%4]
                self.corner_position_rotate[face][fr] = to
            
            for j in range(12): self.edge_position_rotate[face][j] = j
            for k in range(4):
                fr = self.edge_cycle[face][k]
                to = self.edge_cycle[face][(k+1)%4]
                self.edge_position_rotate[face][fr] = to
        
    def clear(self): self.__clear()
    
    def __CWturn(self, face):
        self.corner_position = composePermutation(self.corner_position, 
                                                  self.corner_position_rotate[face])
        self.edge_position = composePermutation(self.edge_position,
                                                self.edge_position_rotate[face])

        corner = [0]*8
        for k in range(4):
            fr = self.corner_cycle[face][(k-1)%4]
            to = self.corner_cycle[face][k]
            corner[to] = (self.corner_orientation[fr] + self.corner_offset_orientation[face][k])%3
        for k in range(4):
            self.corner_orientation[self.corner_cycle[face][k]] = corner[self.corner_cycle[face][k]]
            
        edge = [0]*12
        for k in range(4):
            fr = self.edge_cycle[face][(k-1)%4]
            to = self.edge_cycle[face][k]
            edge[to] = (self.edge_orientation[fr] + self.edge_offset_orientation[face][k])%2
        for k in range(4):
            self.edge_orientation[self.edge_cycle[face][k]] = edge[self.edge_cycle[face][k]]
    
    def turn(self, face, direction):
        assert direction in [-1, 1]
        if direction == 1:
            self.__CWturn(face)
        else:
            for numTurn in range(3): self.__CWturn(face)
    
    def draw_figure(self):
        F = [[[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]] for i in range(6)
            ]
        
        corner = [None]*8
        for j in range(8): corner[self.corner_position[j]] = j
        for j in range(8):
            for i in range(3):
                face = self.corner_face[j][i]
                row = self.corner_face_index[j][i][0]
                col = self.corner_face_index[j][i][1]
                F[face][row][col] = self.corner_face[corner[j]][(self.corner_orientation[j]+i)%3]
    
        edge = [None]*12        
        for j in range(12): edge[self.edge_position[j]] = j
        for j in range(12):
            for i in range(2):
                face = self.edge_face[j][i]
                row = self.edge_face_index[j][i][0]
                col = self.edge_face_index[j][i][1]
                F[face][row][col] = self.edge_face[edge[j]][(self.edge_orientation[j]+i)%2]
        for face in range(6): F[face][1][1] = face
        return F
