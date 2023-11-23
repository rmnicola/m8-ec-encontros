import numpy as np

class Perceptron:
    def __init__(self, weights, threshold):
        self.weights = np.array(weights)
        self.threshold = threshold
        self.bias = 0

    def activation_function(self, x):
        return 1 if x >= self.threshold else 0

    def predict(self, inputs):
        # Calcula a soma ponderada das entradas
        linear_output = np.dot(inputs, self.weights) + self.bias
        # Aplica a função degrau para determinar a saída
        y_predicted = self.activation_function(linear_output)
        return y_predicted

# Exemplo de uso
if __name__ == "__main__":
    # Pesos para: tempo, companhia do namorado/namorada, proximidade do transporte público
    weights = [6, 2, 2]  # O peso do tempo é maior, indicando maior importância
    threshold = 5  # Limiar para a decisão

    # Cria o perceptron com os pesos e limiar pré-definidos
    perceptron = Perceptron(weights, threshold)

    # Testa o perceptron com diferentes entradas
    print(perceptron.predict(np.array([1, 0, 0])))  # Bom tempo, sem companhia, longe do transporte
    print(perceptron.predict(np.array([0, 1, 1])))  # Tempo ruim, com companhia, perto do transporte
    print(perceptron.predict(np.array([1, 1, 1])))  # Bom tempo, com companhia, perto do transporte
