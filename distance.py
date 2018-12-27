import math

def euler(a, b):
    dis = 0
    for i in range(0, len(a)):
        dis += (a[i] - b[i]) * (a[i] - b[i])
    dis = math.sqrt(dis / len(a))
    return dis

def cosine(a, b):
    aTb = 0
    al = 0
    bl = 0
    for i in range(0, len(a)):
        aTb += a[i] * b[i]
        al += a[i] * a[i]
        bl += b[i] * b[i]
    discos = aTb / (math.sqrt(al) * math.sqrt(bl))
    if discos > 1.0:
        discos = 1.0
    if discos < -1.0:
        discos = -1.0
    dis = math.acos(discos)
    return dis

def pearson(a, b):
    a_avg = 0
    b_avg = 0
    for i in range(0, len(a)):
        a_avg += a[i]
        b_avg += b[i]
    a_avg /= len(a)
    b_avg /= len(b)
    cov = 0
    da = 0
    db = 0
    for i in range(0, len(a)):
        cov += (a[i] - a_avg) * (b[i] - b_avg)
        da += (a[i] - a_avg) * (a[i] - a_avg)
        db += (b[i] - b_avg) * (b[i] - b_avg)
    pab = cov / (math.sqrt(da) * math.sqrt(db))
    return 1 - pab
