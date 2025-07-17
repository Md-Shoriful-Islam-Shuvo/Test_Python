# simple KNN classifier
#import numpy as np
class KNN:
    def __init__(self, k):
        self.points = None
        self.labels = None
        self.k = k
    
    def distance(self, point_a, point_b):
        distance = 0
        for i in range(len(point_a)):
            distance += (point_a[i] - point_b[i]) ** 2
        return distance ** 0.5
    def fit(self, X_train, y_train):
        self.points = X_train
        self.labels = y_train

    def predict(self, X_test):
        predictions = []
        for test_point in X_test:
            distances = []
            for i, point in enumerate(self.points):
                distances.append((self.distance(test_point, point), self.labels[i]))
            distances.sort(key=lambda x: x[0])
            neighbors = [distances[i][1] for i in range(self.k)]
            predictions.append(max(set(neighbors), key=neighbors.count))
       # return np.array(predictions)
        return predictions
    
# Example usage
if __name__ == "__main__":
    # Sample data
    X_train = [[1, 2], [2, 3], [3, 4], [5, 6]]
    y_train = [0, 0, 1, 1]
    X_test = [[1, 2], [4, 5]]   # Sample test data  
    # Create KNN classifier
    knn = KNN(k=3)
    # Fit the model
    knn.fit(X_train, y_train)
    # Make predictions
    predictions = knn.predict(X_test)
    # Print predictions
    print("Predictions:", predictions)