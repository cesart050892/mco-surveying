import numpy as np

def getParameters(npdata):

    pt1 = [npdata[1,3][0], npdata[1,3][1], npdata[1,3][2]] # punto 4
    pt2 = [npdata[1,2][0], npdata[1,2][1], npdata[1,2][2]] # punto 3
    pt3 = [npdata[4,2][0], npdata[4,2][1], npdata[4,2][2]] # punto 8
    pt4 = [npdata[4,3][0], npdata[4,3][1], npdata[4,3][2]] # punto 9
    pt5 = [npdata[0,2][0], npdata[0,2][1], npdata[0,2][2]] # punto 10
    pt6 = [npdata[0,3][0], npdata[0,3][1], npdata[0,3][2]] # punto 11

    obs1 = [npdata[1,5]] # obs 2
    obs2 = [npdata[4,5]] # obs 5
    obs3 = [npdata[0,5]] # obs 1
    obs4 = [npdata[3,5]] # obs 4
    obs5 = [npdata[2,5]] # obs 3
    obs6 = [npdata[5,5]] # obs 6

    v = np.array(pt1 + pt2 + pt3 + pt4 + pt5 + pt6 + obs1 + obs2 + obs3 + obs4 + obs5 + obs6, dtype=np.float64).flatten()
    return v