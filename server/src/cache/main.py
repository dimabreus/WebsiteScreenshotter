import uuid

from pathlib import Path
from typing import Optional

from config import cache_image_folder

cache_dir = Path(cache_image_folder)
cache_dir.mkdir(exist_ok=True)

cache_index: dict[str, Path] = {}


def cache_image(key: str, image_bytes: bytes) -> None:
    path = cache_dir / f"{uuid.uuid4()}.png"

    with open(path, "wb") as f:
        f.write(image_bytes)

    cache_index[key] = path

    print(f'Cached {key} to {path}')


def get_cached_image(key: str) -> Optional[bytes]:
    path = cache_index.get(key)

    if path and path.exists():
        print(f'Got cached {key} - {path}')
        return path.read_bytes()

    return None


def clear_cached_image(key: str) -> None:
    path = cache_index.pop(key, None)

    if path and path.exists():
        path.unlink()
        print(f'Deleted cache {key} - {path}')
