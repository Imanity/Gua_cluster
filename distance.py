import math

def euler(a, b):
    dis = 0
    for i in range(0, len(a)):
        dis += (a[i] - b[i]) * (a[i] - b[i])
    dis = math.sqrt(dis)
    return dis
