from dataset import Dataset
from kmeans import kmeansCluster
from bisectingkmeans import bisectingkmeansCluster
from evaluate import purity, fscore
import distance
import time

dataset_path = 'Dataset/Frogs_MFCCs.csv'

def kmeans_test(dataset, method, k):
    print('===== ' + method + ' =====')
    time_start = time.time()
    if method == 'kmeans':
        kmeansCluster(dataset, distance.euler, k)
    elif method == 'bisectingkmeans':
        bisectingkmeansCluster(dataset, distance.euler, k)
    time_end = time.time()
    print('    Time cost: ', time_end - time_start)
    print('    Purity: ', purity(dataset))
    print('    F-score: ', fscore(dataset))

if __name__ == "__main__":
    dataset = Dataset()
    dataset.readFromFile(dataset_path, list(map(lambda x : 'MFCCs_' + str(x).rjust(2), list(range(1, 23)))), 'Family')

    kmeans_test(dataset, 'kmeans', 4)
    kmeans_test(dataset, 'bisectingkmeans', 4)
