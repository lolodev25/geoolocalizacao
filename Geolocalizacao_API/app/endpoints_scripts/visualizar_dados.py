from fastapi import APIRouter
from Geolocalizacao_API.app.modelo_dados import VisualizaPoint
from shapely.geometry import Point, shape
from Geolocalizacao_API.app.funcoes_auxiliares.geo_data import carregar_ubs
import pandas as pd
from fastapi.responses import StreamingResponse
import io

router = APIRouter()

# Carregar os arquivos GeoJSON
df_ubs_brasil = carregar_ubs()


@router.get("/pontos_base/", response_model=list[VisualizaPoint])
def pegar_pontos_base():
    pontos = []
    for index, coluna in df_ubs_brasil.iterrows():
        # Convertendo a geometria da coluna em um objeto shapely
        dados_geometry = shape(coluna["geometry"])
        if isinstance(dados_geometry, Point):
            pontos.append({"id": index, "coordenadas": dados_geometry.coords[0]})

    df_pontos = pd.DataFrame(pontos)
    buffer = io.StringIO()
    df_pontos.to_json(buffer, index=False)
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="text/json",
        headers={"Content-Disposition": "attachment; filename=pontos_base.geojson"},
    )


