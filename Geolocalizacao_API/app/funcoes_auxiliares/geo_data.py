import geopandas as gpd


def carregar_ubs():
    return gpd.read_file(
        "C:/Users/user/.vscode/Geolocalizacao_API/dataframes/UBS_BRASIL.geojson"
    )


def carregar_malha():
    return gpd.read_file(
        "C:/Users/user/.vscode/Geolocalizacao_API/dataframes/BRMALHAUBS.geojson"
    )
