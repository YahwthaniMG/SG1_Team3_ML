# 🚢 Project Proposal: Titanic Survival Prediction

## 📋 Project Information

**Title**: RMS Titanic Survival Prediction using Machine Learning  
**Team**: SG1_Team3_ML  
**Course**: COM 139 - Simulation & Visualization  
**University**: Universidad Panamericana  
**Semester**: Spring 2025  

**Team Members**:
- Andrés López Álvarez
- Héctor Manuel Eguiarte Carlos  
- Yahwthani Morales Gómez
- Omar Vidaña Rodríguez

---

## 🎯 Main Objective

**Develop a machine learning model to predict RMS Titanic passenger survival** based on demographic and socioeconomic characteristics, while uncovering historical patterns that explain determining factors in history's most famous maritime tragedy.

### Specific Objectives

1. **Exploratory Analysis**: Identify survival patterns by gender, social class, age, and origin
2. **Accurate Prediction**: Achieve >80% accuracy in binary classification
3. **Interpretability**: Explain which factors were most decisive for survival
4. **Storytelling**: Tell the human story behind statistical data
5. **Algorithm Comparison**: Evaluate multiple ML techniques per course requirements

---

## 📊 Dataset and Justification

### **Selected Dataset**
- **Source**: [Kaggle - Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- **Size**: 891 passengers × 12 features
- **Type**: Supervised binary classification
- **Target variable**: Survived (0/1)

### **Why Titanic?**

#### **Historical Relevance**
- Iconic event that changed global maritime regulations
- Reflects early 20th century social structure
- Abundant historical documentation to validate insights

#### **Data Quality**
- Clean, well-documented dataset
- Sufficient size for ML without being overwhelming
- Good balance of numeric and categorical variables
- Survival rate (38.4%) avoids extreme class imbalance issues

#### **Appropriate Complexity**
- **Simple enough**: Clear patterns identifiable in EDA
- **Complex enough**: Requires feature engineering and algorithm comparison
- **Storytelling rich**: Data that tells a compelling human story

#### **Academic Applicability**
- Allows application of all course algorithms: Logistic Regression, Random Forest, SVM, Naive Bayes
- Opportunity for creative feature engineering
- Clearly interpretable evaluation metrics

---

## 🔍 Research Hypotheses

### **Main Hypothesis**
*"Titanic survival was primarily determined by the intersection of gender, social class, and age, reflecting 'women and children first' social norms modulated by economic power"*

### **Specific Hypotheses**

1. **H1 - Gender**: Women had significantly higher survival rates than men
2. **H2 - Social Class**: First-class passengers had higher survival than second and third class
3. **H3 - Age**: Children and young adults had an advantage over older adults
4. **H4 - Interaction**: The protective effect of female gender was amplified in higher social classes
5. **H5 - Family**: Family size had non-linear effects (medium families advantage, large families disadvantage)

---

## 🛠️ Proposed Methodology

### **Phase 1: Exploratory Analysis (Completed)**
- [x] Data loading and initial inspection
- [x] Quality analysis (missing values, outliers)
- [x] Univariate and bivariate distributions  
- [x] Correlations and initial patterns
- [x] Descriptive visualizations

### **Phase 2: Data Preparation**
- [ ] **Cleaning**: Handling missing values in Age, Cabin, Embarked
- [ ] **Feature Engineering**: 
  - Family size (SibSp + Parch)
  - Titles extracted from names (Mr, Mrs, Miss, Master)
  - Age and fare categorization
  - Interaction variables (gender × class)
- [ ] **Encoding**: Categorical to numeric variables
- [ ] **Scaling**: Numeric variable normalization

### **Phase 3: Modeling**
- [ ] **Split**: Train/Validation/Test (70/15/15)
- [ ] **Baseline**: Simple model for comparison
- [ ] **Algorithms to implement**:
  - Logistic Regression (interpretability)
  - Random Forest (handling interactions)
  - Support Vector Machine (complex boundaries)
  - Naive Bayes (probabilistic baseline)
- [ ] **Cross-validation**: K-fold for robustness
- [ ] **Hyperparameter tuning**: Grid search for optimization

### **Phase 4: Evaluation and Comparison**
- [ ] **Metrics**: Accuracy, Precision, Recall, F1-score, AUC-ROC
- [ ] **Comparison**: Performance table by algorithm
- [ ] **Feature importance**: Identify most predictive variables
- [ ] **Error analysis**: Misclassified cases

### **Phase 5: Interpretation and Storytelling**
- [ ] **Hypothesis validation**: Confirm/refute initial hypotheses
- [ ] **Historical insights**: Connect findings with historical context
- [ ] **Final visualizations**: Charts that tell the story
- [ ] **Recommendations**: Lessons for modern emergency protocol design

---

## 📈 Success Metrics

### **Technical**
- **Target accuracy**: >80% on test set
- **F1-score**: >0.75 (precision/recall balance)
- **AUC-ROC**: >0.85 (discriminative capability)
- **Clean code**: 100% reproducible, documented

### **Academic**
- **Storytelling**: Coherent and compelling narrative
- **Novel insights**: At least 3 non-obvious discoveries
- **Algorithm comparison**: Detailed pros/cons analysis
- **Complete documentation**: Meet 100% project requirements

### **Learning**
- **Technical mastery**: Correct application of all course algorithms
- **Critical thinking**: Interpretation beyond metrics
- **Communication**: Clear presentation for non-technical audience

---

## ⚠️ Risks and Mitigations

### **Technical Risks**

#### **R1: Overfitting due to small dataset**
- **Mitigation**: Rigorous cross-validation, regularization, ensemble methods

#### **R2: Missing values in Age (19.9%)**
- **Mitigation**: Compare multiple imputation strategies, analyze impact

#### **R3: Categorical feature imbalance**
- **Mitigation**: Appropriate encoding techniques, feature selection

### **Project Risks**

#### **R4: Scope creep (over-complication)**
- **Mitigation**: Clear milestones, MVP first approach

#### **R5: Insufficient time for storytelling**
- **Mitigation**: Document insights during analysis, not just at end

---

## 📅 Proposed Timeline

| Week | Phase | Deliverables | Responsible |
|--------|------|-------------|-------------|
| **1** | Setup + EDA | Notebooks 01, initial docs | Whole team |
| **2** | Data Cleaning | Notebook 02, clean pipeline | Yahwthani, Omar |
| **3** | Feature Engineering | Notebook 03, new features | Andrés, Héctor |
| **4** | Modeling | Notebooks 04-05, base models | Whole team |
| **5** | Evaluation + Tuning | Notebook 06, final model | Yahwthani, Andrés |
| **6** | Storytelling + Docs | Final report, presentation | Whole team |

---

## 🎉 Expected Project Value

### **For Learning**
- **Practical application** of all ML-Practical course content
- **End-to-end experience** of data science project
- **Technical skills** in Python, pandas, scikit-learn, visualization

### **For History**
- **Quantitative validation** of historical Titanic narratives
- **Sociological insights** about 1912 social structure
- **Lessons learned** applicable to modern emergency protocols

### **For Career**
- **Portfolio piece** demonstrable to employers
- **Robust methodology** replicable in future projects
- **Storytelling skills** critical for data scientists

---

## 📚 Initial References

**Historical**:
- Lord, Walter. "A Night to Remember" (1955) - Classic disaster account
- British Board of Trade. "Report on the Loss of the S.S. Titanic" (1912) - Official investigation
- Encyclopedia Titanica - Historical passenger database

**Technical**:
- Castillo, G. "ML-Practical.pdf" - Course base document
- James, G. et al. "An Introduction to Statistical Learning" - Theoretical foundations
- Kaggle Learn - Machine Learning Course

**Datasets**:
- [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic) - Primary dataset
- [Encyclopedia Titanica](https://www.encyclopedia-titanica.org/) - Additional validation data

---

## ✅ Team Commitment

**We commit to**:
- Producing original, high-quality academic work
- Properly citing all sources used
- Honestly documenting challenges and limitations encountered
- Collaborating effectively while respecting individual strengths
- Delivering on time according to course syllabus

**Tentative responsibility distribution**:
- **Yahwthani Morales**: Project lead, data pipeline, documentation
- **Andrés López**: Feature engineering, model implementation  
- **Héctor Eguiarte**: Data visualization, storytelling
- **Omar Vidaña**: Model evaluation, performance analysis

---

## 🎯 Definition of Success

**This project will be successful if**:

1. **We meet academic goals**: Grade ≥85% per course rubric
2. **We generate valuable insights**: Discover non-trivial data patterns
3. **We demonstrate technical competence**: Correctly apply ML algorithms
4. **We tell a compelling story**: Connect data with human historical narrative
5. **We develop skills**: Each member improves individual capabilities

**The story we want to tell**:
*"Through Titanic data analysis, we not only predict who survived, but reveal how 1912 social structures literally determined life and death. Our machine learning models don't just classify passengers - they quantify social injustice and validate human heroism preserved in historical data."*

---

*Proposal approved by team: May 26, 2025*  
*Next review: May 28, 2025*