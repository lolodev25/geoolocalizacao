import geopandas as gpd
from shapely.geometry import Point, shape
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Carregando os arquivos GeoJSON
# df_brmalhaubs = gpd.read_file(".../Geolocalizacao_API/dataframes/BRMALHAUBS.geojson")
# df_ubs_brasil = gpd.read_file(".../Geolocalizacao_API/dataframes/UBS_BRASIL.geojson")


# Modelo de dados para visualização dos pontos
# class VisualizaPoint(BaseModel):
#   id: int
#  coordenadas: tuple


# Endpoint para visualizar os pontos
# @app.get("/pontos_base/", response_model=list[VisualizaPoint])
# def pegar_pontos_base():
#   pontos = []
#  for index, coluna in df_ubs_brasil.iterrows():
# Convertendo a geometria da coluna em um objeto shapely
#     dados_geometry = shape(coluna["geometry"])
#    if isinstance(dados_geometry, Point):  # Verificando se é um ponto
#       pontos.append({"id": index, "coordenadas": dados_geometry.coords[0]})
# return pontos
