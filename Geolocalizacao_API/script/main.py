import geopandas as gpd
from shapely.geometry import Point, shape
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

#carregando os arquivos
df_brmalhaubs = gpd.read_file(
    "C:/Users/user/.vscode/Geolocalizacao_API/dataframes/BRMALHAUBS.geojson"
)
df_ubs_brasil = gpd.read_file(
    "C:/Users/user/.vscode/Geolocalizacao_API/dataframes/UBS_BRASIL.geojson"
)

#modelo para visualizar os dados
class VisualizaPoint(BaseModel):
    id: int
    coordenadas: tuple

#visualizar os pontos
@app.get("/pontos_base/", response_model=list[VisualizaPoint])
def pegar_pontos_base():
    pontos = []
    for index, coluna in df_ubs_brasil.iterrows():
        #convertendo as colunas para um objeto
        dados_geometry = shape(coluna["geometry"])
        if isinstance(dados_geometry, Point):  # Verificando se é um ponto
            pontos.append({"id": index, "coordenadas": dados_geometry.coords[0]})
    return pontos


