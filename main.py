from fastapi import FastAPI

app = FastAPI(
    title="BitwardenCopy API",
    description="API desenvolvida para praticar conceitos de FastAPI, simulando algumas " 
    "funcionalidades do Bitwarden. Permite o gerenciamento seguro de senhas."
)

@app.get("/")
def home():
    return {"message": "Minha API está rodando 🚀"}
