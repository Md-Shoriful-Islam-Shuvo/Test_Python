#kmeans.py
def euclidian_distance(point_a, point_b):
    return (sum([(point_a[i] - point_b[i])**2 for i in range(len(point_a))]))**0.5


    
class KMeans:
    def __init__(self, k):
        self.k = k

    def find_cluster_centroid(self, points):
        centrioid = []
        for i in range(len(points[0])):
            temp = 0
            for j in range(len(points)):
                temp += points[j][i]
            centrioid.append(temp/len(points))
        return centrioid

    def fit(self, X_train):
        if self.k ==3:
            k1 = X_train[2]
            k2 = X_train[4]
            k3 = X_train[6]
        elif self.k == 4:
            k1 = X_train[2]
            k2 = X_train[4]
            k3 = X_train[6]
            k4 = X_train[8]
        elif self.k == 5:
            k1 = X_train[2]
            k2 = X_train[4]
            k3 = X_train[6]
            k4 = X_train[8]
            k5 = X_train[10]

        for i in range(self.k):
            distance=[]
            for j in range(len(X_train)):
                distance.append(euclidian_distance(X_train[i], X_train[j]))

            

                
        self.centroids = ...
    
    def predict(self, X_test):
        pass
    