# 📊 Diccionario de Datos - Dataset Titanic

## 📋 Información General

- **Fuente**: [Kaggle - Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- **Dimensiones**: 891 filas × 12 columnas
- **Tipo de problema**: Clasificación binaria (Supervivencia)
- **Variable objetivo**: `Survived`

## 📝 Descripción de Variables

| Variable | Tipo | Descripción | Valores Posibles | Valores Faltantes |
|----------|------|-------------|------------------|-------------------|
| **PassengerId** | int64 | Identificador único del pasajero | 1-891 | 0 (0.0%) |
| **Survived** | int64 | **Variable objetivo** - Supervivencia del pasajero | 0 = Falleció<br>1 = Sobrevivió | 0 (0.0%) |
| **Pclass** | int64 | Clase del boleto | 1 = Primera clase<br>2 = Segunda clase<br>3 = Tercera clase | 0 (0.0%) |
| **Name** | object | Nombre completo del pasajero | Texto libre | 0 (0.0%) |
| **Sex** | object | Género del pasajero | 'male' = Masculino<br>'female' = Femenino | 0 (0.0%) |
| **Age** | float64 | Edad del pasajero en años | 0.42 - 80.0 años | 177 (19.9%) |
| **SibSp** | int64 | Número de hermanos/cónyuges a bordo | 0-8 | 0 (0.0%) |
| **Parch** | int64 | Número de padres/hijos a bordo | 0-6 | 0 (0.0%) |
| **Ticket** | object | Número del boleto | Alfanumérico | 0 (0.0%) |
| **Fare** | float64 | Tarifa pagada por el boleto | $0.00 - $512.33 | 0 (0.0%) |
| **Cabin** | object | Número de cabina | Alfanumérico (ej: C85) | 687 (77.1%) |
| **Embarked** | object | Puerto de embarque | C = Cherbourg<br>Q = Queenstown<br>S = Southampton | 2 (0.2%) |

## 📈 Estadísticas Descriptivas

### Variables Numéricas

| Estadística | PassengerId | Survived | Pclass | Age | SibSp | Parch | Fare |
|-------------|-------------|----------|--------|-----|-------|-------|------|
| **Media** | 446.0 | 0.384 | 2.31 | 29.7 | 0.52 | 0.38 | 32.20 |
| **Mediana** | 446.0 | 0.0 | 3.0 | 28.0 | 0.0 | 0.0 | 14.45 |
| **Moda** | - | 0 | 3 | 24.0 | 0 | 0 | 8.05 |
| **Desv. Estándar** | 257.4 | 0.487 | 0.84 | 14.5 | 1.10 | 0.81 | 49.69 |
| **Mínimo** | 1.0 | 0.0 | 1.0 | 0.42 | 0.0 | 0.0 | 0.00 |
| **Máximo** | 891.0 | 1.0 | 3.0 | 80.0 | 8.0 | 6.0 | 512.33 |

### Variables Categóricas

| Variable | Valores Únicos | Valor Más Frecuente | Frecuencia |
|----------|----------------|---------------------|------------|
| **Sex** | 2 | 'male' | 577 (64.8%) |
| **Embarked** | 3 | 'S' | 644 (72.4%) |
| **Pclass** | 3 | 3 | 491 (55.1%) |

## 🎯 Variable Objetivo: Survived

- **Distribución**:
  - Fallecidos (0): 549 pasajeros (61.6%)
  - Supervivientes (1): 342 pasajeros (38.4%)
- **Tasa de supervivencia general**: 38.4%

## 🔍 Patrones Identificados

### 👫 Por Género
- **Mujeres**: 74.2% de supervivencia (233/314)
- **Hombres**: 18.9% de supervivencia (109/577)
- **Diferencia**: Las mujeres tuvieron ~4x más probabilidad de sobrevivir

### 🎫 Por Clase
- **Primera clase**: 63.0% de supervivencia (136/216)
- **Segunda clase**: 47.3% de supervivencia (87/184)
- **Tercera clase**: 24.2% de supervivencia (119/491)
- **Patrón**: Supervivencia inversamente proporcional a la clase

### ⚓ Por Puerto de Embarque
- **Cherbourg (C)**: 55.4% de supervivencia (93/168)
- **Queenstown (Q)**: 39.0% de supervivencia (30/77)
- **Southampton (S)**: 33.7% de supervivencia (217/644)

### 👨‍👩‍👧‍👦 Análisis Combinado (Género + Clase)
| Género | Clase | Tasa de Supervivencia |
|--------|-------|----------------------|
| Mujer | 1ª | 96.8% |
| Mujer | 2ª | 92.1% |
| Mujer | 3ª | 50.0% |
| Hombre | 1ª | 36.9% |
| Hombre | 2ª | 15.7% |
| Hombre | 3ª | 13.5% |

## 🔗 Correlaciones con Supervivencia

| Variable | Correlación | Interpretación |
|----------|-------------|----------------|
| **Fare** | +0.257 | Tarifa más alta → Mayor supervivencia |
| **Parch** | +0.082 | Más familiares (padres/hijos) → Ligera mejora |
| **Age** | -0.077 | Mayor edad → Ligera disminución |
| **SibSp** | -0.035 | Más hermanos/cónyuges → Ligera disminución |
| **Pclass** | -0.338 | Clase más alta (número menor) → Mayor supervivencia |

## ❌ Calidad de Datos

### Valores Faltantes por Prioridad de Atención

1. **Cabin (77.1% faltantes)**: 
   - Posible eliminación de la variable
   - O creación de variable binaria "Cabin_Known"

2. **Age (19.9% faltantes)**:
   - Requiere imputación (media, mediana, o modelo predictivo)
   - Variable importante para análisis

3. **Embarked (0.2% faltantes)**:
   - Fácil de imputar (moda = 'S')
   - Mínimo impacto

## 🚀 Recomendaciones para Procesamiento

1. **Eliminar**: PassengerId, Name, Ticket (no predictivos)
2. **Imputar**: Age (con estrategia apropiada)
3. **Codificar**: Variables categóricas (Sex, Embarked)
4. **Feature Engineering**: 
   - Tamaño de familia (SibSp + Parch)
   - Categorías de edad
   - Títulos extraídos del nombre
5. **Outliers**: Revisar valores extremos en Fare y Age

---
*Última actualización: 26 Mayo 2025*