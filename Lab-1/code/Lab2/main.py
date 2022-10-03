import intvalpy as ip
import numpy as np

def det(Aint):
    return Aint[0][0] * Aint[1][1] - Aint[1][0] * Aint[0][1]

if __name__ == '__main__':
    #DELTA = 0.1
    DELTA = 0.025
    
    midA = [
        [1.05, 1],
        [0.95, 1]
    ]

    radA = [
        [DELTA, 0], 
        [DELTA, 0]
    ]

    Aint = ip.Interval(midA, radA, midRadQ=True)

    verts = Aint.vertex

    isFounded = False
    for i in range(len(verts)):
        for j in range(i + 1, len(verts)):
            A1 = verts[i]
            A2 = verts[j]

            if (np.array_equal(A1,A2)):
                break

            if (det(A1) * det(A2) <= 0):
                isFounded = True

                print("FOUNDED with eps={}!".format(DELTA))
                print(A1)
                print(A2)
                print("det(A1) * det(A2) = {} * {} = {}".format(det(A1), det(A2), det(A1) * det(A2)))
                print("So 'A' is unique")
                break
        
        if isFounded:
            break

    if not isFounded:
        print("For all 'A1' and 'A2' in vert(A) det(A1)*det(A2) > 0 => A is ununigue")