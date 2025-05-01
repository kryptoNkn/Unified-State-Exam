data = []
for s in open('27'):
    x,y = [float(a) for a in s.split()]
    data.append([x,y])

from math import *

clusters = []
while data:
    cl = [data.pop()]
    for p in cl:
        sosed = [p1 for p1 in data if dist(p,p1)<1.5]
        for p1 in sosed:
            cl.append(p1)
            data.remove(p1)
    clusters.append(cl)

def centroid (cl):
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return min(m)[1]

cen = [centroid(cl) for cl in clusters]
px = sum(x for x,y in cen)/len(cen)
py = sum(y for x,y in cen)/len(cen)
print(abs(int(px*10000)), abs(int(py*10000)))

# 32540 13646
# 47031 25263