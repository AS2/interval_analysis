import intvalpy as ip

if __name__ == '__main__':
    #DELTA = 0.1
    DELTA = 0.05
    
    midA = [
        [1.05, 1],
        [0.95, 1]
    ]

    radA = [
        [DELTA, 0], 
        [DELTA, 0]
    ]

    Aint = ip.Interval(midA, radA, midRadQ=True)
    print(Aint)
    detA = Aint[0][0] * Aint[1][1] - Aint[1][0] * Aint[0][1]
    print(detA)