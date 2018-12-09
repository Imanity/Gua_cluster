def purity(dataset):
    # Number of data
    N = len(dataset.data)
    # Number of clusters
    K = 0
    for data in dataset.data:
        if data.cluster >= K:
            K = data.cluster + 1
    # Number of classes
    J = len(dataset.keys)
    # Sum of max wk^cj
    s = 0
    for k in range(0, K):
        c = [0] * J
        for data in dataset.data:
            if data.cluster == k:
                c[dataset.keys.index(data.key)] += 1
        s += max(c)
    return s / N

def fscore(dataset):
    TP = 0
    FP = 0
    FN = 0
    TN = 0
    # Number of data
    N = len(dataset.data)
    for i in range(0, N):
        for j in range(0, N):
            if i == j:
                continue
            if dataset.data[i].cluster == dataset.data[j].cluster:
                if dataset.data[i].key == dataset.data[j].key:
                    TP += 1
                else:
                    FP += 1
            else:
                if dataset.data[i].key == dataset.data[j].key:
                    FN += 1
                else:
                    TN += 1
    beita = 1.0
    P = TP / (TP + FP)
    R = TP / (TP + FN)
    return (beita * beita + 1) * P * R / (beita * beita * P + R)
