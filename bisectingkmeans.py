import numpy as np

def bisectingkmeansCluster(dataset, dis, k):
    for i in range(0, k - 1):
        # Select a cluster from the list of clusters
        sse = [SSE(dataset, dis, c) for c in range(0, i + 1)]
        split_cluster = 0
        for j in range(0, len(sse)):
            if sse[j] > sse[split_cluster]:
                split_cluster = j
        
        # Bisect the selected cluster using basic K-means
        Bisect(dataset, dis, split_cluster, i + 1)

def SSE(dataset, dis, cluster):
    c = np.array([0.0] * len(dataset.data[0].val))
    n = 0
    for data in dataset.data:
        if data.cluster == cluster:
            c += data.val
            n += 1
    c /= n
    sse = 0
    for data in dataset.data:
        if data.cluster == cluster:
            sse += dis(data.val, c) * dis(data.val, c)
    return sse

def Bisect(dataset, dis, cluster, new_cluster):
    c = []
    for data in dataset.data:
        if data.cluster == cluster:
            c.append(data.val)
        if len(c) >= 2:
            break
    
    while True:
        for data in dataset.data:
            if data.cluster == cluster or data.cluster == new_cluster:
                if dis(c[0], data.val) < dis(c[1], data.val):
                    data.cluster = cluster
                else:
                    data.cluster = new_cluster
                    
        c_new = []
        for i in range(0, 2):
            centroid = np.array([0.0] * len(c[i]))
            n = 0
            for data in dataset.data:
                if data.cluster == [cluster, new_cluster][i]:
                    centroid += data.val
                    n += 1
            centroid /= n
            c_new.append(centroid)
        
        unchanged = True
        for i in range(0, 2):
            if not (c[i] == c_new[i]).all():
                unchanged = False
        if unchanged:
            break
        c = c_new
