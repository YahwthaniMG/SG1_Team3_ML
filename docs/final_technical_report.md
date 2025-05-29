# 📊 Reporte Técnico Final - Predicción de Supervivencia del Titanic

## 📋 Información del Proyecto

**Equipo**: SG1_Team3_ML  
**Integrantes**: Andrés López, Héctor Eguiarte, Yahwthani Morales, Omar Vidaña  
**Materia**: COM 139 - Simulación & Visualización  
**Universidad**: Universidad Panamericana  
**Fecha**: Mayo 2025  

---

## 🎯 Resumen Ejecutivo

### **Objetivo Alcanzado**
Desarrollamos un modelo de machine learning que predice la supervivencia de pasajeros del RMS Titanic con **84.4% de accuracy**, superando el objetivo académico del 80% y revelando patrones históricos significativos sobre la tragedia marítima más famosa de la historia.

### **Resultados Principales**
- **🏆 Mejor Modelo**: Support Vector Machine (SVM) con kernel RBF
- **📊 Performance**: 84.4% accuracy, F1=0.78, AUC=0.86
- **🎯 Insights Históricos**: Validación cuantitativa del protocolo "mujeres y niños primero"
- **⚖️ Factor Clave**: Intersección género-clase social determinó supervivencia

---

## 📊 Metodología y Datos

### **Dataset**
- **Fuente**: Kaggle Titanic Dataset
- **Dimensiones**: 891 pasajeros × 12 características originales
- **Variable Objetivo**: Supervivencia (38.4% tasa histórica)
- **Calidad**: Valores faltantes en Age (19.9%), Cabin (77.1%), Embarked (0.2%)

### **Proceso CRISP-DM**
1. **Data Understanding**: EDA completo identificó patrones género-clase
2. **Data Preparation**: Imputación inteligente, feature engineering avanzado
3. **Modeling**: 4 algoritmos comparados (Logistic Regression, Random Forest, SVM, Naive Bayes)
4. **Evaluation**: Validación cruzada, hyperparameter tuning, análisis de errores
5. **Deployment**: Modelo productivo con interpretación histórica

---

## 🔧 Feature Engineering

### **Variables Creadas (9 → 29 features)**

#### **Variables Derivadas Exitosas**
1. **FamilySize** (SibSp + Parch + 1): Familias 2-4 personas → 55-72% supervivencia
2. **IsAlone**: Acompañados (50.6%) vs Solos (30.4%) supervivencia  
3. **AgeGroup**: Child (57.4%) > Young_Adult (33.7%) > Senior (26.9%)
4. **FareBin**: Premium (58.1%) > High (45.5%) > Medium (30.4%) > Low (19.7%)
5. **Title** (extraído de nombres): Mrs (79.4%) > Miss (70.1%) > Master (57.5%) > Mr (15.7%)

#### **Variables de Interacción Críticas**
- **Sex_Pclass**: female_Class1 (96.8%) vs male_Class3 (13.5%)
- **Age_Sex**: Adult_Female (75.3%) > Young (54.0%) > Adult_Male (16.6%)

### **Top 3 Features Más Predictivas**
1. **AgeSex_Adult_Female** (r=0.486): Mujeres adultas
2. **SexPclass_female_Class1** (r=0.413): Mujeres primera clase  
3. **Title_Mrs** (r=0.342): Estado social femenino

---

## 🤖 Modelado y Resultados

### **Comparación de Algoritmos**

| Modelo | Accuracy | F1-Score | AUC-ROC | Overfitting | Interpretabilidad |
|--------|----------|----------|---------|-------------|-------------------|
| **SVM** | **84.4%** | **0.781** | **0.859** | ✅ No | Baja |
| Logistic Regression | 84.3% | 0.781 | **0.910** | ✅ No | **Alta** |
| Random Forest | 83.2% | 0.783 | 0.879 | ⚠️ Sí | Media |
| Naive Bayes | 82.0% | 0.750 | 0.876 | ✅ No | Media |

### **Modelo Final: SVM Optimizado**
- **Hiperparámetros**: C=1, kernel='rbf', gamma='auto'
- **Validación**: 5-fold cross-validation consistente
- **Generalización**: Performance estable en train/val/test

### **Métricas Detalladas**
- **Precision**: 84.7% (confiabilidad en predicciones positivas)
- **Recall**: 72.5% (capacidad de encontrar supervivientes)
- **F1-Score**: 78.1% (balance precision-recall)
- **AUC-ROC**: 85.9% (excelente capacidad discriminativa)

---

## 🔍 Análisis de Errores

### **16.2% Total de Errores (144 casos)**

#### **Falsos Positivos (52 casos)**
- **Perfil**: Principalmente mujeres de 3ª clase jóvenes
- **Interpretación**: Modelo optimista sobre supervivencia femenina
- **Contexto Histórico**: Casos excepcionales donde ubicación/circunstancias impidieron evacuación

#### **Falsos Negativos (92 casos)**  
- **Perfil**: Mayormente hombres (86/92) que sobrevivieron inesperadamente
- **Interpretación**: Casos de heroísmo, suerte o ayuda en evacuación
- **Valor Humano**: Revelan historias extraordinarias de supervivencia

---

## 🏛️ Validación Histórica

### **Hipótesis Confirmadas**

#### **H1 - Protocolo "Mujeres y Niños Primero"** ✅
- **Evidencia**: Mujeres 74.2% vs Hombres 18.9% supervivencia
- **Ratio**: 3.9x mayor supervivencia femenina
- **Contexto**: Protocolo Birkenhead aplicado fielmente

