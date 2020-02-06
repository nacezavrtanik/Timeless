latinski = [[[0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 0, 1], [3, 2, 1, 0]],
            [[0, 1, 2, 3], [1, 0, 3, 2], [3, 2, 1, 0], [2, 3, 0, 1]],
            [[0, 1, 2, 3], [3, 2, 1, 0], [1, 0, 3, 2], [2, 3, 0, 1]],
            [[0, 1, 2, 3], [2, 3, 0, 1], [1, 0, 3, 2], [3, 2, 1, 0]],
            [[0, 1, 2, 3], [2, 3, 0, 1], [3, 2, 1, 0], [1, 0, 3, 2]],
            [[0, 1, 2, 3], [3, 2, 1, 0], [2, 3, 0, 1], [1, 0, 3, 2]],
            [[0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 1, 0], [3, 2, 0, 1]],
            [[0, 1, 2, 3], [1, 0, 3, 2], [3, 2, 0, 1], [2, 3, 1, 0]],
            [[0, 1, 2, 3], [3, 2, 0, 1], [1, 0, 3, 2], [2, 3, 1, 0]],
            [[0, 1, 2, 3], [2, 3, 1, 0], [1, 0, 3, 2], [3, 2, 0, 1]],
            [[0, 1, 2, 3], [2, 3, 1, 0], [3, 2, 0, 1], [1, 0, 3, 2]],
            [[0, 1, 2, 3], [3, 2, 0, 1], [2, 3, 1, 0], [1, 0, 3, 2]],
            [[0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1], [3, 0, 1, 2]],
            [[0, 1, 2, 3], [1, 2, 3, 0], [3, 0, 1, 2], [2, 3, 0, 1]],
            [[0, 1, 2, 3], [3, 0, 1, 2], [1, 2, 3, 0], [2, 3, 0, 1]],
            [[0, 1, 2, 3], [2, 3, 0, 1], [1, 2, 3, 0], [3, 0, 1, 2]],
            [[0, 1, 2, 3], [2, 3, 0, 1], [3, 0, 1, 2], [1, 2, 3, 0]],
            [[0, 1, 2, 3], [3, 0, 1, 2], [2, 3, 0, 1], [1, 2, 3, 0]],
            [[0, 1, 2, 3], [1, 3, 0, 2], [2, 0, 3, 1], [3, 2, 1, 0]],
            [[0, 1, 2, 3], [1, 3, 0, 2], [3, 2, 1, 0], [2, 0, 3, 1]],
            [[0, 1, 2, 3], [3, 2, 1, 0], [1, 3, 0, 2], [2, 0, 3, 1]],
            [[0, 1, 2, 3], [2, 0, 3, 1], [1, 3, 0, 2], [3, 2, 1, 0]],
            [[0, 1, 2, 3], [2, 0, 3, 1], [3, 2, 1, 0], [1, 3, 0, 2]],
            [[0, 1, 2, 3], [3, 2, 1, 0], [2, 0, 3, 1], [1, 3, 0, 2]]]

a = latinski[17]

def izomorfizem(latin):
    prototip = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]
    for i in range(4):
        if i == 0:
            prototip[i][0] = latin[0][0]
            prototip[i][1] = latin[1][0]
            prototip[i][2] = latin[2][0]
            prototip[i][3] = latin[3][0]
        elif i == 1:
            prototip[i][0] = latin[1][1]
            prototip[i][1] = latin[0][1]
            prototip[i][2] = latin[3][1]
            prototip[i][3] = latin[2][1]
        elif i == 2:
            prototip[i][0] = latin[2][2]
            prototip[i][1] = latin[3][2]
            prototip[i][2] = latin[0][2]
            prototip[i][3] = latin[1][2]
        else:
            prototip[i][0] = latin[3][3]
            prototip[i][1] = latin[2][3]
            prototip[i][2] = latin[1][3]
            prototip[i][3] = latin[0][3]
    return(prototip)

matchupi = []

print('[')
for i in range(len(latinski)):
    matchupi.append(izomorfizem(latinski[i]))
    print(str(izomorfizem(latinski[i]))+ ',')
print(']')
