import matplotlib.pyplot as plt
from Geolocalizacao_API.app.funcoes_auxiliares.geo_data import carregar_ubs, carregar_malha

def plot_ubs(buffer):
    df_brmalhaubs = carregar_malha()
    df_ubs_brasil = carregar_ubs()

    fig, ax = plt.subplots(figsize=(10, 10))

    df_brmalhaubs.plot(ax=ax, color="green", markersize=1, label="Malha UBS")
    df_ubs_brasil.plot(ax=ax, color="blue", markersize=5, label="UBS Brasil")

    plt.title("Visualização das UBS no Brasil")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.savefig(buffer, format="png")
