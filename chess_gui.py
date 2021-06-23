#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Kay Kats

A simple two player chess game using pygame. Players drag and drop the pieces
across the board using the left mouse button. Before capturing the piece must
be removed using the right mouse button.

Chess pieces were created using the free Pecita font.

Icon available at http://flaticon.com

Python 3.8.10
Pygame 2.0.1

"""

# import packages and required files

import pygame
import os
import sys

# System Settings

os.environ['SDL_AUDIODRIVER'] = 'dsp'
sys.dont_write_bytecode = True  # Prevents .pyc file being written
pygame.init()

# Define the files of the chess board / W = Width, H = Height

TILE_W = 60
TILE_H = 60
SCREEN_WIDTH = TILE_W * 8
SCREEN_HEIGHT = TILE_H * 8

# Screen Settings

pygame.display.set_caption("Let's play chess!")
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 60 # Frames per second
GREY = (165, 165, 165)
WHITE = (255, 255, 255)
ICON = pygame.image.load(os.path.join('img', 'chess-pieces.png'))
pygame.display.set_icon(ICON)

# Class for each piece

class Piece(pygame.sprite.Sprite):
    def __init__(self,picture_path, pos_x, pos_y):
        super(Piece, self).__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.clicked = False
    
                
# Load in white pieces

whiteKing = Piece("img/w_king.png", 240, 420)
whiteQueen = Piece("img/w_queen.png", 180, 420)
whiteRook1 = Piece("img/w_rook.png", 0, 420)
whiteRook2 = Piece("img/w_rook.png", 420, 420)
whiteKnight1 = Piece("img/w_knight.png", 60, 420)
whiteKnight2 = Piece("img/w_knight.png", 360, 420)
whiteBishop1 = Piece("img/w_bishop.png", 120, 420)
whiteBishop2 = Piece("img/w_bishop.png", 300, 420)

# Load in black pieces

blackKing = Piece("img/b_king.png", 240, 0)
blackQueen = Piece("img/b_queen.png", 180, 0)
blackRook1 = Piece("img/b_rook.png", 0, 0)
blackRook2 = Piece("img/b_rook.png", 420, 0)
blackKnight1 = Piece("img/b_knight.png", 60, 0)
blackKnight2 = Piece("img/b_knight.png", 360, 0)
blackBishop1 = Piece("img/b_bishop.png", 120, 0)
blackBishop2 = Piece("img/b_bishop.png", 300, 0)

# Create two Sprite colour groups

white_group = pygame.sprite.Group()
white_group.add(whiteKing, whiteQueen, whiteRook1, whiteRook2, 
                whiteKnight1, whiteKnight2, whiteBishop1, whiteBishop2)

black_group = pygame.sprite.Group()
black_group.add(blackKing, blackQueen, blackRook1, blackRook2, blackKnight1,
                blackKnight2, blackBishop1, blackBishop2)

# For loop the pawns into the Sprite groups

for whitepawn in range(8):
    new_wpawn = Piece("img/w_pawn.png", whitepawn*60, 360)
    white_group.add(new_wpawn)
    

for blackpawn in range(8):
    new_bpawn = Piece("img/b_pawn.png", blackpawn*60, 60)
    black_group.add(new_bpawn)

# Create the screen and code piece movement by colour group.

def main():

    clock = pygame.time.Clock()
    
    run = True  # The program is running
    
    while run:
        clock.tick(FPS)
        pygame.draw.rect(SCREEN, GREY, [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])
        for row in range(4):
            for col in range(4):
                pygame.draw.rect(SCREEN,WHITE,
                                 [row*120, col*120, TILE_W, TILE_H])
                pygame.draw.rect(SCREEN, WHITE, [row*120 + TILE_W,
                                                 col*120 + TILE_H,
                                                 TILE_W, TILE_H])
                
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                if event.button == 1:
                    for w in white_group:
                        if w.rect.collidepoint(x, y):
                            w.clicked = True
                    for b in black_group:
                        if b.rect.collidepoint(x, y):
                            b.clicked = True
                elif event.button == 3:
                    for w in white_group:
                        if w.rect.collidepoint(x, y):
                            w.clicked = True
                            white_group.remove(w)
                    for b in black_group:
                        if b.rect.collidepoint(x, y):
                            b.clicked = True
                            black_group.remove(b)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for w in white_group:
                        w.clicked = False
                    for b in black_group:
                        b.clicked = False
        
        for w in white_group:
            if w.clicked == True:
                pos = pygame.mouse.get_pos()
                w.rect.x = pos[0]-(w.rect.width/2)
                w.rect.y = pos[1]-(w.rect.height/2)
        for b in black_group:
            if b.clicked == True:
                pos = pygame.mouse.get_pos()
                b.rect.x = pos[0]-(b.rect.width/2)
                b.rect.y = pos[1]-(b.rect.height/2)
                
        white_group.draw(SCREEN)
        black_group.draw(SCREEN)
        pygame.display.update()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()

###### Tests

# Load main pygame window and icons - pass
# Create background chessboard # pass
# Create Piece class and add pieces to seperate sprite groups - pass
# write pieces to main window = pass
# code piece movement/deletion according to class by mouse event type - pass

##### Known bugs

# pieces merge when clicked on each other. Possible fix could be creating
# individual ID and writing a collision detection function in the class.

##### Future improvements / ideas

# Fix the bug
# an automatic way to capture pieces
# Create a two player game where pieces are restricted by legal moves
# Implement an AI for a one player game. 