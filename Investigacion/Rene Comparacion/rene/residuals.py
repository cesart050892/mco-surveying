import numpy as np

def getResiduals(npdata):
    obs1 = npdata[0,6]
    obs2 = npdata[1,6]
    obs3 = npdata[2,6]
    obs4 = npdata[3,6]
    obs5 = npdata[4,6]
    obs6 = npdata[5,6]

    W = np.asarray([[obs2],[obs5],[obs1],[obs4],[obs3],[obs6]])
    return W