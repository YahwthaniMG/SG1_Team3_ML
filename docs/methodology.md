# 🔬 Metodología del Proyecto - Titanic Survival Prediction

## 📋 Marco Metodológico

**Proceso Base**: CRISP-DM (Cross-Industry Standard Process for Data Mining)  
**Enfoque**: Análisis exploratorio → Modelado comparativo → Storytelling interpretativo  
**Paradigma**: Supervised Learning - Clasificación binaria  

---

## 🎯 1. Business Understanding

### **Definición del Problema**
- **Tipo**: Clasificación binaria (Sobrevivió: Sí/No)
- **Contexto**: Análisis histórico con implicaciones sociológicas
- **Métricas objetivo**: Accuracy >80%, Interpretabilidad alta
- **Stakeholders**: Académicos, historiadores, estudiantes de ML

### **Success Criteria**
1. **Técnico**: Modelo con performance superior a baseline random (50%)
2. **Académico**: Cumplir 100% requerimientos ML-Practical.pdf
3. **Interpretativo**: Generar insights validables históricamente
4. **Educativo**: Demonstrar dominio de algoritmos del curso

---

## 📊 2. Data Understanding

### **Estrategia de Análisis Exploratorio**

#### **2.1 Análisis Univariado**
```python
# Para cada variable:
# - Distribución (histogramas, boxplots)
# - Estadísticas descriptivas (media, mediana, moda)
# - Valores faltantes (cantidad, patrón)
# - Outliers (detección visual y estadística)
```

#### **2.2 Análisis Bivariado**
```python
# Variable objetivo vs predictores:
# - Tablas de contingencia (categóricas)
# - Correlaciones (numéricas)
# - Visualizaciones comparativas
# - Tests estadísticos de significancia
```

#### **2.3 Análisis Multivariado**
```python
# Interacciones entre variables:
# - Matrices de correlación
# - Análisis factorial exploratorio
# - Clustering para identificar grupos
# - Análisis de correspondencias
```

### **Calidad de Datos - Criterios**

| Dimensión | Criterio | Acción |
|-----------|----------|---------|
| **Completitud** | <5% missing → OK<br>5-20% → Imputar<br>>20% → Evaluar eliminación | Age: 19.9% → Imputar<br>Cabin: 77.1% → Eliminar |
| **Consistencia** | Valores en rangos esperados | Age: [0-80] ✓<br>Fare: [0-512] ✓ |
| **Precisión** | Coherencia con fuentes históricas | Validar con Encyclopedia Titanica |
| **Relevancia** | Correlación con variable objetivo | Mantener \|corr\| > 0.05 |

---

## 🛠️ 3. Data Preparation

### **3.1 Estrategia de Limpieza**

#### **Valores Faltantes**
```python
# Age (19.9% missing):
strategies = {
    'simple': df['Age'].fillna(df['Age'].median()),
    'group_median': df.groupby(['Sex', 'Pclass'])['Age'].transform('median'),
    'predictive': RandomForestRegressor(features=['Pclass', 'Sex', 'SibSp', 'Parch', 'Fare'])
}
# Selección: Comparar distribuciones resultantes
```

#### **Outliers**
```python
# Criterio: IQR method
def detect_outliers(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    return (column < Q1 - 1.5*IQR) | (column > Q3 + 1.5*IQR)

# Acción: Investigar, no eliminar automáticamente
```

### **3.2 Feature Engineering Strategy**

#### **Variables Derivadas**
```python
features_new = {
    'FamilySize': lambda df: df['SibSp'] + df['Parch'] + 1,
    'IsAlone': lambda df: (df['FamilySize'] == 1).astype(int),
    'Title': lambda df: df['Name'].str.extract('([A-Za-z]+)\.'),
    'AgeGroup': lambda df: pd.cut(df['Age'], bins=[0,12,18,35,60,100], 
                                  labels=['Child','Teen','Adult','Middle','Senior']),
    'FareBin': lambda df: pd.qcut(df['Fare'], q=4, labels=['Low','Medium','High','Premium'])
}
```

