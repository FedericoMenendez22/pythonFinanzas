#PROBLEM SET 1
from math import exp,sqrt
from random import gauss,seed


def create_gbm(s0,mu,sigma):
    st = s0
    print("Paso 1: ST =",st)
    
    #FUNCION 2
    def generate_value():
        nonlocal st 
        print("Paso 2: ST =",st)
        st*=exp((mu-0.5*sigma**2)*(1./365.)+sigma*sqrt(1./365.)*gauss(0.,1.))
        print("Paso 3: ST =",st)
        return st

    print("Paso 4: ST =",st)
    return generate_value

if __name__ == '__main__':
    seed(1234) 

    #CREO LA FUNCION PERO NO EJECUTO LA FUNCION 2 
    print("INICIO CREATE GBM")
    gbm = create_gbm(100.,.1,.05)
    print("FIN CREATE GBM")

    for _ in range(1000):

         
        #EJECUTO FUNCION 2 
        print("INICIO GENERATE VALUE")
        valor1 = gbm()
        print("FIN GENERATE VALUE")

        if valor1 >= 130.:
            print("Alcanzado")
            break
    else:
        print("No Alcanzado")
    print(valor1)
    
        
  

    