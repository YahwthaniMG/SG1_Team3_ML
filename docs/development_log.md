# 📝 Development Log - Titanic Survival Prediction

## 📅 Registro de Desarrollo del Proyecto

**Equipo**: SG1_Team3_ML  
**Integrantes**: Andrés López, Héctor Eguiarte, Yahwthani Morales, Omar Vidaña  
**Materia**: COM 139 - Simulación & Visualización  
**Universidad**: Universidad Panamericana  

---

## 🎯 Fase 1: Setup e Inicialización del Proyecto

### ✅ **28 Mayo 2025 - Configuración Inicial**

**Tareas Completadas:**
- [x] Creación de estructura de proyecto profesional
- [x] Configuración de entorno virtual y dependencias
- [x] Setup de repositorio Git con .gitignore apropiado
- [x] Documentación inicial en README.md

**Decisiones Técnicas:**
- **Python 3.9** como versión base para compatibilidad
- **Conda + pip** para gestión híbrida de dependencias
- **Estructura modular** separando notebooks, src, docs, y scripts
- **Setup.py** para instalación como paquete Python

**Herramientas Seleccionadas:**
```yaml
Análisis: pandas, numpy, scipy
ML: scikit-learn, xgboost
Visualización: matplotlib, seaborn, plotly
Desarrollo: jupyter, black, flake8
```

**Challenges Identificados:**
- ⚠️ Necesidad de balance entre estructura profesional y simplicidad académica
- ⚠️ Gestión de versiones de dependencias para reproducibilidad

---

## 🔍 Fase 2: Análisis Exploratorio de Datos (EDA)

### ✅ **28 Mayo 2025 - EDA Completo**

**Dataset Características:**
- **Fuente**: Kaggle Titanic Dataset
- **Dimensiones**: 891 pasajeros × 12 características
- **Variable objetivo**: Survived (38.4% tasa supervivencia)

**Hallazgos Principales:**

#### 📊 **Insights de Supervivencia**
1. **Género es el factor más determinante**:
   - Mujeres: 74.2% supervivencia
   - Hombres: 18.9% supervivencia
   - **Ratio 4:1** a favor de mujeres

2. **Clase social crítica**:
   - 1ª clase: 63.0% supervivencia
   - 2ª clase: 47.3% supervivencia  
   - 3ª clase: 24.2% supervivencia

3. **Intersección género-clase reveló patrón "Mujeres y niños primero"**:
   - Mujeres 1ª clase: **96.8%** supervivencia
   - Hombres 3ª clase: **13.5%** supervivencia

#### ❌ **Calidad de Datos**
- **Cabin**: 77.1% valores faltantes → Candidata a eliminación
- **Age**: 19.9% valores faltantes → Requiere imputación estratégica
- **Embarked**: 0.2% valores faltantes → Fácil de corregir

**Decisiones de Procesamiento:**
- Eliminar variables no predictivas: PassengerId, Name, Ticket
- Estrategia de imputación para Age pendiente de definir
- Feature engineering: tamaño familia, categorías edad, títulos

**Tools Utilizadas:**
```python
# Visualizaciones efectivas generadas
matplotlib + seaborn  # Gráficos estadísticos
plotly                # Gráficos interactivos
pandas.crosstab()     # Análisis categórico
correlation matrix    # Relaciones numéricas
```

**Challenges Encontrados:**

#### 🚧 **Challenge 1: Visualización Automática**
**Problema**: Notebooks generan muchos gráficos que se pierden al cerrar  
**Solución Implementada**: 
- Función `save_plot()` en `src/utils/helpers.py`
- Guarda automáticamente en múltiples formatos (PNG, SVG)
- Timestamp para versionado

#### 🚧 **Challenge 2: Balance Complejidad vs Insights**
**Problema**: Tentación de sobre-analizar vs necesidad de insights claros  
**Solución**: 
- Enfoque en top 3 factores predictivos: Género, Clase, Age
- Visualizaciones que cuentan historia clara
- Métricas simples pero efectivas

#### 🚧 **Challenge 3: Interpretación de Correlaciones**
**Problema**: Correlaciones bajas en variables numéricas (-0.338 max)  
**Aprendizaje**: 
- Variables categóricas más importantes que numéricas
- Necesidad de feature engineering
- Interacciones entre variables críticas

