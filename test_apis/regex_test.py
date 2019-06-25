import re

if __name__ == '__main__':
    string = "PESIMA ATENCION LA DE TIGO.  Firme contrato el 17 de enero con Mirian Elizabeth Cordero Durán de renovaciones, con un cambio a pagar por $38.41  y  a la  fecha me siguen cobrando mas de $60. dolares,  NO ME DAN RESPUESTA, HE LLAMADO TELEFONICAMENTE, POR CORREO Y SIGO ESPERANDO. \nES UN EJEMPLO TIPICO DE PUBLICIDAD ENGAÑOSA QUE NO CUMPLEN CON LO QUE PROMETEN Y UNA PESIMA ATENCION AL CLIENTE"
    string = re.sub('\n', ' ', string)
    print(string.encode('latin-1', errors='replace'))