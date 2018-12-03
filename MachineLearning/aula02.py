# https://www.youtube.com/watch?v=6HpBUzpXzIA
from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.datasets import SupervisedDataSet
from pybrain3.supervised.trainers import BackpropTrainer
from pybrain3.structure.modules import SoftmaxLayer, SigmoidLayer
import decimal, numpy

'''net = buildNetwork(2, 3, 1, outclass= SoftmaxLayer,
                            hiddenclass=SigmoidLayer, 
                            bias=False)
 print(net['in'])
 print(net['hidden0'])
 print(net['out'])'''

net = buildNetwork(2, 3, 1)
ds = SupervisedDataSet(2, 1)
ds.addSample((0, 0), (0, ))
ds.addSample((0, 1), (1, ))
ds.addSample((1, 0), (1, ))
ds.addSample((1, 1), (0, ))
# print(ds['input'])
# print(ds['target'])

trainer = BackpropTrainer(net, dataset=ds, learningrate=0.01, momentum=0.06)

for i in range(1, 30001):
    erro = trainer.train()
    if i % 1000 == 00:
        print(f'[{i}] Taxa de erro: {erro:.8f} %') 

print(numpy.ndarray.round(net.activate([0, 0])))
print(numpy.ndarray.round(net.activate([0, 1])))
print(numpy.ndarray.round(net.activate([1, 0])))
print(numpy.ndarray.round(net.activate([1, 1])))