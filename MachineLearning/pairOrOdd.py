# Par ou Impar 70% eficaz
from pybrain3.datasets import SupervisedDataSet
from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.supervised.trainers import BackpropTrainer
import numpy

net = buildNetwork(1, 3, 1)
ds = SupervisedDataSet(1, 1)

ds.addSample((1), (0, ))
ds.addSample((3), (0, ))
ds.addSample((5), (0, ))
ds.addSample((7), (0, ))
ds.addSample((9), (0, ))

ds.addSample((0), (1, ))
ds.addSample((2), (1, ))
ds.addSample((4), (1, ))
ds.addSample((6), (1, ))
ds.addSample((8), (1, ))

trainer = BackpropTrainer(net, dataset=ds, learningrate=0.01, momentum=0.06)

for i in range(1, 100001):
    erro = trainer.train()
    if i % 1000 == 00:
        print(f'[{i}] Taxa de erro: {erro} %')

while True:
    num = int(input('Digite um numero de 0 a 9: '))
    if num > 9:
        num = int(input('Digite um numero de 0 a 9: '))
    elif num < 0:
        num = int(input('Digite um numero de 0 a 9: '))
    else:
        r = numpy.ndarray.round(net.activate([num]))

        if(r == 0):
            print(f'O valor {num} e IMPAR')
        else:
            print(f'O valor {num} e PAR')