import glob
import os

import uvicorn

from src.config import cache_image_folder


def clear_cache():
    files = glob.glob(cache_image_folder + '*')

    for file in files:
        os.remove(file)


def main():
    clear_cache()

    port = int(os.environ.get("PORT", 10000))

    uvicorn.run("src.server.main:app", host="0.0.0.0", port=port)
