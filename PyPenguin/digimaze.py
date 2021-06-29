# -*- coding: utf-8 -*-
#################
import numpy as np

#################
"""
PyPenguin.digimaze
================

Block class
    Block


Created on Tue May 4 22:21 2021

@author: flovan / fvanden

Revision history:   04.05.2021 - Created


"""
## -------------------------------------------------------------------------- ##


class Block(object):
    """
    Creates Block object

    Parameters - required
    ---------------------
    walls : list of bool
    	list of 4 numbers: 1 for a closed boundary (wall), 0 for an open boundary

    Parameters - optional
    ---------------------


    """
    ## ------------------------------------------------------------------ ##
    ## Constructors/Destructors                                           ##
    ## ------------------------------------------------------------------ ##
    def __init__(self, location, wall):
        pass

        self.location = location
        self.walls = None
        self.dropwalls(wall)

    def __del__(self):
        pass

    ## ------------------------------------------------------------------ ##
    ## Methods                                                            ##
    ## ------------------------------------------------------------------ ##

    # public
    def allow(self, move):
        """
        """
        wpos = [1,1]
        #print("start: ", wpos)
        position = self.location
        for i, pos in enumerate(move):
            if move[i] - position[i] == 0:
                pass
            elif move[i] - position[i] > 0:
                wpos[i] += 1
            else:
                wpos[i] -= 1
        #print("end: ", wpos)
        #print(self.walls[wpos[0]][wpos[1]])
        return self.walls[wpos[0]][wpos[1]]


    # private
    def dropwalls(self, wall):
        """
        """
        walls = np.asarray([[True,True,True],[True, True,True],[True,True,True]])

        if wall[0] == 1:
            walls[:,0] = False
        if wall[1] == 1:
            walls[0,:] = False
        if wall[2] == 1:
            walls[:,-1] = False
        if wall[3] == 1:
            walls[-1,:] = False

        self.walls = walls
