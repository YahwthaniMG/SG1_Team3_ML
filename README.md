# 🚢 Titanic Survival Prediction

## 📖 Descripción del Proyecto

Este proyecto utiliza técnicas de Machine Learning para predecir la supervivencia de los pasajeros del RMS Titanic basándose en características demográficas y socioeconómicas.

### 🎯 Objetivos
- Analizar los factores que influyeron en la supervivencia
- Implementar y comparar diferentes algoritmos de clasificación
- Crear visualizaciones que cuenten la historia de los datos
- Descubrir patrones ocultos en los datos históricos

## 📊 Dataset

El dataset contiene información de 891 pasajeros con las siguientes características:
- **Survived**: Variable objetivo (0 = No sobrevivió, 1 = Sobrevivió)
- **Pclass**: Clase del boleto (1, 2, 3)
- **Sex**: Género del pasajero
- **Age**: Edad del pasajero
- **SibSp**: Número de hermanos/cónyuges a bordo
- **Parch**: Número de padres/hijos a bordo
- **Fare**: Tarifa pagada
- **Embarked**: Puerto de embarque

## 🛠️ Instalación

1. Clona el repositorio:
```bash
git https://github.com/YahwthaniMG/SG1_Team3_ML.git
cd SG1_Team3_ML
```

2. Crea el entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 🚀 Uso

1. **Ejecutar análisis completo**:
```bash
python scripts/run_pipeline.py
```

2. **Entrenar modelos**:
```bash
python scripts/train_models.py
```

3. **Explorar notebooks**:
```bash
jupyter notebook notebooks/
```

## 📈 Resultados

### Métricas de los Modelos
| Modelo | Accuracy | Precision | Recall | F1-Score |
|--------|----------|-----------|--------|----------|
| Logistic Regression | 0.XX | 0.XX | 0.XX | 0.XX |
| Random Forest | 0.XX | 0.XX | 0.XX | 0.XX |
| SVM | 0.XX | 0.XX | 0.XX | 0.XX |

### Hallazgos Principales
- Las mujeres tuvieron una tasa de supervivencia del XX%
- Los pasajeros de primera clase tuvieron XX% más probabilidades de sobrevivir
- La edad promedio de los supervivientes fue XX años

## 📁 Estructura del Proyecto

```
SG1_Team3_ML/
├── data/              # Datos raw y procesados
├── notebooks/         # Jupyter notebooks
├── src/              # Código fuente
├── models/           # Modelos entrenados
├── results/          # Resultados y visualizaciones
└── docs/             # Documentación
```


## 👨‍🎓 Autores

- **Andrés López Álvarez**
- **Hector Manuel Eguiarte Carlos**
- **Yahwthani Morales Gómez**
- **Omar Vidaña Rodríguez**

##  🏫 Universidad
- Universidad Panamericana
- Materia: COM 139 - Simulación & Visualización
- Semestre: Primavera 2025

## 🙏 Agradecimientos

- Dataset proporcionado por Kaggle
- Inspiración en el trágico evento histórico del RMS Titanic
-  Gabriel Castillo Cortés (Profesor)  y compañeros de la Universidad Panamericana