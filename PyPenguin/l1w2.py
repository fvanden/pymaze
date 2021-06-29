# -*- coding: utf-8 -*-
#################
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
from PyPenguin.penguin import Penguin
from PyPenguin.digimaze import Block

import ipywidgets as widgets
#################
"""
l1w1.maze1
================

maze1


Created on Mon May 19 15:53 2021

@author: flovan / fvanden

Revision history:   19.05.2021 - Created


"""
## -------------------------------------------------------------------------- ##

setRight1 = widgets.IntText(
    value=0,
    description='Right:',
    disabled=False
)

setDown1 = widgets.IntText(
    value=0,
    description='Down:',
    disabled=False
)

setRight2 = widgets.IntText(
    value=0,
    description='Right:',
    disabled=False
)

setDown2 = widgets.IntText(
    value=0,
    description='Down:',
    disabled=False
)

setRight3 = widgets.IntText(
    value=0,
    description='Right:',
    disabled=False
)

setUp1 = widgets.IntText(
    value=0,
    description='Up:',
    disabled=False
)

setRight4 = widgets.IntText(
    value=0,
    description='Right:',
    disabled=False
)

setDown3 = widgets.IntText(
    value=0,
    description='Down:',
    disabled=False
)

show = widgets.Button(description='Show correct values',
    disabled=False,
    button_style='warning', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Show correct values')

def set_all(b):
    setRight1.set_trait('value',2)
    setDown1.set_trait('value',2)
    setRight2.set_trait('value',1)
    setDown2.set_trait('value',3)
    setRight3.set_trait('value',1)
    setUp1.set_trait('value',2)
    setRight4.set_trait('value',1)
    setDown3.set_trait('value',1)

enter = widgets.Button(description='Enter',
    disabled=False,
    button_style='success', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Submit values')

#def run_all(ev):
#    dp.display(dp.Javascript('IPython.notebook.execute_cells_below()'))

#enter.on_click(run_all)
show.on_click(set_all)

dirbox1 = widgets.VBox([setRight1,setDown1, setRight2, setDown2, setRight3,setUp1,setRight4,setDown3,enter, show])

#enterbox = widgets.VBox([enter])
#outbox1 = widgets.HBox([dirbox1,dirbox2,dirbox3])
#allbox1 = widgets.VBox([outbox1,enterbox])
dirbox1
