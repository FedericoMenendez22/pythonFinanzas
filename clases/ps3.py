"""
Problem Set 3
"""


def pretty_print_fwd(fwd_struct):
    """
    Arma cuadro para visualizar una estructura forward.
    Parámetros:
        fwd_struct : Estructura de tasas forward
    """
    for t, fwds in fwd_struct.items():
        fwds_txt = ', '.join(f'{tt:3}: {r:6.2%}' for tt, r in fwds.items())
        print(f'{t:3}: {{', fwds_txt, '}')


if __name__ == '__main__':
    import json

    data = json.loads(open('C:\\Users\\FedericoMenendez\\Desktop\\PYTHON\\FinanzasPython\\data\\c4_mkt_data.json').read())   
    