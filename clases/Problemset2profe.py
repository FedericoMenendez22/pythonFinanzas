# -*- coding: utf-8 -*-
"""
Problem Set 2
"""


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

def tir(precio,capital,plazo, is_tea=True):
    if is_tea:
        return (capital / precio) ** (365. / plazo) - 1.
    else:
        return ((capital / precio) - 1.) * (365. / plazo)
        

def precio(tasa,capital,plazo,is_tea = True):
    if is_tea:
        return capital/((tasa+1.)) ** (plazo/365.)     
    else: 
        return capital/((tasa * plazo / 365.)+1.)
   
   
def tir_portfolio (mkt_data,port_weights, is_tea=True):
    return sum([tir(**mkt_data[lc], is_tea=is_tea) * lw for lc, lw in port_weights.items()])

def plazo_promedio(mkt_data, port_weights):
    return sum([mkt_data[lc]['plazo'] * lw for lc, lw in port_weights.items()])

def total_return(mkt_data, port_weights, horizon, shift_fuction, is_tea=True):
    port_ret = 0
    for lc, lw in port_weights.items():
        old_TIR = tir(**mkt_data[lc], is_tea=is_tea)
        new_plazo = mkt_data[lc]['plazo'] - horizon
        new_TIR = old_TIR + shift_fuction(new_plazo)
        new_price = precio(new_TIR, mkt_data[lc]['capital'], new_plazo, is_tea=is_tea)

        port_ret += (new_price / mkt_data[lc]['precio'] -1. ) * lw
    
    return port_ret
        

if __name__ == '__main__':
    import json
    

    data = json.load(open(r'C:\\Users\\FedericoMenendez\\Desktop\\PYTHON\\FinanzasPython\\data\\c3_mkt_data.json'))
    
    
    print("Portfolio Stats:")
    print("(valores promedio)")
    print("-------------------")
    print(f'TIR = {tir_portfolio(data["mercado"], data["portfolio"]):.2f}%')
    print(f'Plazo = {plazo_promedio(data["mercado"], data["portfolio"]):.2f}')
    sf = crea_shift_func(-500. , -500.)
    tr = total_return(data["mercado"], data["portfolio"], 15 , sf)
    print(f' TotRet = {tr:2%}')