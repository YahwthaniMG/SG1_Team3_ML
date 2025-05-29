"""
Utilities and helper functions for the Titanic project.
"""

import matplotlib.pyplot as plt
import os
from datetime import datetime


def save_plot(
    fig, filename, save_dir="../results/figures/", formats=["png", "svg"], dpi=300
):
    """
    Automatically saves a graphic in multiple formats

    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        The figure to keep
    filename : str
        File name (without extension)
    save_dir : str
        Directory where to save
    formats : list
        File formats ['png', 'svg', 'pdf']
    dpi : int
        Resolution for raster images
    """
    # Create directory if it does not exist
    os.makedirs(save_dir, exist_ok=True)

    # Timestamp for versioning
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
        print(f"✅ Graph saved: {filepath}")

    return saved_files


def save_current_plot(filename, save_dir="../results/figures/", formats=["png"]):
    """
    Saves the current matplotlib plot
    """
    fig = plt.gcf()
    return save_plot(fig, filename, save_dir, formats)
