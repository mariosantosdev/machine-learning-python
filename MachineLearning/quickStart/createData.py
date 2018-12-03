# 02/122018 - 20:42
from pybrain3.datasets import SupervisedDataSet

# criando dataSet
ds = SupervisedDataSet(2, 1) # entrada bidimensional, saida unidimensional

# adicionando amostras
ds.addSample((0, 0), (0))
ds.addSample((0, 1), (1))
ds.addSample((1, 0), (1))
ds.addSample((1, 1), (0))

# examinando o data set
print(len(ds)) # retorna a quantidade de amostras
print(ds['input']) # retorna um array com valores de entrada
print(ds['target']) # retorna um array com valores objetivos
ds.clear() # limpa o dataSet