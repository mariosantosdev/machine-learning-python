# 05/12/2018 - 18:50
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

# criando dataset
x = np.array([[0.0, 0.0], [0.0, 0.1], [0.25, 0.25], [0.3, 0.4], [0.5, 0.5]])# dataset input values
y = np.array([[0.0], [0.1], [0.5], [0.7], [1.0]])# dataset output values

model = Sequential()# criacao do tipo de layer

# adicionando layer(neuronios, valores de entrada, tipo de ativacao) 
model.add(Dense(5, input_dim=2, activation='sigmoid'))
model.add(Dense(5, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

# compilando o aprendizazdo(tipo de otimizador, tipo de erros, tipo de precisao)
model.compile(optimizer='adam', loss='mse', metrics=['acc'])
# treinando(dataset input, dataset output, epocas de treinamento)
model.fit(x, y, epochs=5000)
result = model.predict(x) # gerando o output
print(result)