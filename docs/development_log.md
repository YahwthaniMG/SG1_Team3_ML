# 📝 Development Log - Titanic Survival Prediction

## 📅 Registro de Desarrollo del Proyecto

**Equipo**: SG1_Team3_ML  
**Integrantes**: Andrés López, Héctor Eguiarte, Yahwthani Morales, Omar Vidaña  
**Materia**: COM 139 - Simulación & Visualización  
**Universidad**: Universidad Panamericana  

---

## 🎯 Fase 1: Setup e Inicialización del Proyecto

### ✅ **26 Mayo 2025 - Configuración Inicial**

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

### ✅ **26 Mayo 2025 - EDA Completo**

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

## 🔄 Fase 3: Data Cleaning & Preprocessing (En Progreso)

### 🚧 **Próximos Challenges Identificados:**

#### **Challenge Anticipado 1: Imputación de Age**
**Opciones consideradas**:
1. Media/Mediana simple
2. Imputación por clase y género
3. Modelo predictivo (KNN, Random Forest)
4. Múltiple imputation

**Criterio de decisión**: Balance entre precisión y simplicidad

#### **Challenge Anticipado 2: Feature Engineering**
**Variables a crear**:
- `FamilySize` = SibSp + Parch + 1
- `IsAlone` = FamilySize == 1
- `Title` extraído de Name (Mr, Mrs, Miss, Master, etc.)
- `AgeGroup` = categorías de edad
- `FareBin` = categorías de tarifa

#### **Challenge Anticipado 3: Encoding Categórico**
**Decisiones pendientes**:
- One-hot encoding vs Label encoding
- Manejo de variables ordinales (Pclass)
- Estrategia para variables de alta cardinalidad

---

## 📊 Métricas de Progreso

| Fase | Completado | Tiempo Estimado | Tiempo Real | Estado |
|------|------------|-----------------|-------------|---------|
| Setup | 100% | 2h | 1.5h | ✅ |
| EDA | 100% | 6h | 4h | ✅ |
| Cleaning | 0% | 4h | - | 🚧 |
| Feature Eng. | 0% | 3h | - | ⏳ |
| Modeling | 0% | 6h | - | ⏳ |
| Evaluation | 0% | 3h | - | ⏳ |

**Total Progreso**: 35% completado

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
- [ ] Implementar estrategia de imputación para Age
- [ ] Feature engineering básico
- [ ] Data cleaning pipeline completo
- [ ] Notebook 02_data_cleaning.ipynb

### **Siguientes (Próxima Semana):**
- [ ] Selección de algoritmos ML
- [ ] Implementación de modelos base
- [ ] Cross-validation strategy
- [ ] Métricas de evaluación

### **Finales:**
- [ ] Model comparison y tunning
- [ ] Interpretación de resultados
- [ ] Storytelling final
- [ ] Documentación completa

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

*Log actualizado: 26 Mayo 2025, 18:30*  
*Próxima actualización: 28 Mayo 2025*