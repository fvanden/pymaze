# -*- coding: utf-8 -*-
#################
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
from pymaze.PyPenguin.penguin import Penguin
from pymaze.PyPenguin.digimaze import Block

import ipywidgets as widgets
#################
"""
l1w1.maze1
================

maze1


Created on Mon May 16 22:04 2021

@author: flovan / fvanden

Revision history:   16.05.2021 - Created


"""
## -------------------------------------------------------------------------- ##

mypenguin = Penguin("penguin.png")
style = {'description_width':'initial'}

left = widgets.Button(
    description = '<- left',
    button_style = 'success',
    tooltip = 'Move right',
    style = style)

up = widgets.Button(
    description = 'up',
    button_style = 'success',
    tooltip = 'Move up',
    style = style)

down = widgets.Button(
    description = 'down',
    button_style = 'success',
    tooltip = 'Move down',
    style = style)

right = widgets.Button(
    description = 'right ->',
    button_style = 'success',
    tooltip = 'Move left',
    style = style)

x = widgets.BoundedIntText(
    value=0,
    min=0,
    max=1000,
    step=100,
    description='x:',
    disabled=False
)

y = widgets.BoundedIntText(
    value=0,
    min=0,
    max=1000,
    step=100,
    description='y:',
    disabled=False
)

maze = [[Block([0,0],[1,1,0,0]), Block([181,0],[0,1,0,1]),Block([362,0],[0,1,1,0]),Block([543,0],[1,1,0,0]),Block([724,0],[0,1,0,1]),Block([905,0],[0,1,1,0])],
        [Block([0,181],[1,0,0,1]), Block([181,181],[0,1,1,0]),Block([362,181],[1,0,1,0]),Block([543,181],[1,0,0,1]),Block([724,181],[0,1,1,0]),Block([905,181],[1,0,1,1])],
        [Block([0,362],[1,1,0,0]), Block([181,362],[0,0,1,1]),Block([362,362],[1,0,0,1]),Block([543,362],[0,1,1,0]),Block([724,362],[1,0,0,1]),Block([905,362],[0,1,1,0])],
        [Block([0,543],[1,0,1,0]), Block([181,543],[1,1,0,1]),Block([362,543],[0,1,1,0]),Block([543,543],[1,0,1,0]),Block([724,543],[1,1,0,0]),Block([905,543],[0,0,1,0])],
        [Block([0,724],[1,0,0,1]), Block([181,724],[0,1,1,0]),Block([362,724],[1,0,1,0]),Block([543,724],[1,0,1,0]),Block([724,724],[1,0,1,0]),Block([905,724],[1,0,1,0])],
        [Block([0,905],[1,1,0,1]), Block([181,905],[0,0,1,1]),Block([362,905],[1,0,0,1]),Block([543,905],[0,0,0,1]),Block([724,905],[0,0,1,1]),Block([905,905],[1,0,1,1])]]



# change block with penguin position

def moveLeft(b):
    myblock = maze[int(mypenguin.position[1]/mypenguin.pace)][int(mypenguin.position[0]/mypenguin.pace)]
    move = [mypenguin.position[0], mypenguin.position[1] - mypenguin.pace]
    if myblock.allow(move):
        mypenguin.moveRight()
        movelist.set_trait('value', movelist.value + 'You moved left \n')
        x.set_trait('value', mypenguin.position[0])
        y.set_trait('value', mypenguin.position[1])
    else:
        pass
        wrongmoves.set_trait('value',wrongmoves.value +1)
        #movelist.set_trait('value', movelist.value + 'You can not move left \n')

def moveUp(b):
    myblock = maze[int(mypenguin.position[1]/mypenguin.pace)][int(mypenguin.position[0]/mypenguin.pace)]
    move = [mypenguin.position[0]- mypenguin.pace, mypenguin.position[1] ]
    if myblock.allow(move):
        mypenguin.moveUp()
        movelist.set_trait('value', movelist.value + 'You moved up \n')
        x.set_trait('value', mypenguin.position[0])
        y.set_trait('value', mypenguin.position[1])
    else:
        pass
        wrongmoves.set_trait('value',wrongmoves.value +1)
        #movelist.set_trait('value', movelist.value + 'You can not move up \n')

def moveDown(b):
    myblock = maze[int(mypenguin.position[1]/mypenguin.pace)][int(mypenguin.position[0]/mypenguin.pace)]
    move = [mypenguin.position[0]+ mypenguin.pace, mypenguin.position[1] ]
    if myblock.allow(move):
        mypenguin.moveDown()
        movelist.set_trait('value', movelist.value + 'You moved down \n')
        x.set_trait('value', mypenguin.position[0])
        y.set_trait('value', mypenguin.position[1])
    else:
        pass
        wrongmoves.set_trait('value',wrongmoves.value +1)
        #movelist.set_trait('value', movelist.value + 'You can not move down \n')


def moveRight(b):
    myblock = maze[int(mypenguin.position[1]/mypenguin.pace)][int(mypenguin.position[0]/mypenguin.pace)]
    move = [mypenguin.position[0], mypenguin.position[1]+ mypenguin.pace ]
    if myblock.allow(move):
        mypenguin.moveLeft()
        movelist.set_trait('value', movelist.value + 'You moved right \n')
        x.set_trait('value', mypenguin.position[0])
        y.set_trait('value', mypenguin.position[1])
    else:
        pass
        wrongmoves.set_trait('value',wrongmoves.value +1)
        #movelist.set_trait('value', movelist.value + 'You can not move right \n')

right.on_click(moveRight)
up.on_click(moveUp)
down.on_click(moveDown)
left.on_click(moveLeft)

def on_value_change(change):
    mypenguin.show()

movelist = widgets.Textarea(
    value = '',
    description = '',
    layout = widgets.Layout(width = '20%', height = '100%', border='solid 2px'),
    disabled = True)

wrongmoves = widgets.IntText(
    value = 0,
    description = 'wrong moves',
    disabled = False
)

def showOut(mypenguin):
    return mypenguin.show()


def movePenguin(x,y):
    display(mypenguin.showposition(x,y))

out = widgets.interactive_output(movePenguin, {'x':x, 'y':y})

dirbox = widgets.HBox([left,up, down, right])
outbox = widgets.HBox([movelist,out])
allbox = widgets.VBox([dirbox,outbox])
allbox
