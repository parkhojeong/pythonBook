def max(topHitters):
    maxHits = 0
    for key in topHitters.keys():
        if topHitters[key]["hits"] > maxHits:
            maxHits = topHitters[key]["hits"]
    return maxHits

topHitters = {"Gehrig":{"atBats":8061 , "hits":2721},
              "Ruth": {"atBats": 8399, "hits": 2873},
              "Williams": {"atBats": 7706, "hits": 2654} }

print("The most hits by one of the baseball players was ",max(topHitters),".",sep="")