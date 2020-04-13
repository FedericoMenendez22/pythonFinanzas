# -*- coding: utf-8 -*-
"""
Problem Set 2
"""
from finpylib.calc_fin import tea,tna

def crea_shift_func(bpsShort, bpsLong):
    """
    Crea función desplazamiento.
    Parámetros:
        bpsShort : Puntós Básicos deplazamiento en tasa 0 días (parte corta)
        bpsLong  : Puntós Básicos deplazamiento en tasa 365 días (parte larga)

    NOTA: 100 Puntos Básicos = 1.00 %
    """
    def shift_func(plazo):
        """
        Devuelve la magnitud del cambio de yield para un plazo determinado.
        Parámetros:
            plazo : Plazo expresado en días.

        NOTA: Realiza interpolación lineal. De sólo uso entre 0 y 365 días.
        """
        return ((bpsLong - bpsShort) * (plazo / 365) + bpsShort) / 10000.0

    return shift_func

def calcula_tir_letra (precio,capital,plazo,tipo_tasa):
    if (tipo_tasa):
        #Calcula T.E.A
        tir = tea(precio,capital,plazo)
    else:
        #Calcula T.N.A
        tir = tna(precio,capital,plazo)
    return tir

def precio_letra (tir,capital,plazo,tipo_tasa):
    if (tipo_tasa):
        #Calcula T.E.A
        precio = capital/((tir+1.)) ** (plazo/365.)
    else:
        #Calcula T.N.A
        precio = capital/((tir * plazo / 365.)+1.)
    return precio

def tir_promedio_portfolio (mercado_dict,portfolio_dict,tipo_tasa):
    if (tipo_tasa):
        #Calcula T.E.A
        dict_variable = {letra:calcula_tir_letra(ld['precio'], ld['capital'], ld['plazo'],1)*portfolio_dict[letra] for (letra , ld) in mercado_dict.items() if letra in portfolio_dict}
        promedio_ponderado = 100 * (sum(dict_variable.values())/sum(portfolio_dict.values()))
    else:
        dict_variable = {letra:calcula_tir_letra(ld['precio'], ld['capital'], ld['plazo'],0)*portfolio_dict[letra] for (letra , ld) in mercado_dict.items() if letra in portfolio_dict}
        promedio_ponderado = 100 * sum(dict_variable.values())/len(dict_variable)
    return promedio_ponderado


def plazo_promedio_ponderado(mercado_dict,portfolio_dict):
    dict_variable = {letra:ld['plazo']*portfolio_dict[letra] for (letra , ld) in mercado_dict.items() if letra in portfolio_dict}
    return sum(dict_variable.values())
   

def total_return(mercado_dict,portfolio_dict,tiempo_dias,cambioDeCurva,tipo_tasa):
        totalReturnPortfolio = 0
        for (letra , ld) in mercado_dict.items():
            if letra in portfolio_dict:
                tir = calcula_tir_letra (ld['precio'],ld['capital'],ld['plazo'],tipo_tasa)
                plazo_futuro = ld['plazo'] -15 
                tir_futura = tir - 0.05
                totalReturnLetra = precio_letra(tir_futura,ld['capital'],plazo_futuro,tipo_tasa) / ld['precio'] - 1    
                totalReturnPortfolio = totalReturnPortfolio + (totalReturnLetra * portfolio_dict[letra])
        return totalReturnPortfolio
        
        



if __name__ == '__main__':
    import json

    data = json.loads(open('C:\\Users\\FedericoMenendez\\Desktop\\PYTHON\\FinanzasPython\\data\\letras.json').read())   
   
    tir = tir_promedio_portfolio(data['mercado'],data['portfolio'],1)
    plazo = plazo_promedio_ponderado(data['mercado'],data['portfolio'])
    totalReturnSumatoria = total_return(data['mercado'],data['portfolio'],15,crea_shift_func(0, 500),1)
    
    

    print("Portfolio Stats:")
    print("(valores promedio)")
    print("-------------------")
    print(f'TIR = {tir:.2f}%')
    print(f'Plazo = {plazo:.2f}')
    print(f'TotRet = {totalReturnSumatoria:.2%}')  
    
       
   
        


