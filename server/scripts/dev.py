import uvicorn


def main():
    uvicorn.run("src.server.main:app", host="0.0.0.0", port=8800, reload=True)
