# 🚢 Titanic Survival Prediction

## 📖 Descripción del Proyecto

Este proyecto utiliza técnicas de Machine Learning para predecir la supervivencia de los pasajeros del RMS Titanic basándose en características demográficas y socioeconómicas. Desarrollado como proyecto académico para la materia COM 139 - Simulación & Visualización de la Universidad Panamericana.

### 🎯 Objetivos
- Analizar los factores que influyeron en la supervivencia del Titanic
- Implementar y comparar diferentes algoritmos de clasificación
- Crear visualizaciones que cuenten la historia de los datos
- Descubrir patrones ocultos en los datos históricos
- Validar cuantitativamente el protocolo "mujeres y niños primero"

## 🏆 Resultados Principales

- **🎯 Objetivo Académico**: ✅ **ALCANZADO** - Accuracy superior al 80% requerido
- **🤖 Mejor Modelo**: Support Vector Machine (SVM) con kernel RBF
- **📊 Performance Final**: **84.4% accuracy** en test set
- **🔍 Métricas Balanceadas**: F1-Score: 0.78, Precision: 0.85, Recall: 0.72, AUC-ROC: 0.86
- **🧪 Validación Demostrada**: 87.0% accuracy en datos de validación final

### 📈 Comparación de Algoritmos

| Modelo | Accuracy | F1-Score | AUC-ROC | Interpretabilidad |
|--------|----------|----------|---------|-------------------|
| **SVM (Ganador)** | **84.4%** | **0.781** | **0.859** | Media |
| Logistic Regression | 84.3% | 0.781 | **0.910** | **Alta** |
| Random Forest | 83.2% | 0.783 | 0.879 | Media |
| Naive Bayes | 82.0% | 0.750 | 0.876 | Media |

## 📊 Dataset y Características

