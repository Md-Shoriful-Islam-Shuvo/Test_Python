#Simple machine learning model to predict y values from x values
class SimpleModel:
    def __init__(self):
        self.mode = {}

    def fit(self, X, y):
        for i in range(len(X)):
            if X[i] not in self.mode:
                self.mode[X[i]] = None
                value = 0
                t = 0
                for j in range(len(X)):
                    if X[i] == X[j]:
                        t +=1
                        value += y[j]
                self.mode[X[i]] = round(value/t)
            
        

    def predict(self, X):
        predictions = []
        for i in range(len(X)):
            if X[i] in self.mode:
                predictions.append(self.mode[X[i]])
            else:
                predictions.append(None)
        return predictions

def train_and_predict(X_train, y_train, X_test):
    model = SimpleModel()
    model.fit(X_train, y_train)  # Train the model with X_train and y_train
    
    return model.predict(X_test)  # Predict using the trained model on X_test
# Example usage
if __name__ == "__main__":
    X_train = ['A', 'A', 'A', 'C', 'C']
    y_train = [1, 0, 1, 1, 1]
    X_test = ['C', 'B']

    predictions = train_and_predict(X_train, y_train, X_test)
    print(predictions)  # Output: [10, 20, 30, None]