import requests

def obtener_precio_criptomoneda(criptomoneda):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={criptomoneda}&vs_currencies=usd'
    respuesta = requests.get(url)
    datos = respuesta.json()
    if criptomoneda in datos:
        precio = datos[criptomoneda]['usd']
        return precio
    else:
        return None

if __name__ == '__main__':
    nombre_criptomoneda = input('Ingresa el nombre de la criptomoneda que deseas consultar: ').lower()
    precio = obtener_precio_criptomoneda(nombre_criptomoneda)
    if precio is not None:
        print(f'El precio actual de {nombre_criptomoneda.capitalize()} es: ${precio} USD')
    else:
        print('La criptomoneda no se ha encontrado.')
