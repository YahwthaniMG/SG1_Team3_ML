"""
Utilidades y funciones helper para el proyecto Titanic
"""

import matplotlib.pyplot as plt
import os
from datetime import datetime


def save_plot(
    fig, filename, save_dir="../results/figures/", formats=["png", "svg"], dpi=300
):
    """
    Guarda automáticamente un gráfico en múltiples formatos

    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        La figura a guardar
    filename : str
        Nombre del archivo (sin extensión)
    save_dir : str
        Directorio donde guardar
    formats : list
        Formatos de archivo ['png', 'svg', 'pdf']
    dpi : int
        Resolución para imágenes raster
    """
    # Crear directorio si no existe
    os.makedirs(save_dir, exist_ok=True)

    # Timestamp para versioning
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    saved_files = []

    for fmt in formats:
        filepath = os.path.join(save_dir, f"{filename}.{fmt}")
        fig.savefig(
            filepath,
            format=fmt,
            dpi=dpi,
            bbox_inches="tight",
            facecolor="white",
            edgecolor="none",
        )
        saved_files.append(filepath)
        print(f"✅ Gráfico guardado: {filepath}")

    return saved_files


def save_current_plot(filename, save_dir="../results/figures/", formats=["png"]):
    """
    Guarda el gráfico actual de matplotlib
    """
    fig = plt.gcf()
    return save_plot(fig, filename, save_dir, formats)
