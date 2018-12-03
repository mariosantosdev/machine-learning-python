# https://www.youtube.com/watch?v=BKdKfcP1dP0
from pybrain3.structure import FeedForwardNetwork, LinearLayer
from pybrain3.structure import SigmoidLayer, BiasUnit, FullConnection

rede = FeedForwardNetwork()

camadaEntrada = LinearLayer(2)
camadaOculta = SigmoidLayer(3)
camadaSaida = SigmoidLayer(1)
bais1 = BiasUnit()
bais2 = BiasUnit()

rede.addModule(camadaEntrada)
rede.addModule(camadaEntrada)
rede.addModule(camadaSaida)
rede.addModule(bais1)
rede.addModule(bais2)

entradaOculta = FullConnection(camadaEntrada, camadaOculta)
ocultaSaida = FullConnection(camadaOculta, camadaSaida)
baisOculta = FullConnection(bais1, camadaOculta)
baisSaida = FullConnection(bais2, camadaSaida)

rede.sortModules()

print(rede)
print(entradaOculta.params)
print(ocultaSaida.params)
print(baisOculta.params)
print(baisSaida.params)