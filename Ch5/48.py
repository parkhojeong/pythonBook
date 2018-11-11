

def max(topHitters):
    maxHits = 0
    for key in topHitters.keys():
        if topHitters[key]["hits"] > maxHits:
            maxHits = topHitters[key]["hits"]
            maxPlayer = key
    return maxPlayer

def min(topHitters):
    minHits = 1000000
    for key in topHitters.keys():
        if topHitters[key]["hits"] < minHits:
            minHits = topHitters[key]["hits"]
            minPlayer = key
    return minPlayer

topHitters = {"Gehrig":{"atBats":8061 , "hits":2721},
              "Ruth": {"atBats": 8399, "hits": 2873},
              "Williams": {"atBats": 7706, "hits": 2654} }

del topHitters[max(topHitters)]
del topHitters[min(topHitters)]
print(topHitters)