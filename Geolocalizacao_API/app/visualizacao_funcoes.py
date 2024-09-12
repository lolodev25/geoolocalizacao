import geopandas as gpd
from shapely.geometry import Point, shape
from pydantic import BaseModel
from fastapi import FastAPI
import matplotlib.pyplot as plt
from io import BytesIO
from fastapi.responses import StreamingResponse


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Carregando os arquivos GeoJSON
df_brmalhaubs = gpd.read_file(
    "C:/Users/user/.vscode/Geolocalizacao_API/dataframes/BRMALHAUBS.geojson"
)
df_ubs_brasil = gpd.read_file(
    "C:/Users/user/.vscode/Geolocalizacao_API/dataframes/UBS_BRASIL.geojson"
)


# Modelo de dados para visualização dos pontos
class VisualizaPoint(BaseModel):
    id: int
    coordenadas: tuple


# visualizar os pontos
@app.get("/pontos_base/", response_model=list[VisualizaPoint])
def pegar_pontos_base():
    pontos = []
    for index, coluna in df_ubs_brasil.iterrows():
        # Convertendo a geometria da coluna em um objeto shapely
        dados_geometry = shape(coluna["geometry"])
        if isinstance(dados_geometry, Point):  # Verificando se é um ponto
            pontos.append({"id": index, "coordenadas": dados_geometry.coords[0]})
    return pontos


@app.get("/plot")
def plot_pontos():

    fig, ax = plt.subplots(figsize=(10, 10))

    df_brmalhaubs.plot(ax=ax, color="green", markersize=1, label="Malha UBS")
    df_ubs_brasil.plot(ax=ax, color="blue", markersize=5, label="UBS Brasil")

    plt.title("Visualização das UBS no Brasil")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")


# @app.post("/post")
# def inserir_coordenada()
