import numpy as np

def getVectorCorrections(B, C, W):
    M = np.linalg.inv(np.dot(B,np.dot(C,B.T)))
    K = np.dot(M,W)
    V = np.dot(np.dot(C,B.T),K)
    return V