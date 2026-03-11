import os
import requests

class Downloader:
    def __init__(self, url_servidor: str, pasta: str):
        self.url_servidor = url_servidor
        self.pasta = pasta
        os.makedirs(self.pasta, exist_ok=True)

    def download(self,nome:str):
        url = self.url_servidor.format(nome)
        response = requests.get(url)
        caminho = os.path.join(self.pasta, f"{nome}.zip")

        if response.status_code == 200:
            with open(caminho, 'wb') as arquivo:
                arquivo.write(response.content)
            print('Arquivo foi baixado')
        else:
            print('Falha em baixar o arquivo')

if __name__ == "__main__":

    teste = Downloader ("https://geoftp.ibge.gov.br/cartas_e_mapas/folhas_topograficas/vetoriais/escala_1000mil/shapefile/{}.zip",r"D:\carto\progcart\progcartfavalessa\downloader")

    print (dir(teste))

    teste.download("g04_na19")