from dataset import Dataset
from kmeans import kmeansCluster
from bisectingkmeans import bisectingkmeansCluster
from clique import cliqueCluster
from evaluate import purity, fscore
import distance
import time

dataset_path = 'Dataset/Frogs_MFCCs.csv'
dataset_3_path = 'Dataset/pca_result/Frogs_MFCCs_pca_3.csv'

def cluster_test(dataset, method, arg1, arg2 = 0):
    for data in dataset.data:
        data.cluster = 0
    print('===== ' + method + ' =====')
    time_start = time.time()
    if method == 'kmeans':
        kmeansCluster(dataset, distance.euler, arg1)
    elif method == 'bisectingkmeans':
        bisectingkmeansCluster(dataset, distance.euler, arg1)
    elif method == 'clique':
        cliqueCluster(dataset, arg1, arg2)
    time_end = time.time()
    print('    Time cost: ', time_end - time_start)
    print('    Purity: ', purity(dataset))
    #print('    F-score: ', fscore(dataset))

if __name__ == "__main__":
    dataset = Dataset()
    dataset.readFromFile(dataset_path, ['MFCCs_' + str(x).rjust(2) for x in list(range(1, 23))], 'Family')

    dataset3 = Dataset()
    dataset3.readFromFile(dataset_3_path, ['MFCCs_' + str(x).rjust(2) for x in list(range(1, 4))], 'Family')
    
    cluster_test(dataset3, 'clique', 0.1, 5)
