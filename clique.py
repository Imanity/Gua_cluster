import numpy as np
import queue

def cliqueCluster(dataset, step, threshold):
    n = len(dataset.data)
    m = len(dataset.data[0].val)

    # Shape of grid
    dim_len = np.zeros(m)
    min_val_list = []
    for i in range(0, m):
        min_val = dataset.data[0].val[i]
        max_val = dataset.data[0].val[i]
        for j in range(0, n):
            if dataset.data[j].val[i] < min_val:
                min_val = dataset.data[j].val[i]
            if dataset.data[j].val[i] > max_val:
                max_val = dataset.data[j].val[i]
        min_val_list.append(min_val)
        dim_len[i] = max_val - min_val
    shape = tuple(np.ceil(dim_len / step).astype(int))

    # Grid initialize
    density = np.zeros(shape)
    flag = np.full(shape, False)
    idx = [tuple(np.floor((data.val - np.array(min_val_list)) / step).astype(int)) for data in dataset.data]
    for i in range(0, len(dataset.data)):
        density[idx[i]] += 1
    dense = (lambda x : x > threshold)(density)
    cluster = np.zeros(shape, dtype = int)
    
    # Traverse the grid
    it = np.nditer(dense, flags=['multi_index'])
    current_cluster = 1
    while not it.finished:
        current_idx = it.multi_index
        if flag[current_idx]:
            it.iternext()
            continue
        flag[current_idx] = True
        if not dense[current_idx]:
            continue
        cluster[current_idx] = current_cluster
        q = queue.Queue()
        q.put(current_idx)
        while not q.empty():
            curr_idx = q.get()
            neighbors = neighbor(curr_idx, shape)
            for neighbor_idx in neighbors:
                if flag[neighbor_idx]:
                    continue
                flag[neighbor_idx] = True
                if dense[neighbor_idx]:
                    cluster[neighbor_idx] = current_cluster
                    q.put(neighbor_idx)
        current_cluster += 1
        it.iternext()
    
    # Label cluster
    for i in range(0, len(dataset.data)):
        dataset.data[i].cluster = cluster[idx[i]]


def neighbor(idx, shape):
    m = len(shape)
    neighbors = []
    for i in range(0, m):
        left = list(idx)
        left[i] -= 1
        if left[i] >= 0:
            neighbors.append(tuple(left))
        right = list(idx)
        right[i] += 1
        if right[i] < shape[i]:
            neighbors.append(tuple(right))
    return neighbors