#### **Justificación Teórica**
- **FamilySize**: Hipótesis de protección familiar vs sobrecarga
- **Title**: Indicador de estatus social más granular que Pclass
- **AgeGroup**: Política "niños primero" en grupos etarios
- **FareBin**: Proxy de riqueza independiente de clase

### **3.3 Encoding Strategy**

#### **Variables Categóricas**
```python
encoding_strategy = {
    'Sex': 'LabelEncoder',  # Binaria: male=0, female=1
    'Embarked': 'OneHotEncoder',  # Nominal: C, Q, S
    'Title': 'TargetEncoder',  # Alta cardinalidad
    'AgeGroup': 'OrdinalEncoder',  # Ordinal natural
    'Pclass': 'keep_numeric'  # Ya ordinal
}
```

### **3.4 Feature Selection**

#### **Criterios de Selección**
1. **Correlación**: |correlation| > 0.05 con target
2. **Varianza**: Variance threshold > 0.01
3. **Multicolinealidad**: VIF < 5.0
4. **Domain knowledge**: Relevancia histórica/teórica

#### **Métodos a Comparar**
```python
selection_methods = [
    'SelectKBest(chi2)',  # Univariado
    'RFE(LogisticRegression)',  # Wrapper
    'SelectFromModel(RandomForest)',  # Embedded
    'manual_domain_knowledge'  # Expert
]
```

---

## 🤖 4. Modeling Strategy

### **4.1 Algoritmos Seleccionados**

#### **Justificación por Algoritmo**

| Algoritmo | Justificación | Fortalezas Esperadas | Debilidades |
|-----------|---------------|---------------------|-------------|
| **Logistic Regression** | Baseline interpretable, asunciones lineales | Coeficientes interpretables, probabilidades calibradas | Asume linealidad |
| **Random Forest** | Maneja interacciones, robusto | Feature importance, maneja outliers | Menos interpretable |
| **SVM** | Boundaries complejas, kernels | Efectivo en alta dimensión | Hiperparámetros sensibles |
| **Naive Bayes** | Baseline probabilístico | Rápido, maneja missing values | Asume independencia |

### **4.2 Validation Strategy**

#### **Data Splitting**
```python
# Estratificado para mantener proporción de supervivencia
train_size = 0.70  # 623 samples
val_size = 0.15    # 134 samples  
test_size = 0.15   # 134 samples

# Stratified para balance de clases
stratify_on = ['Survived', 'Sex', 'Pclass']
```

#### **Cross-Validation**
```python
cv_strategy = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
# Para model selection y hyperparameter tuning
```

### **4.3 Hyperparameter Optimization**

#### **Grid Search Strategy**
```python
param_grids = {
    'LogisticRegression': {
        'C': [0.01, 0.1, 1, 10, 100],
        'penalty': ['l1', 'l2', 'elasticnet'],
        'solver': ['liblinear', 'saga']
    },
    'RandomForest': {
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 10, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    },
    'SVM': {
        'C': [0.1, 1, 10, 100],
        'kernel': ['linear', 'rbf', 'poly'],
        'gamma': ['scale', 'auto', 0.01, 0.1]
    }
}
```

---

## 📏 5. Evaluation Methodology

### **5.1 Métricas de Performance**

#### **Métricas Primarias**
```python
primary_metrics = {
    'accuracy': 'Proporción correcta total',
    'f1_score': 'Balance precision-recall',
    'roc_auc': 'Capacidad discriminativa',
    'classification_report': 'Detalle por clase'
}
```

#### **Métricas por Contexto**
- **Académico**: Accuracy (simplicidad interpretativa)
- **Médico/Seguridad**: Recall (evitar falsos negativos)
- **Histórico**: Precision (confianza en predicciones positivas)
- **Científico**: AUC-ROC (threshold-independent)

### **5.2 Model Comparison Framework**