**Referencias Consultadas:**
- [Kaggle Titanic Tutorials](https://www.kaggle.com/learn/intro-to-machine-learning)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- Documentación scikit-learn para preprocessing

---

## 🔄 Fase 3: Data Cleaning & Preprocessing (Completado)

### ✅ **29 Mayo 2025 - Data Cleaning Exitoso**

**Estrategias Implementadas:**
- **Age (19.9% faltantes)**: Imputación por mediana agrupada (Sex + Pclass)
- **Cabin (77.1% faltantes)**: Convertida a variable binaria `Cabin_Known`
- **Embarked (0.2% faltantes)**: Imputación con moda (Southampton)
- **Outliers**: Analizados y mantenidos (históricamente válidos)

**Decisiones Tomadas:**
- Eliminación de PassengerId, Name, Ticket (no predictivos)
- Mantener outliers de Fare (suites de lujo legítimas)
- Mantener outliers de Age (bebés/ancianos realistas en 1912)

---

## 🔧 Fase 4: Feature Engineering (Completado)

### ✅ **29 Mayo 2025 - Feature Engineering Exitoso**

**Nuevas Variables Creadas:**

#### 📊 **Variables Derivadas Exitosas:**
1. **FamilySize**: Familias 2-4 personas → 55-72% supervivencia
2. **IsAlone**: Acompañados (50.6%) vs Solos (30.4%) supervivencia
3. **AgeGroup**: Niños (57.4%) > Adultos jóvenes (33.7%) > Seniors (26.9%)
4. **FareBin**: Premium (58.1%) > High (45.5%) > Medium (30.4%) > Low (19.7%)
5. **Title**: Mrs (79.4%) > Miss (70.1%) > Master (57.5%) > Mr (15.7%)

#### 🔗 **Variables de Interacción Poderosas:**
- **Sex_Pclass**: female_Class1 (96.8%) vs male_Class3 (13.5%)
- **Age_Sex**: Adult_Female (75.3%) > Young (54.0%) > Adult_Male (16.6%)

**Encoding Estratégico:**
- **Label**: Variables binarias (Sex, Embarked)
- **Ordinal**: Variables ordenadas (AgeGroup, FareBin)  
- **One-Hot**: Variables nominales (Title, interacciones)

**Resultado Final:**
- De 9 variables originales → **29 features**
- **Top 3 predictores**: AgeSex_Adult_Female (0.486), SexPclass_female_Class1 (0.413), Title_Mrs (0.342)

#### 🚧 **Challenges Encontrados:**

#### **Challenge 4: Balance de Features**
**Problema**: Riesgo de overfitting con 29 features en dataset de 891 registros  
**Solución Implementada**: 
- Correlación analysis para identificar features más importantes
- Encoding estratégico (no dummy trap)
- Preparación para feature selection en modelado

#### **Challenge 5: Interpretabilidad vs Performance**
**Problema**: Variables de interacción mejoran predicción pero complican interpretación  
**Aprendizaje**: 
- Mantener variables originales para interpretación
- Variables de interacción para performance
- Documentar claramente cada feature

---

## 🤖 Fase 5: Machine Learning Modeling (Completado)

### ✅ **29 Mayo 2025 - Modelado Exitoso**

**Algoritmos Implementados:**
- **Logistic Regression**: Baseline interpretable (84.3% accuracy, AUC=0.91)
- **Random Forest**: Ensemble robusto (83.2% accuracy, overfitting detectado)
- **Support Vector Machine**: Boundaries complejas (**GANADOR**: 84.4% accuracy)
- **Naive Bayes**: Baseline probabilístico (82.0% accuracy)

**Mejor Modelo Final:**
- **Algoritmo**: SVM con kernel RBF
- **Hiperparámetros**: C=1, gamma='auto'
- **Performance Test**: 84.4% accuracy, F1=0.78, AUC=0.86
- **✅ OBJETIVO ALCANZADO**: >80% accuracy

**Proceso de Validación:**
- **Data Split**: 70% train, 10% validation, 20% test
- **Cross-Validation**: 5-fold estratificado para robustez
- **Grid Search**: Optimización de hiperparámetros
- **Test Final**: Evaluación en conjunto no visto

#### 🚧 **Challenges Encontrados:**

#### **Challenge 7: Overfitting en Random Forest**
**Problema**: Random Forest mostró 99.2% accuracy en train vs 83.2% en validation
**Solución**: 
- Identificado mediante comparación train-val
- SVM demostró mejor generalización
- Documentado para análisis futuro

#### **Challenge 8: Selección de Métrica Óptima**
**Problema**: Balance entre accuracy, precision y recall para contexto histórico
**Decisión**: 
- F1-Score como métrica principal (balance precision-recall)
- AUC-ROC para capacidad discriminativa
- Accuracy para cumplir objetivo académico (>80%)

#### **Challenge 9: Interpretabilidad vs Performance**
**Problema**: SVM (ganador) menos interpretable que Logistic Regression
**Aprendizaje**: 
- Priorizar performance para objetivo académico
- Mantener Logistic Regression para interpretación
- Feature importance no disponible en SVM (como esperado)

---

## 📊 Fase 6: Model Evaluation & Interpretation (Completado)

### ✅ **29 Mayo 2025 - Evaluación y Análisis Profundo Completado**

**Análisis de Performance Final:**
- **SVM Optimizado**: 84.4% accuracy en test (objetivo >80% ✅)
- **Balance Métricas**: F1=0.78, Precision=0.85, Recall=0.72, AUC=0.86
- **Sin Overfitting**: Performance consistente entre train/val/test
- **Robustez Confirmada**: Cross-validation estable

**Error Analysis Revelador:**
- **16.2% Error Total**: 52 falsos positivos + 92 falsos negativos
- **Falsos Positivos**: Principalmente mujeres de 3ª clase (predicción optimista)
- **Falsos Negativos**: Mayormente hombres que sobrevivieron inesperadamente
- **Insights Humanos**: Errores reflejan casos excepcionales de la tragedia

**Validación de Hipótesis Históricas:**
- **✅ H1**: Mujeres 3.9x más supervivencia que hombres (74% vs 19%)
- **✅ H2**: 1ª clase (63%) > 2ª (47%) > 3ª (24%) supervivencia
- **✅ H4**: Mujeres 1ª clase 97% vs Hombres 3ª clase 14%
- **✅ Features Top**: AgeSex_Adult_Female, SexPclass_female_Class1, Title_Mrs

**Contexto Histórico Validado:**
- **Protocolo Birkenhead**: "Mujeres y niños primero" claramente capturado
- **Clase Social**: Determinó acceso a botes salvavidas
- **Capacidad Limitada**: Solo 53% capacidad de botes explicó tragedia

#### 🚧 **Challenge 10: Interpretación de Casos de Error**
**Problema**: ¿Cómo explicar por qué el modelo se equivocó en casos específicos?
**Análisis Realizado**: 
- Falsos positivos: Mujeres jóvenes 3ª clase con alta probabilidad asignada
- Falsos negativos: Hombres que sobrevivieron contra pronóstico
- **Insight Histórico**: Errores reflejan la naturaleza caótica y humana del desastre

#### 🚧 **Challenge 11: Balance Interpretabilidad vs Accuracy**
**Problema**: SVM no ofrece feature importance directa como Random Forest
**Solución Adoptada**: 
- Usar feature importance del análisis de correlación previo
- Validar con conocimiento histórico del dominio
- Priorizar performance final sobre interpretabilidad inmediata

#### 🚧 **Challenge 12: Bias en Subgrupos Demográficos**
**Problema**: Performance desigual entre géneros y clases
**Hallazgo**: 
- Modelo excelente prediciendo supervivencia femenina (Recall=97%)
- Conservador prediciendo supervivencia masculina (Precision=100%, Recall=21%)
- **Reflexión Ética**: Refleja sesgos históricos reales, no del modelo

---

## 📊 Métricas de Progreso

| Fase | Completado | Tiempo Estimado | Tiempo Real | Estado |
|------|------------|-----------------|-------------|---------|
| Setup | 100% | 2h | 1.5h | ✅ |
| EDA | 100% | 6h | 4h | ✅ |
| Cleaning | 100% | 4h | 3h | ✅ |
| Feature Eng. | 100% | 3h | 2.5h | ✅ |
| Modeling | 100% | 6h | 4h | ✅ |
| Evaluation | 100% | 3h | 2h | ✅ |

**Total Progreso**: 100% completado

---

## 🎓 Lecciones Aprendidas

### **Técnicas:**
1. **EDA estructurado es fundamental** - Insights claros antes de modelado
2. **Visualización cuenta historia** - Gráficos comunican mejor que números
3. **Variables categóricas dominan** - En este dataset, género/clase > edad/tarifa

### **Metodológicas:**
1. **Documentación paralela** - Escribir insights mientras se descubren
2. **Código modular desde inicio** - Funciones helper ahorran tiempo
3. **Versioning visual** - Guardar gráficos importantes automáticamente

### **De Dominio:**
1. **"Mujeres y niños primero"** se refleja claramente en datos
2. **Clase social** = acceso a botes salvavidas
3. **Familia** puede ser ventaja o desventaja según tamaño

---

## 🔮 Próximos Pasos

### **Inmediatos (Esta Semana):**
- [x] Implementar estrategia de imputación para Age
- [x] Feature engineering básico
- [x] Data cleaning pipeline completo
- [x] Notebook 02_data_cleaning.ipynb
- [x] Notebook 03_feature_engineering.ipynb
- [ ] Implementar algoritmos de Machine Learning
- [ ] Notebook 04_modeling.ipynb

### **Siguientes (Próxima Semana):**
- [ ] Comparación de modelos y tunning
- [ ] Cross-validation strategy
- [ ] Métricas de evaluación
- [ ] Interpretación de feature importance

### **Finales:**
- [ ] Error analysis y model improvement
- [ ] Storytelling final
- [ ] Documentación completa
- [ ] Reporte técnico final

---

## 📚 Referencias y Recursos

**Documentación Técnica:**
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [Scikit-learn Preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)

**Inspiración de Análisis:**
- Kaggle Titanic Kernels (Top notebooks)
- [Towards Data Science - Titanic](https://towardsdatascience.com/tagged/titanic)

**Metodología:**
- CRISP-DM Process
- ML-Practical.pdf (Documento del curso)

---

*Log actualizado: 29 Mayo 2025, 18:30*  