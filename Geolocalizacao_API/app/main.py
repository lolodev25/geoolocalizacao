from fastapi import FastAPI
from Geolocalizacao_API.app.endpoints_scripts.visualizar_dados import router as pontos_router
from Geolocalizacao_API.app.endpoints_scripts.visualizacao_pontos import router as dados_router

app = FastAPI()

# Incluindo as rotas
app.include_router(pontos_router)
app.include_router(dados_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}