import geopandas as gpd

def carregar_ubs():
    url_ubs = 'https://raw.githubusercontent.com/lolodev25/base_dados/main/UBS_BRASIL.geojson'

    return gpd.read_file(url_ubs)

def carregar_malha():
    url_malha = 'https://raw.githubusercontent.com/lolodev25/base_dados/main/BRMALHAUBS.geojson'
    return gpd.read_file(url_malha)