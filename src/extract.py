import os
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

def download_data():
    """Download Spotify Dataset 2023 files from Kaggle."""
    api = KaggleApi()
    api.authenticate()
    dataset = "tonygordonjr/spotify-dataset-2023"
    os.makedirs("data", exist_ok=True)
    api.dataset_download_file(dataset, file_name="spotify-albums_data_2023.csv", path="data")
    api.dataset_download_file(dataset, file_name="spotify_tracks_data_2023.csv", path="data")
    for filename in os.listdir("data"):
      print(filename)
      if filename.endswith(".zip"):
        with zipfile.ZipFile(os.path.join("data", filename), 'r') as zip_ref:
            zip_ref.extractall("data")

if __name__ == "__main__":
    download_data()
