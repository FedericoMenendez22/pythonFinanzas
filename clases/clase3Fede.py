# -*- coding: utf-8 -*-
"""
Clase 3: Trabajando con Letras ARS
"""


def tea(precio, capital, plazo):
    """
    Calcula la TEA de una letra.
    Parámetros:
        precio  : Precio de la letra cada 100 VN.
        capital : Monto de capital que devuelve la letra cada 100 VN.
        plazo   : Plazo residual en días.
    """
    return (capital / precio) ** (365 / plazo) - 1


def tna(precio, capital, plazo):
    """
    Calcula la TNA de una letra.
    Parámetros:
        precio  : Precio de la letra cada 100 VN.
        capital : Monto de capital que devuelve la letra cada 100 VN.
        plazo   : Plazo residual en días.
    """
    return ((capital / precio) - 1) * (365 / plazo)


if __name__ == '__main__':
    import json

    data = json.load(open(r'..\Data\letras.json'))

    
    for lc, ld in data['mercado'].items():
        # Debajo **ld funciona sólo si ld es un dict que tiene las mismas
        # etiquetas que los nombres de los parámteros de la función. Hace
        # tea(ld['precio'], ld['capital'], ld['plazo']) de forma automática.
        irr = tea(**ld)
        # Si ld en vez de un dict fuese una list de tantos elementos como
        # parámetros tenga la función, en nuestro caso 3, por ejemplo
        # [90.25, 100.0, 7] (importante aquí el ordenamiento) podríamos llamar
        # a la función tea(*ld). Notar el uso de 1 SOLO asterisco en vez de 2.
        print(f'{lc} - TEA = {irr:7.2%} - Plazo = {ld["plazo"]:3}')