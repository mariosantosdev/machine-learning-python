# 02/12/2018 - 20:49
from pybrain3.supervised.trainers import BackpropTrainer
from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.datasets import SupervisedDataSet

net = buildNetwork(2, 3, 1) # 2 input, 3 ocultas, 1 output
ds = SupervisedDataSet(2, 1) # entrada bidimensional, saida unidimensional

ds.addSample((0, 0), (0))
ds.addSample((0, 1), (1))
ds.addSample((1, 0), (1))
ds.addSample((1, 1), (0))

trainer = BackpropTrainer(net, ds) # definindo a net e o dataSet
trainer.train() # treinando
''' TREINAR ATé A CONVERGêNCIA
  trainer.trainUntilConvergence()'''

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
print(net.activate([n1, n2]))
print('-'*15)