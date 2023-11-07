import copy
import random
random.seed(123)
import numpy as np
import matplotlib as matlab
from scipy.spatial.distance import hamming
import matplotlib.pyplot as plt
from PIL import Image as im
def MinimizeHammingDistance(v, c):
    #v to wektor odkodowywany a c to to C co jest w zadaniach
    d = []
    for j in range(len(c)):
        odl = 0
        for i in range(len(v)):
            if (c[j][i] != v[i]):
                odl += 1
        d.append(odl)
    a = min(d)
    L = []
    for j in range(len(d)):
        if d[j] == a:
            L.append(c[j])
    w = L[0]
    w = [w[0], w[1], w[2], w[3]]
    return w

def main():
    #a
    print("#a")
    A = [[],[],[],[]]
    for i in range(4):
        for j in range(10):
            A[i].append(random.randint(0, 4))
    print(np.asmatrix(A))
    #b
    print("#b")
    B = copy.deepcopy(A)
    for i in range(4):
        for j in range(10):
            B[i][j] = A[i][j] / 4
    print(np.asmatrix(B))
    #c
    print("#c")
    G = [[1,0,0,0,0,4,4,2,0,1,1], [0,1,0,0,0,3,0,2,2,1,0], [0,0,1,0,0,2,0,1,1,1,1], [0,0,0,1,1,0,0,0,4,3,0]]
    print(np.asmatrix(G))
    #d
    print("#d")
    C = np.transpose(A)
    w = []
    for i in range(len(C)):
        wektor = np.transpose(np.dot((C[i]) , G))
        w.append(wektor)
    for i in range(len(w)):
        for j in range(len(w[0])):
            if w[i][j] >= 5:
                w[i][j] -= 5

    print(np.asmatrix(w))
    #e
    print("#e")
    u = copy.deepcopy(w)
    for i in range(len(u)):
        for j in range(len(u[0])):
            q = random.random()
            if q < 0.95:
                u[i][j] += 0
            else:
                u[i][j] += 3
            while u[i][j] >= 5:
                u[i][j] -= 5
    print(np.asmatrix(u))
    #f i #g
    print("#f i #g")
    m = []
    for i in range(len(w)):
        wektor = MinimizeHammingDistance(w[i], u)
        m.append(wektor)
    print(np.asmatrix(np.transpose(m)))
    print(np.asmatrix(A))
    print(np.asmatrix(B))
    m = np.transpose(m)
    print(np.asmatrix(m))
    array = np.asarray(B)
    map = plt.imshow(array)
    map.set_cmap("Greys_r")
    plt.savefig("out.png")







if __name__ == "__main__":
    main()