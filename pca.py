from dataset import Dataset
import numpy as np

dataset_path = 'Dataset/Frogs_MFCCs.csv'
output_path = 'Dataset/pca_result/Frogs_MFCCs_pca_'

if __name__ == "__main__":
    dataset = Dataset()
    dataset.readFromFile(dataset_path, ['MFCCs_' + str(x).rjust(2) for x in list(range(1, 23))], 'Family')

    m = len(dataset.data[0].val)
    n = len(dataset.data)
    X = np.mat(np.zeros((m, n)))

    for j in range(0, n):
        for i in range(0, m):
            X[i, j] = dataset.data[j].val[i]

    for i in range(0, m):
        c = 0
        for j in range(0, n):
            c += X[i, j]
        c /= n
        for j in range(0, n):
            X[i, j] -= c
    
    C = X * X.T
    C /= m

    evals, evecs = np.linalg.eig(C)
    sorted_indices = np.argsort(evals)

    for k in range(1, 22):
        topk_evecs = evecs[:, sorted_indices[:-k-1:-1]].T
        Y = topk_evecs * X

        for i in range(0, n):
            dataset.data[i].val = np.array(np.array(Y[:,i]).flatten())
        
        dataset.writeToFile(output_path + str(k) + '.csv')
