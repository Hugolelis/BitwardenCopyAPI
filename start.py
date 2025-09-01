import uvicorn

import webbrowser
import threading
import time

from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()
ENV: str = os.getenv("ENV")     
HOST: str = os.getenv("HOST")
PORT: int = int(os.getenv("PORT"))  


# Abre o swagger
def open_browser():
    time.sleep(1)
    webbrowser.open(f"http://{HOST}:{PORT}/docs")

# roda o servidor
if __name__ == "__main__":
    if ENV.lower() == "dev":
        threading.Thread(target=open_browser).start()

    uvicorn.run("main:app", host=HOST, port=PORT, reload=(ENV=="dev"))
