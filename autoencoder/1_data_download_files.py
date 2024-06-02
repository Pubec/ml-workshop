"""
Download files from an API
"""

import os
import requests
import shutil
from time import sleep
from tqdm import tqdm


width = 148
nr = 200
folder = "images148color"


os.makedirs(folder, exist_ok=True)

api_url = f"https://picsum.photos/{width}"


for i in tqdm(range(nr)):
    response = requests.get(api_url, stream=True)
    if response.status_code == requests.codes.ok:
        with open(f"{folder}/{i:03d}.jpg", "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)
    else:
        print("Error:", response.status_code, response.text)
    sleep(0.01)
