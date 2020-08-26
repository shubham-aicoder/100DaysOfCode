def apartmentHunting(blocks, reqs):
    maxDistanceAtBlocks = [float('-inf') for block in blocks]
    for i in range(len(blocks)):
        for req in reqs:
            closestReqDistance = float('inf')
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestReqDistance = min(closestReqDistance, distanceBetween(i, j))
            maxDistanceAtBlocks[i] = max(maxDistanceAtBlocks[i], closestReqDistance)
    return getIndexAtMinValue(maxDistanceAtBlocks)


def distanceBetween(i, j):
    return abs(i - j)


def getIndexAtMinValue(array):
    idxAtMinValue = 0
    minValue = float('inf')
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            idxAtMinValue = i
            minValue = currentValue
    return idxAtMinValue

blocks = [
 {"gym": False, "school": True, "store": False},
 {"gym": True, "school": False, "store": False},
 {"gym": True, "school": True, "store": False},
 {"gym": False, "school": True, "store": False},
 {"gym": False, "school": True, "store": True}
]
reqs = ["gym", "school", "store"]
print(apartmentHunting(blocks,reqs))