- **Fuente**: [Kaggle - Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- **Dimensiones**: 891 pasajeros × 12 características originales → **29 features engineeradas**
- **Variable objetivo**: Survived (38.4% tasa histórica de supervivencia)
- **Calidad**: Procesamiento completo de valores faltantes y feature engineering avanzado

### 🔍 Top Features Más Predictivas
1. **AgeSex_Adult_Female** (r=0.486): Mujeres adultas
2. **SexPclass_female_Class1** (r=0.413): Mujeres de primera clase  
3. **Title_Mrs** (r=0.342): Estado social femenino

## 🏛️ Insights Históricos Validados

- **✅ Protocolo "Mujeres y Niños Primero"**: Mujeres 74.2% vs Hombres 18.9% supervivencia (ratio 4:1)
- **✅ Clase Social Determinante**: 1ª clase (63%) > 2ª clase (47%) > 3ª clase (24%)
- **✅ Intersección Crítica**: Mujeres 1ª clase 96.8% vs Hombres 3ª clase 13.5%
- **✅ Validación Cuantitativa**: Los datos confirman las narrativas históricas del desastre

## 📁 Estructura del Proyecto

```
SG1_Team3_ML/
├── 📋 DOCUMENTACIÓN
│   ├── docs/
│   │   ├── project_proposal.md          # Propuesta inicial del proyecto
│   │   ├── methodology.md               # Metodología CRISP-DM detallada
│   │   ├── data_dictionary.md           # Diccionario completo de datos
│   │   ├── development_log.md           # ⭐ Log detallado del desarrollo
│   │   └── final_technical_report.md    # ⭐ Reporte técnico completo
│
├── 📓 NOTEBOOKS (Pipeline ML Completo)
│   ├── notebooks/
│   │   ├── 01_exploratory_data_analysis.ipynb    # EDA completo
│   │   ├── 02_data_cleaning.ipynb               # Limpieza de datos
│   │   ├── 03_feature_engineering.ipynb        # Ingeniería de características
│   │   ├── 04_modeling.ipynb                   # ⭐ Entrenamiento de modelos
│   │   ├── 05_model_evaluation.ipynb           # Evaluación y análisis
│   │   └── 06_final_predictions.ipynb          # ⭐ Predicciones finales
│
├── 📊 DATOS
│   ├── data/
│   │   ├── raw/titanic.csv              # Dataset original de Kaggle
│   │   └── processed/                   # Datos procesados y features
│
├── 🤖 MODELOS
│   ├── models/
│   │   ├── best_model_svm.pkl          # ⭐ Modelo SVM final entrenado
│   │   └── model_metrics.json          # Métricas y parámetros del modelo
│
├── 📈 RESULTADOS
│   ├── results/
│   │   ├── figures/                    # Todas las visualizaciones generadas
│   │   └── reports/                    # Reportes HTML automáticos
│
├── 🔧 CÓDIGO FUENTE
│   ├── src/
│   │   └── utils/helpers.py            # Funciones utilitarias
│
└── 📋 CONFIGURACIÓN
    ├── requirements.txt                 # Dependencias Python
    ├── environment.yml                  # Entorno Conda
    └── setup.py                        # Configuración del paquete
```

## 🔑 Archivos Clave para Revisar

### 📋 **Documentación Principal**
- **`docs/final_technical_report.md`** - Reporte técnico completo con todos los resultados
- **`docs/development_log.md`** - Registro detallado del proceso de desarrollo
- **`docs/methodology.md`** - Metodología CRISP-DM implementada

### 🧪 **Notebooks Ejecutables**
- **`notebooks/04_modeling.ipynb`** - Entrenamiento y comparación de modelos
- **`notebooks/06_final_predictions.ipynb`** - Demostración de predicciones finales
- **`notebooks/01_exploratory_data_analysis.ipynb`** - Análisis exploratorio completo

### 🤖 **Modelo Productivo**
- **`models/best_model_svm.pkl`** - Modelo SVM entrenado listo para usar
- **`models/model_metrics.json`** - Métricas completas de performance

## 🛠️ Instalación y Ejecución

### Opción 1: Conda (Recomendado)
```bash
# Clonar repositorio
git clone https://github.com/YahwthaniMG/SG1_Team3_ML.git
cd SG1_Team3_ML

# Crear entorno
conda env create -f environment.yml
conda activate SG1_Team3_ML

# Ejecutar notebooks
jupyter notebook notebooks/
```

### Opción 2: pip + venv
```bash
# Clonar repositorio
git clone https://github.com/YahwthaniMG/SG1_Team3_ML.git
cd SG1_Team3_ML

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar notebooks
jupyter notebook notebooks/
```

### 🚀 Ejecución Rápida

Para ver los resultados inmediatamente:

1. **Ver Resultados**: Abrir `docs/final_technical_report.md`
2. **Ejecutar Predicciones**: Notebook `06_final_predictions.ipynb`
3. **Pipeline Completo**: Ejecutar notebooks 01-06 en orden

## 📊 Demostración de Predicciones

El modelo final puede predecir supervivencia en nuevos datos:

```python
# Ejemplo de uso del modelo entrenado
import joblib
model = joblib.load('models/best_model_svm.pkl')

# El modelo logró en demostración:
# - 87.0% accuracy en 100 pasajeros de prueba
# - 35% predichos como supervivientes (vs 38.4% histórico)
# - 78% predicciones de alta confianza
```

## 🎓 Valor Académico Demostrado

### ✅ **Objetivos Técnicos Cumplidos**
- **Pipeline ML Completo**: CRISP-DM implementado de principio a fin
- **Comparación Algorítmica**: 4 algoritmos evaluados sistemáticamente
- **Performance Superior**: 84.4% accuracy (objetivo >80% ✅)
- **Validación Rigurosa**: Cross-validation, test set holdout, métricas balanceadas

### 🏛️ **Contribución Histórica**
- **Validación Cuantitativa**: Protocolo "mujeres y niños primero" confirmado estadísticamente
- **Interseccionalidad**: Género + Clase social como factor determinante crítico  
- **Casos Excepcionales**: Análisis de errores revela historias humanas extraordinarias
- **Lecciones Modernas**: Insights aplicables a protocolos de emergencia actuales

### 🔬 **Rigor Metodológico**
- **Reproducibilidad**: Todo el código y pipeline documentado
- **Transparencia**: Development log con todos los challenges y decisiones
- **Validación**: Resultados consistentes y estadísticamente significativos

## 👨‍🎓 Equipo de Desarrollo

**SG1_Team3_ML** - Universidad Panamericana, Primavera 2025

- **Andrés López Álvarez** - Feature Engineering & Modelado
- **Héctor Manuel Eguiarte Carlos** - Visualización & Storytelling  
- **Yahwthani Morales Gómez** - Project Lead & Data Pipeline
- **Omar Vidaña Rodríguez** - Model Evaluation & Performance Analysis

**Instructor**: Gabriel Castillo Cortés  
**Materia**: COM 139 - Simulación & Visualización

## 📚 Referencias y Fuentes

### **Datos Históricos**
- [Kaggle Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- Encyclopedia Titanica (validación histórica)
- British Board of Trade Report (1912)

### **Metodología Técnica**
- James, G. et al. "An Introduction to Statistical Learning"
- Castillo, G. "ML-Practical.pdf" (documento base del curso)
- Documentación scikit-learn

### **Contexto Histórico**
- Lord, Walter. "A Night to Remember" (1955)
- Investigación oficial británica del desastre (1912)

---

## 🎯 Conclusión

Este proyecto demuestra exitosamente la aplicación de Machine Learning para validar narrativas históricas, alcanzando no solo los objetivos técnicos académicos sino también generando insights valiosos sobre uno de los eventos más estudiados de la historia marítima.

**El modelo SVM final no solo predice supervivencia con 84.4% de precisión, sino que revela cuantitativamente cómo la estructura social de 1912 determinó literalmente la vida y la muerte en el Titanic.**

---

*¿Quieres explorar más? Comienza con `docs/final_technical_report.md` para el análisis completo o ejecuta `notebooks/06_final_predictions.ipynb` para ver el modelo en acción.*