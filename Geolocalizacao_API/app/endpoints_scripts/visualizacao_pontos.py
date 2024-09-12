from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from io import BytesIO
from Geolocalizacao_API.app.funcoes_auxiliares.plot_data import plot_ubs

router = APIRouter()

@router.get("/plot")
def plot_pontos():
    buffer = BytesIO()
    plot_ubs(buffer)
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="image/png")
