import numpy as np

def kmeansCluster(dataset, dis, k):
    c = []
    for i in range(0, k):
        c.append(dataset.data[i].val)
    
    while True:
        # Form k clusters by assigning all points to the closest centroid
        for data in dataset.data:
            distances = [dis(x, data.val) for x in c]
            for i in range(0, len(distances)):
                if (distances[i] < distances[data.cluster]):
                    data.cluster = i
        
        # Recompute the centroid of each cluster
        c_new = []
        for i in range(0, len(c)):
            centroid = np.array([0.0] * len(c[i]))
            n = 0
            for data in dataset.data:
                if data.cluster == i:
                    centroid += data.val
                    n += 1
            centroid /= n
            c_new.append(centroid)
        
        # Repeat until the centroids don't change
        unchanged = True
        for i in range(0, len(c)):
            if not (c[i] == c_new[i]).all():
                unchanged = False
        if unchanged:
            break
        c = c_new
