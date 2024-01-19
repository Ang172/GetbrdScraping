import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#topics = "pokemon","python","genshin"
topics = "arduino","electronica"

def scraping(topic):

    # Ingresar la URL de la página web que deseas scrapear
    url = "https://socialblade.com/youtube/top/tag/" + topic + "/subscribers"  # Reemplaza con la URL real

    # Realizar una solicitud HTTP para obtener el contenido de la página
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})

    # Verificar que la solicitud se haya realizado correctamente
    if response.status_code == 200:
        # Obtener el contenido HTML de la página
        html = response.text

        # Crear un objeto BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        # Lista de estilos a buscar
        styles_to_find = [
            'width: 860px; background: #f8f8f8;; padding: 10px 20px; color:#444; font-size: 10pt; border-bottom: 1px solid #eee; line-height: 30px;',
            'width: 860px; background: #fafafa; padding: 10px 20px; color:#444; font-size: 10pt; border-bottom: 1px solid #eee; line-height: 30px;'
        ]

        # Buscar los elementos <div> con los estilos especificados
        channel_divs = soup.find_all('div', style=lambda value: value in styles_to_find)

        # Inicializar una lista para almacenar los datos de los canales
        channels_data = []

        # Iterar a través de los elementos div para extraer la información
        for div in channel_divs:
            # Encontrar elementos div dentro de este div
            sub_divs = div.find_all('div', recursive=False)

            # Extraer los datos de los divs internos
            position = sub_divs[0].text.strip()
            channel_info = sub_divs[2]
            channel_name = channel_info.find('a').text.strip()
            subscribers = sub_divs[3].text.strip()
            views = sub_divs[4].text.strip()
            total_views = sub_divs[5].text.strip()

            # Crear un diccionario con la información y agregarlo a la lista
            channel_data = {
                'position': position,
                'channelName': channel_name,
                'subscribers': subscribers,
                'views': views,
                'totalViews': total_views
            }
            channels_data.append(channel_data)

        # Imprimir los datos de los canales
        
        graphic(channels_data)
        #print(channels_data)
        
        #for channel in channels_data:
            #print(channel)

    else:
        print("No se pudo acceder a la página:", response.status_code)

def graphic(channels_data_local):
    # Extraer los datos de suscriptores, vistas y vistas totales
    subscribers = [int(data['subscribers'].replace(',', '')) for data in channels_data_local]
    views = [int(data['views'].replace(',', '')) for data in channels_data_local]
    #total_views = [int(data['totalViews'].replace(',', '')) for data in channels_data_local]

    # Crear una figura y ejes para la visualización
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 12))

    # Visualización de suscriptores
    axes[0].bar([data['channelName'] for data in channels_data_local], subscribers)
    axes[0].set_title('Suscriptores')
    axes[0].set_ylabel('Cantidad')

    # Visualización de vistas
    axes[1].bar([data['channelName'] for data in channels_data_local], views, color='orange')
    axes[1].set_title('Vistas')
    axes[1].set_ylabel('Cantidad')

    # Visualización de vistas totales
    #axes[2].bar([data['channelName'] for data in channels_data_local], total_views, color='green')
    #axes[2].set_title('Vistas Totales')
    #axes[2].set_ylabel('Cantidad')

    # Rotar los nombres de los canales en el eje x para una mejor visualización
    for ax in axes:
        ax.tick_params(axis='x', rotation=45)

    # Ajustar el espacio entre las subtramas para evitar solapamientos
    plt.tight_layout()

    # Mostrar la visualización
    plt.show()

for caracter in topics:
    scraping(caracter)