#### **Criterios de Comparación**
```python
comparison_criteria = {
    'performance': ['accuracy', 'f1', 'auc'],
    'interpretability': ['feature_importance', 'coefficients', 'decision_rules'],
    'robustness': ['cv_std', 'learning_curves', 'validation_curves'],
    'efficiency': ['training_time', 'prediction_time', 'memory_usage'],
    'generalization': ['bias_variance_tradeoff', 'overfitting_indicators']
}
```

### **5.3 Error Analysis**

#### **Análisis de Casos Mal Clasificados**
```python
def analyze_errors(y_true, y_pred, X):
    errors = X[y_true != y_pred]
    return {
        'false_positives': analyze_group(errors[y_pred[y_true != y_pred] == 1]),
        'false_negatives': analyze_group(errors[y_pred[y_true != y_pred] == 0]),
        'confusion_patterns': find_common_characteristics(errors)
    }
```

---

## 📊 6. Visualization & Interpretation

### **6.1 Storytelling Framework**

#### **Narrativa Estructurada**
1. **Context Setting**: "Era el 14 de abril de 1912..."
2. **Data Introduction**: "891 historias humanas en números..."
3. **Pattern Discovery**: "Los datos revelan que..."
4. **Model Insights**: "Nuestros algoritmos descubrieron..."
5. **Historical Validation**: "Esto confirma que..."
6. **Modern Implications**: "Hoy esto significa..."

### **6.2 Visualization Strategy**

#### **Por Fase del Proyecto**
```python
viz_by_phase = {
    'EDA': ['distributions', 'correlations', 'crosstabs'],
    'Preprocessing': ['before_after_cleaning', 'feature_distributions'],
    'Modeling': ['learning_curves', 'validation_curves'],
    'Evaluation': ['confusion_matrices', 'roc_curves', 'feature_importance'],
    'Interpretation': ['decision_boundaries', 'prediction_examples']
}
```

#### **Principios de Diseño**
- **Clarity**: Mensaje claro en 5 segundos
- **Honesty**: No misleading scales/colors
- **Accessibility**: Colorblind-friendly palettes
- **Narrative**: Cada gráfico cuenta parte de la historia

---

## 🔄 7. Iteration & Refinement

### **7.1 Iterative Approach**

#### **Baseline → Improvement Cycles**
```
Cycle 1: Simple models, basic features
Cycle 2: Feature engineering, hyperparameter tuning  
Cycle 3: Ensemble methods, advanced techniques
Cycle 4: Error analysis, final refinement
```

### **7.2 Validation Gates**

#### **Go/No-Go Criteria per Phase**
- **EDA**: ≥3 significant patterns identified
- **Preprocessing**: Missing values <5%, no data leakage
- **Modeling**: Baseline accuracy >60%
- **Evaluation**: Best model accuracy >75%
- **Interpretation**: ≥5 actionable insights generated

---

## 📝 8. Documentation Standards

### **8.1 Code Documentation**
```python
def function_template(param):
    """
    Brief description
    
    Parameters:
    -----------
    param : type
        Description
        
    Returns:
    --------
    type : Description
    
    Example:
    --------
    >>> function_template("example")
    result
    """
    pass
```

### **8.2 Decision Documentation**
- **Rationale**: Por qué se tomó cada decisión técnica
- **Alternatives**: Qué otras opciones se consideraron
- **Trade-offs**: Ventajas/desventajas de la elección
- **Results**: Impacto medible de la decisión

---

## ✅ 9. Quality Assurance

### **9.1 Reproducibility Checklist**
- [ ] Random seeds fijos en todo el pipeline
- [ ] Versiones de librerías especificadas
- [ ] Datos originales preservados e inmutables
- [ ] Pipeline documentado paso a paso
- [ ] Resultados validables independientemente

### **9.2 Validation Protocol**
- [ ] Cross-validation en model selection
- [ ] Hold-out test set nunca visto hasta el final
- [ ] Métricas reportadas con intervalos de confianza
- [ ] Assumptions de modelos verificadas
- [ ] Resultados consistentes con domain knowledge

---

*Metodología aprobada: 26 Mayo 2025*  
*Versión: 1.0*  
*Próxima revisión: Al completar cada fase*