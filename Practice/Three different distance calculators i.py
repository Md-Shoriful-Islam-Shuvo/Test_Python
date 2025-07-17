# three different distance calculators in machine learning
def distances_option_calculator(X, y, distance_type):
    # Write code here
    if distance_type == "euclidian":
        distance = 0
        for i in range(len(X)):
            distance += (X[i] - y[i]) ** 2
        return "{:.1f}".format(distance**0.5)

    elif distance_type == "manhattan":
        distance = 0
        for i in range(len(X)):
            distance += abs(X[i] - y[i])
        return distance
    elif distance_type == "hamming":
        distance = 0
        for i in range(len(X)):
            if X[i] != y[i]:
                distance += 1
        return distance
    
# Example usage
X = [1, 2, 3]
y = [4, 5, 6]
distance_type = "euclidian"
print(distances_option_calculator(X, y, distance_type))  # Output: 5.2
distance_type = "manhattan"
print(distances_option_calculator(X, y, distance_type))  # Output: 9
distance_type = "hamming"
print(distances_option_calculator(X, y, distance_type))  # Output: 3