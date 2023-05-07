# author: Sona Nair
# date: 03/17/23

import numpy as np
from random import choice

class Fifteen:
    
    def __init__(self, size = 4):
        self.size = size
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        self.solved_state = np.array([i for i in range(1,size**2)] + [0])
        self.adj = [[1, 4],     # 0
    [0, 2, 5],  # 1
    [1, 3, 6],  # 2
    [2, 7],     # 3
    [0, 5, 8],  # 4
    [1, 4, 6, 9], # 5
    [2, 5, 7, 10], # 6
    [3, 6, 11], # 7
    [4, 9, 12], # 8
    [5, 8, 10, 13], # 9
    [6, 9, 11, 14], # 10
    [7, 10, 15], # 11
    [8, 13], # 12
    [9, 12, 14], # 13
    [10, 13, 15], # 14
    [11, 14]]        

    def update(self, move):
        if self.is_valid_move(move):
            zero_index = np.where(self.tiles == 0)[0][0]
            move_index = np.where(self.tiles == move)[0][0]
            self.tiles[zero_index], self.tiles[move_index] = self.tiles[move_index], self.tiles[zero_index]
        
    def transpose(self, i, j):
        i_index = np.where(self.tiles == i)[0][0]
        j_index = np.where(self.tiles == j)[0][0]
        self.tiles[i_index], self.tiles[j_index] = self.tiles[j_index], self.tiles[i_index]

    def shuffle(self, steps=100):
        index = np.where(self.tiles == 0)[0][0]
        for i in range(steps):
            move_index = choice(self.adj[index])
            self.tiles[index],self.tiles[move_index] = self.tiles[move_index],self.tiles[index]
            index = move_index
        
        
    def is_valid_move(self, move):
        move_index = np.where(self.tiles == move)[0][0]
        zero_index = np.where(self.tiles == 0)[0][0]
        return move_index in self.adj[zero_index]

    def is_solved(self):
        return np.array_equal(self.tiles, self.solved_state)

    # draw the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):
        for i in range(self.size):
            row = self.tiles[i*self.size:(i+1)*self.size]
            print("+---"*self.size+"+")
            print("|"+" |".join(f"{tile:2}" if tile else "  " for tile in row)+" |")
        print("+---"*self.size+"+")
        
    def __str__(self):
        #return ''.join(['{:3}'.format(x) + '\n' if (i+1)%self.size == 0 else '{:3}'.format(x) for i, x in enumerate(self.tiles)])
        s = ""
        for i in range(self.size):
            row = self.tiles[i*self.size:(i+1)*self.size]
            s += " ".join(f"{tile:2}" if tile else "  " for tile in row)
            s += " \n"
        return s
    

if __name__ == '__main__':
    
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    
    #You should be able to play the game if you uncomment the code below
    
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    
    
    
        
