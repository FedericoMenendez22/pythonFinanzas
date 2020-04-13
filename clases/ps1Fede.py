#PROBLEM SET 1

import math as mt
from random import gauss,seed

#Crea un generador de valores de un Geometric Brownian Motion
def precioSimulado(precioInicial,media,volatilidad):
    def generadorDeValoresDeUnGeometricBrownianMotion():
        return precioInicial * mt.exp ((media - .5 * volatilidad**2) * (1./365.) + volatilidad * mt.sqrt(1./365.) * gauss(0., 1.))
    return generadorDeValoresDeUnGeometricBrownianMotion()


if __name__ == "__main__":
    seed(1234)
    iteracion = 0
    precioAccion = 100
    volatilidad = 0.05
    media = 0.1
    precioAccionActual = 0
    while iteracion < 1000:
        precioAccionActual = precioSimulado(precioAccion,.1,0.05)
        precioAccion = precioAccionActual
        if precioAccion >= 130:
            print("Target alcanzado. Toma de Ganancia.")
            print(precioAccion)
            print(iteracion)
            break
        iteracion += 1 # iteracion = iteracion + 1
    
    if precioAccion < 130:
        print("Target no alcanzado.")
        print(precioAccion)
        print(iteracion)




