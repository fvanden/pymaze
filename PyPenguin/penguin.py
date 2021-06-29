# -*- coding: utf-8 -*-
#################
import numpy as np
from PIL import Image
#################
"""
PyPenguin.penguin
================

penguin class
    Penguin


Created on Mon May 3 16:48 2021

@author: flovan / fvanden

Revision history:   03.05.2021 - Created


"""
## -------------------------------------------------------------------------- ##


class Penguin(object):
    """
    Creates Penguin object

    Parameters - required
    ---------------------
    filename : str
    	name of the image file to read

    Parameters - optional
    ---------------------


    """
    ## ------------------------------------------------------------------ ##
    ## Constructors/Destructors                                           ##
    ## ------------------------------------------------------------------ ##
    def __init__(self, filename, **kwargs):
        pass

        self.pen = Image.open(filename)
        #self.standardBackground = kwargs.get("background","pymaze/maze1.png")
        self.standardBackground = "pymaze/maze1.png"

        self.pace = 181
        self.orientation = 90
        self.position = (0,0)

        self.drop()

    def __del__(self):
        pass

    ## ------------------------------------------------------------------ ##
    ## Methods                                                            ##
    ## ------------------------------------------------------------------ ##

    # public
    def show(self,):
        """
        """
        self.background.paste(self.pen, tuple(self.position), self.pen)
        return self.background

    def showposition(self, x, y):
        """
        """
        self.background = Image.open(self.standardBackground)
        self.background.paste(self.pen, (x,y),self.pen)
        return self.background

    def moveDown(self):
        """
        """

        self.background = Image.open(self.standardBackground)
        self.rotate("down")
        self.position = (self.position[0], self.position[1] + self.pace)
        self.background.paste(self.pen, tuple(self.position), self.pen)
        return self.background

    def moveUp(self):
        """
        """

        self.background = Image.open(self.standardBackground)
        self.rotate("up")
        self.position = (self.position[0], self.position[1] - self.pace)
        self.background.paste(self.pen, tuple(self.position), self.pen)
        return self.background

    def moveLeft(self):
        """
        """

        self.background = Image.open(self.standardBackground)
        self.rotate("left")
        self.position = (self.position[0]+ self.pace, self.position[1] )
        self.background.paste(self.pen, tuple(self.position), self.pen)
        return self.background

    def moveRight(self):
        """
        """

        self.background = Image.open(self.standardBackground)
        self.rotate("right")
        self.position = (self.position[0]- self.pace, self.position[1] )
        self.background.paste(self.pen, tuple(self.position), self.pen)
        return self.background



    # private
    def drop(self, background = None):
        """
        """
        if background is None:
            self.background = Image.open(self.standardBackground)
        else:
            self.background = Image.open(background)
            self.standardBackground = background

        self.background.paste(self.pen, tuple(self.position), self.pen)
        return self.background

    def rotate(self, direction ):
        """
        """
        if direction == "down":
            orientation = self.orientation - 180
            self.pen = self.pen.rotate(orientation)
            self.orientation = 180

        elif direction == "up":
            orientation = self.orientation
            self.pen = self.pen.rotate(orientation)
            self.orientation = 0

        elif direction == "left":
            orientation = self.orientation - 90
            self.pen = self.pen.rotate(orientation)
            self.orientation = 90

        elif direction == "right":
            orientation = self.orientation - 270
            self.pen = self.pen.rotate(orientation)
            self.orientation = 270
