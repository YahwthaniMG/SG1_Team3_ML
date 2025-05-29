# 🚢 Propuesta de Proyecto: Predicción de Supervivencia del Titanic

## 📋 Información del Proyecto

**Título**: Predicción de Supervivencia del RMS Titanic usando Machine Learning  
**Equipo**: SG1_Team3_ML  
**Materia**: COM 139 - Simulación & Visualización  
**Universidad**: Universidad Panamericana  
**Semestre**: Primavera 2025  

**Integrantes**:
- Andrés López Álvarez
- Héctor Manuel Eguiarte Carlos  
- Yahwthani Morales Gómez
- Omar Vidaña Rodríguez

---

## 🎯 Objetivo Principal

**Desarrollar un modelo de machine learning que prediga la supervivencia de los pasajeros del RMS Titanic** basándose en características demográficas y socioeconómicas, mientras descubrimos patrones históricos que expliquen los factores determinantes en la tragedia marítima más famosa de la historia.

### Objetivos Específicos

1. **Análisis Exploratorio**: Identificar patrones de supervivencia por género, clase social, edad y origen
2. **Predicción Precisa**: Lograr >80% de accuracy en clasificación binaria
3. **Interpretabilidad**: Explicar qué factores fueron más determinantes para sobrevivir
4. **Storytelling**: Contar la historia humana detrás de los datos estadísticos
5. **Comparación de Algoritmos**: Evaluar múltiples técnicas de ML según el curso

---

## 📊 Dataset y Justificación

