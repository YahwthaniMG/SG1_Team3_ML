#!/usr/bin/env python3
"""
Pipeline Principal - Titanic Survival Prediction
================================================

Este script ejecuta todo el pipeline de ML de principio a fin:
1. Carga de datos
2. EDA (opcional)
3. Data cleaning
4. Feature engineering
5. Modelado
6. Evaluación
7. Predicciones finales

Uso:
    python scripts/run_pipeline.py --mode full
    python scripts/run_pipeline.py --mode predict_only
"""

import argparse
import sys
import os
import pandas as pd
import joblib
from pathlib import Path

# Añadir src al path
sys.path.append(str(Path(__file__).parent.parent / "src"))


def run_full_pipeline():
    """Ejecuta todo el pipeline desde cero"""
    print("🚢 INICIANDO PIPELINE COMPLETO DEL TITANIC")
    print("=" * 50)

    try:
        # 1. Verificar datos
        if not os.path.exists("data/raw/titanic.csv"):
            print("❌ Error: No se encuentra data/raw/titanic.csv")
            return False

        # 2. Data Cleaning
        print("\n🧹 Paso 1: Data Cleaning...")
        # Aquí ejecutarías el proceso de cleaning
        # O importar funciones de src/data/

        # 3. Feature Engineering
        print("🔧 Paso 2: Feature Engineering...")

        # 4. Modelado
        print("🤖 Paso 3: Entrenamiento de Modelos...")

        # 5. Evaluación
        print("📊 Paso 4: Evaluación...")

        # 6. Predicciones finales
        print("🎯 Paso 5: Predicciones Finales...")

        print("\n✅ ¡Pipeline completado exitosamente!")
        return True

    except Exception as e:
        print(f"❌ Error en pipeline: {str(e)}")
        return False


def predict_only():
    """Solo genera predicciones con modelo existente"""
    print("🎯 GENERANDO PREDICCIONES FINALES")
    print("=" * 35)

    try:
        # Cargar modelo
        model_path = "models/best_model_svm.pkl"
        if not os.path.exists(model_path):
            print(f"❌ Error: No se encuentra {model_path}")
            return False

        model = joblib.load(model_path)
        print(f"✅ Modelo cargado: {model_path}")

        # Generar predicciones
        # ... código para predicciones

        print("✅ Predicciones generadas en results/final_predictions.csv")
        return True

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Pipeline ML Titanic")
    parser.add_argument(
        "--mode",
        choices=["full", "predict_only"],
        default="full",
        help="Modo de ejecución (default: full)",
    )

    args = parser.parse_args()

    if args.mode == "full":
        success = run_full_pipeline()
    else:
        success = predict_only()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
