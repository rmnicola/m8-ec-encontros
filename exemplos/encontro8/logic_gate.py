import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, n_iterations=100, threshold=0.5):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.threshold = threshold
        self.weights = np.zeros(2)
        self.bias = 0

    def activation_function(self, x):
        return 1 if x >= self.threshold else 0

    def predict(self, inputs):
        # Calcula a soma ponderada das entradas
        linear_output = np.dot(inputs, self.weights) + self.bias
        # Aplica a função degrau para determinar a saída
        y_predicted = self.activation_function(linear_output)
        return y_predicted

    def train(self, X, y):
        for _ in range(self.n_iterations):
            for x, y_true in zip(X, y):
                y_pred = self.predict(x)
                error = y_true - y_pred
                self.weights += error * self.learning_rate * x
                self.bias += error * self.learning_rate

# Exemplo de uso
if __name__ == "__main__":
    # Dados para a porta AND
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    # y = np.array([0, 0, 0, 1]) 
    # y = np.array([0, 1, 1, 1])  
    # y = np.array([1, 1, 1, 0])
    y = np.array([0, 1, 1, 0])

    # Treinando o Perceptron
    perceptron = Perceptron()
    perceptron.train(X, y)

    # Testando o Perceptron
    print(f"in (0, 0), out: {perceptron.predict([0, 0])}")
    print(f"in (0, 1), out: {perceptron.predict([0, 1])}")
    print(f"in (1, 0), out: {perceptron.predict([1, 0])}")
    print(f"in (1, 1), out: {perceptron.predict([1, 1])}")
