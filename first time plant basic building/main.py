#! /usr/bin/python3
from random import randint
from tkinter import END

from gdpc import geometry as GEO
from gdpc import interface as INTF
from gdpc import toolbox as TB
from gdpc import worldLoader as WL
from math import floor
from poissionDiskSampling import poissionSample as pS
from NTNUBasicBuilding import InitialChalet

STARTX, STARTY, STARTZ, ENDX, ENDY, ENDZ = INTF.setBuildArea(10,1,10,410,10,410)  # BUILDAREA

WORLDSLICE = WL.WorldSlice(STARTX, STARTZ, ENDX + 1, ENDZ + 1)  # this takes a while
ROADHEIGHT = 0

def buildBasicBuilding():
    heights = WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
    coBuildingList = pS(STARTX,STARTZ,ENDX,ENDZ,5,10)
    print(coBuildingList)
    for pos in coBuildingList:
        x,z = pos
        x,z = floor(x),floor(z)
        y = heights[(x,z)]
        print(x,y,z)
        InitialChalet(x,y,z)

if __name__ == '__main__':

    try:
        height = WORLDSLICE.heightmaps["MOTION_BLOCKING"][(STARTX, STARTY)]
        INTF.runCommand(f"tp @a {STARTX} {height} {STARTZ}")
        print(f"/tp @a {STARTX} {height} {STARTZ}")
        buildBasicBuilding()

        print("Done!")
    except KeyboardInterrupt:   # useful for aborting a run-away program
        print("Pressed Ctrl-C to kill program.")