### **Dataset Seleccionado**
- **Fuente**: [Kaggle - Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- **Tamaño**: 891 pasajeros × 12 características
- **Tipo**: Clasificación binaria supervisada
- **Variable objetivo**: Survived (0/1)

### **¿Por qué el Titanic?**

#### **Relevancia Histórica**
- Evento icónico que cambió regulaciones marítimas mundiales
- Refleja la estructura social de principios del siglo XX
- Abundante documentación histórica para validar insights

#### **Calidad de Datos**
- Dataset limpio y bien documentado
- Suficiente tamaño para ML sin ser overwhelming
- Balance adecuado de variables numéricas y categóricas
- Tasa de supervivencia (38.4%) evita problemas de clases desbalanceadas extremas

#### **Complejidad Apropiada**
- **Simple enough**: Patrones claros identificables en EDA
- **Complex enough**: Requiere feature engineering y comparación de algoritmos
- **Storytelling rich**: Datos que cuentan historia humana compelling

#### **Aplicabilidad Académica**
- Permite aplicar todos los algoritmos del curso: Logistic Regression, Random Forest, SVM, Naive Bayes
- Oportunidad de feature engineering creativo
- Métricas de evaluación claramente interpretables

---

## 🔍 Hipótesis de Investigación

### **Hipótesis Principal**
*"La supervivencia en el Titanic estuvo determinada principalmente por la intersección de género, clase social y edad, reflejando las normas sociales de 'mujeres y niños primero' moduladas por el poder económico"*

### **Hipótesis Específicas**

1. **H1 - Género**: Las mujeres tuvieron significativamente mayor tasa de supervivencia que los hombres
2. **H2 - Clase Social**: Los pasajeros de primera clase tuvieron mayor supervivencia que segunda y tercera clase
3. **H3 - Edad**: Los niños y adultos jóvenes tuvieron ventaja sobre adultos mayores
4. **H4 - Interacción**: El efecto protector del género femenino se amplificó en clases sociales altas
5. **H5 - Familia**: El tamaño de familia tuvo efecto no-lineal (familias medianas ventaja, familias grandes desventaja)

---

## 🛠️ Metodología Propuesta

### **Fase 1: Análisis Exploratorio (Completado)**
- [x] Carga y inspección inicial de datos
- [x] Análisis de calidad (valores faltantes, outliers)
- [x] Distribuciones univariadas y bivariadas  
- [x] Correlaciones y patrones iniciales
- [x] Visualizaciones descriptivas

### **Fase 2: Preparación de Datos**
- [ ] **Limpieza**: Manejo de valores faltantes en Age, Cabin, Embarked
- [ ] **Feature Engineering**: 
  - Tamaño de familia (SibSp + Parch)
  - Títulos extraídos de nombres (Mr, Mrs, Miss, Master)
  - Categorización de edad y tarifa
  - Variables de interacción (género × clase)
- [ ] **Encoding**: Variables categóricas a numéricas
- [ ] **Scaling**: Normalización de variables numéricas

### **Fase 3: Modelado**
- [ ] **Split**: Train/Validation/Test (70/15/15)
- [ ] **Baseline**: Modelo simple para comparación
- [ ] **Algoritmos a implementar**:
  - Logistic Regression (interpretabilidad)
  - Random Forest (manejo de interacciones)
  - Support Vector Machine (boundaries complejas)
  - Naive Bayes (baseline probabilístico)
- [ ] **Validación cruzada**: K-fold para robustez
- [ ] **Hyperparameter tuning**: Grid search para optimización

### **Fase 4: Evaluación y Comparación**
- [ ] **Métricas**: Accuracy, Precision, Recall, F1-score, AUC-ROC
- [ ] **Comparación**: Tabla de performance por algoritmo
- [ ] **Feature importance**: Identificar variables más predictivas
- [ ] **Análisis de errores**: Casos mal clasificados

### **Fase 5: Interpretación y Storytelling**
- [ ] **Validación de hipótesis**: Confirmar/refutar hipótesis iniciales
- [ ] **Insights históricos**: Conectar hallazgos con contexto histórico
- [ ] **Visualizaciones finales**: Gráficos que cuentan la historia
- [ ] **Recomendaciones**: Lecciones para diseño de protocolos de emergencia

---

## 📈 Métricas de Éxito

### **Técnicas**
- **Accuracy objetivo**: >80% en test set
- **F1-score**: >0.75 (balance precision/recall)
- **AUC-ROC**: >0.85 (capacidad discriminativa)
- **Código limpio**: 100% reproducible, documentado

### **Académicas**
- **Storytelling**: Narrativa coherente y compelling
- **Insights noveles**: Al menos 3 descubrimientos no obvios
- **Comparación algorítmica**: Análisis detallado de pros/cons
- **Documentación completa**: Cumplir 100% requerimientos del proyecto

### **Aprendizaje**
- **Dominio técnico**: Aplicación correcta de todos los algoritmos del curso
- **Pensamiento crítico**: Interpretación beyond métricas
- **Comunicación**: Presentación clara para audiencia no-técnica

---

## ⚠️ Riesgos y Mitigaciones

### **Riesgos Técnicos**

#### **R1: Overfitting por dataset pequeño**
- **Mitigación**: Cross-validation rigurosa, regularización, ensemble methods

#### **R2: Valores faltantes en Age (19.9%)**
- **Mitigación**: Comparar múltiples estrategias de imputación, analizar impacto

#### **R3: Desbalance de features categóricas**
- **Mitigación**: Técnicas de encoding apropiadas, feature selection

### **Riesgos de Proyecto**

#### **R4: Scope creep (sobre-complicación)**
- **Mitigación**: Milestone claros, MVP first approach

#### **R5: Tiempo insuficiente para storytelling**
- **Mitigación**: Documentar insights durante análisis, no al final

---

## 📅 Timeline Propuesto

| Semana | Fase | Entregables | Responsable |
|--------|------|-------------|-------------|
| **1** | Setup + EDA | Notebooks 01, docs iniciales | Todo el equipo |
| **2** | Data Cleaning | Notebook 02, pipeline clean | Yahwthani, Omar |
| **3** | Feature Engineering | Notebook 03, nuevas features | Andrés, Héctor |
| **4** | Modeling | Notebooks 04-05, modelos base | Todo el equipo |
| **5** | Evaluation + Tuning | Notebook 06, modelo final | Yahwthani, Andrés |
| **6** | Storytelling + Docs | Reporte final, presentación | Todo el equipo |

---

## 🎉 Valor Esperado del Proyecto

### **Para el Aprendizaje**
- **Aplicación práctica** de todo el contenido del curso ML-Practical
- **Experiencia end-to-end** de proyecto de data science
- **Habilidades técnicas** en Python, pandas, scikit-learn, visualización

### **Para la Historia**
- **Validación cuantitativa** de narrativas históricas sobre el Titanic
- **Insights sociológicos** sobre estructura social de 1912
- **Lessons learned** aplicables a protocolos de emergencia modernos

### **Para la Carrera**
- **Portfolio piece** demostrable para empleadores
- **Metodología robusta** replicable en proyectos futuros
- **Storytelling skills** críticas para data scientists

---

## 📚 Referencias Iniciales

**Históricas**:
- Lord, Walter. "A Night to Remember" (1955) - Relato clásico del desastre
- British Board of Trade. "Report on the Loss of the S.S. Titanic" (1912) - Investigación oficial
- Encyclopedia Titanica - Base de datos histórica de pasajeros

**Técnicas**:
- Castillo, G. "ML-Practical.pdf" - Documento base del curso
- James, G. et al. "An Introduction to Statistical Learning" - Fundamentos teóricos
- Kaggle Learn - Machine Learning Course

**Datasets**:
- [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic) - Dataset principal
- [Encyclopedia Titanica](https://www.encyclopedia-titanica.org/) - Datos adicionales de validación

---

## ✅ Compromiso del Equipo

**Declaramos nuestro compromiso de**:
- Producir trabajo original y de alta calidad académica
- Citar apropiadamente todas las fuentes utilizadas
- Documentar honestamente challenges y limitaciones encontradas
- Colaborar efectivamente respetando las fortalezas individuales
- Entregar en tiempo y forma según el syllabus del curso

**Distribución tentativa de responsabilidades**:
- **Yahwthani Morales**: Project lead, data pipeline, documentation
- **Andrés López**: Feature engineering, model implementation  
- **Héctor Eguiarte**: Data visualization, storytelling
- **Omar Vidaña**: Model evaluation, performance analysis

---

## 🎯 Definición de Éxito

**Este proyecto será exitoso si**:

1. **Cumplimos objetivos académicos**: Nota ≥85% según rubrica del curso
2. **Generamos insights valiosos**: Descubrimos patrones no triviales en los datos
3. **Demostramos competencia técnica**: Aplicamos correctamente algoritmos ML
4. **Contamos historia compelling**: Conectamos datos con narrativa histórica humana
5. **Desarrollamos habilidades**: Cada miembro mejora capacidades individuales

**La historia que queremos contar**:
*"A través del análisis de datos del Titanic, no solo predecimos quién sobrevivió, sino que revelamos cómo las estructuras sociales de 1912 determinaron literalmente la vida y la muerte. Nuestros modelos de machine learning no solo clasifican pasajeros, sino que cuantifican la injusticia social y validan el heroísmo humano preservado en los datos históricos."*

---

*Propuesta aprobada por el equipo: 26 Mayo 2025*  
*Próxima revisión: 28 Mayo 2025*
-