#### **H2 - Clase Social Determinante** ✅  
- **Evidencia**: 1ª clase (63.0%) > 2ª clase (47.3%) > 3ª clase (24.2%)
- **Interpretación**: Acceso privilegiado a botes salvavidas
- **Implicación Social**: Estructura social de 1912 reflejada en supervivencia

#### **H4 - Intersección Género-Clase** ✅
- **Evidencia Extrema**: Mujeres 1ª clase (96.8%) vs Hombres 3ª clase (13.5%)
- **Factor Multiplicativo**: Género + Clase social = Predicción más precisa
- **Top Features**: Las 3 variables más predictivas involucran esta intersección

### **Validación con Datos Históricos**
- **Capacidad Botes**: 1,178 personas (53% de 2,224 a bordo)
- **Supervivientes Reales**: ~710 personas (32% histórico vs 38.4% dataset)
- **Protocolo**: Nuestro modelo captura fielmente el "mujeres y niños primero"

---

## ⚖️ Análisis de Bias y Equidad

### **Performance por Subgrupos**

#### **Por Género**
- **Mujeres**: Recall=97.4% (excelente detectando supervivientes femeninas)
- **Hombres**: Precision=100% (conservador, solo predice supervivencia cuando muy seguro)

#### **Por Clase Social**  
- **Clase 1**: Precision=97% (muy preciso para primera clase)
- **Clase 2**: Accuracy=92.4% (mejor performance general)
- **Clase 3**: Recall=62% (dificultad prediciendo supervivencia tercera clase)

### **Reflexión Ética**
El modelo refleja **sesgos históricos reales** de la época (1912), no sesgos algorítmicos. Las diferencias en performance por subgrupos reflejan las desigualdades sociales que determinaron el acceso a la supervivencia.

---

## 🧠 Lecciones para Protocolos Modernos

### **Insights Aplicables**
1. **Planificación de Evacuación**: Considerar todas las clases sociales equitativamente
2. **Protocolos Claros**: Definir prioridades transparentes y justas
3. **Capacidad Suficiente**: Asegurar recursos de emergencia para 100% de ocupantes
4. **Análisis Predictivo**: Usar ML para optimizar planes de evacuación

### **Valor del Análisis Histórico**
- **Cuantificación**: Convertir narrativas históricas en datos medibles
- **Validación**: Confirmar o refutar teorías históricas con evidencia estadística
- **Aprendizaje**: Extraer lecciones aplicables a situaciones modernas

---

## 📈 Robustez y Limitaciones

### **Fortalezas del Modelo**
- **✅ Sin Overfitting**: Performance consistente entre conjuntos
- **✅ Generalización**: AUC estable en cross-validation (0.856 ± 0.031)
- **✅ Interpretabilidad**: Resultados alineados con conocimiento histórico
- **✅ Reproducibilidad**: Pipeline documentado y replicable

### **Limitaciones Identificadas**
- **⚠️ Tamaño Dataset**: 891 muestras para 29 features (ratio 30:1)
- **⚠️ Datos Faltantes**: 19.9% imputación en Age puede introducir sesgo
- **⚠️ Supervivientes Sesgados**: Solo pasajeros en botes, no víctimas en agua
- **⚠️ Interpretabilidad SVM**: Kernel RBF dificulta explicación directa

### **Posibles Mejoras**
- **Ensemble Methods**: Combinar múltiples modelos para mayor robustez
- **Datos Externos**: Incorporar información de ubicación de cabinas
- **Análisis Temporal**: Considerar momento exacto del hundimiento
- **Validación Cruzada**: Temporal si se consiguen datos de otros naufragios

---

## 🎯 Conclusiones

### **Objetivos Académicos** ✅
- **Performance**: 84.4% accuracy > 80% objetivo
- **Metodología**: CRISP-DM completo aplicado
- **Algoritmos**: 4 técnicas ML comparadas sistemáticamente
- **Documentación**: Development log completo con challenges

### **Contribución Histórica** 🏛️
- **Validación Cuantitativa**: Protocolo "mujeres y niños primero" confirmado estadísticamente
- **Interseccionalidad**: Género + Clase social como factor determinante crítico  
- **Casos Excepcionales**: Errores del modelo revelan historias humanas extraordinarias
- **Lecciones Modernas**: Insights aplicables a protocolos de emergencia actuales

### **Impacto Técnico** 🔬
- **Feature Engineering**: 29 variables creadas capturan patrones históricos complejos
- **Error Analysis**: 16.2% errores ofrecen insights sobre naturaleza caótica del desastre
- **Reproducibilidad**: Pipeline completo disponible para investigación futura
- **Metodología**: Framework aplicable a análisis de otros eventos históricos

---

## 📚 Referencias y Recursos

### **Fuentes de Datos**
- [Kaggle Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- Encyclopedia Titanica (validación histórica)
- British Board of Trade Report (1912)

### **Metodología Técnica**
- James, G. et al. "An Introduction to Statistical Learning"
- Castillo, G. "ML-Practical.pdf" (documento del curso)
- Documentación scikit-learn

### **Contexto Histórico**
- Lord, Walter. "A Night to Remember" (1955)
- Investigación oficial británica del desastre (1912)
- Archivos históricos navales

---

**Reporte Técnico Final**  
*Proyecto SG1_Team3_ML*  
*Universidad Panamericana - Mayo 2025*