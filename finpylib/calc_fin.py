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
    return (capital / precio) ** (365. / plazo) - 1.


def tna(precio, capital, plazo):
    """
    Calcula la TNA de una letra.
    Parámetros:
        precio  : Precio de la letra cada 100 VN.
        capital : Monto de capital que devuelve la letra cada 100 VN.
        plazo   : Plazo residual en días.
    """
    return ((capital / precio) - 1.) * (365. / plazo)


