# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:18:02 2020

@author: BERKAY 
"""

import numpy as np


grid= [[0,0,6,0,0,0,0,0,0],
       [0,8,0,0,5,4,2,0,0],
       [0,4,0,0,9,0,0,7,0],
       [0,0,7,9,0,0,3,0,0],
       [0,0,0,0,8,0,4,0,0],
       [6,0,0,0,0,0,1,0,0],
       [2,0,3,0,0,0,0,0,1],
       [0,0,0,5,0,0,0,4,0],
       [0,0,8,3,0,0,5,0,2]]


def possible(y,x,n) :
   
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for k in range(0,9):
        if grid[k][x] == n:
            return False
    xSquare = (x//3)*3
    ySquare = (y//3)*3
    for j in range(0,3):
        for m in range(0,3):
            if grid[ySquare+j][xSquare+m] == n:
                return False
    return True    


def solve() :
    global grid
    for y in range(0,9):
        for x in range(0,9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return grid
    print(np.matrix(grid))

solve()
   
    
    


