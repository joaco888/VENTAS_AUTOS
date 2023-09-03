import pandas as pd
import gdown

class DataCapture:
    def __init__(self, url):
        self.url = url
        self.dataframe = None

    def capture(self):
        # Convertir la URL de Google Drive para que sea compatible con gdown
        file_id = self.url.split('/')[-2]
        gdown_url = f'https://drive.google.com/uc?id={file_id}'
        
        # Descargar el archivo CSV
        gdown.download(gdown_url, 'temp.csv', quiet=False)
        
        # Cargar el archivo CSV en un DataFrame
        self.dataframe = pd.read_csv('temp.csv')
        return self
