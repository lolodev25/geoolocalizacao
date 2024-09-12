from pydantic import BaseModel


class VisualizaPoint(BaseModel):
    id: int
    coordenadas: tuple
