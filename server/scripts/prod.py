import os

import uvicorn


def main():
    port = int(os.environ.get("PORT", 10000))

    uvicorn.run("src.server.main:app", host="0.0.0.0", port=port)
