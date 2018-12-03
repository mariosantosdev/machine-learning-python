# 02/12/2018 - 20:33
from pybrain3.tools.shortcuts import buildNetwork

# crinado uma rede neural
net = buildNetwork(2, 3, 1) # 2 input, 3 ocultas, 1 output

# ativando uma rede neural
print(net.activate([2, 1]))

# examinando uma rede neural
print(net['in']) # camanda de entrada
print(net['hidden0']) # camada oculta (numero no final de acordo com a camada)
print(net['out']) # camada de saida
