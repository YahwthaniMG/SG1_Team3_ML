# 📝 Development Log - Titanic Survival Prediction

## 📅 Project Development Record

**Team**: SG1_Team3_ML  
**Members**: Andrés López, Héctor Eguiarte, Yahwthani Morales, Omar Vidaña  
**Subject**: COM 139 - Simulation & Visualization  
**University**: Universidad Panamericana  

---

## 🎯 Phase 1: Project Setup and Initialization

### ✅ **May 28, 2025 - Initial Configuration**

**Completed Tasks:**
- [x] Created professional project structure  
- [x] Set up virtual environment and dependencies  
- [x] Git repository setup with appropriate `.gitignore`  
- [x] Initial documentation in `README.md`

**Technical Decisions:**
- **Python 3.9** as the base version for compatibility  
- **Conda + pip** for hybrid dependency management  
- **Modular structure** separating notebooks, src, docs, and scripts  
- **Setup.py** for installation as a Python package

**Selected Tools:**
```yaml
Analysis: pandas, numpy, scipy
ML: scikit-learn, xgboost
Visualization: matplotlib, seaborn, plotly
Development: jupyter, black, flake8
```

**Identified Challenges:**
- ⚠️ Need to balance professional structure with academic simplicity  
- ⚠️ Managing dependency versions for reproducibility

---

## 🔍 Phase 2: Exploratory Data Analysis (EDA)

### ✅ **May 28, 2025 - EDA Completed**

**Dataset Characteristics:**
- **Source**: Kaggle Titanic Dataset
- **Dimensions**: 891 passengers × 12 features
- **Target variable**: Survived (38.4% survival rate)

**Key Findings:**

#### 📊 **Survival Insights**
1. **Gender is the most decisive factor**:
   - Women: 74.2% survival
   - Men: 18.9% survival
   - **4:1 ratio** in favor of women

2. **Social class critical**:
   - 1st class: 63.0% survival
   - 2nd class: 47.3% survival  
   - 3rd class: 24.2% survival

3. **Gender-class intersection revealed "Women and children first" pattern**:
   - Women 1st class: **96.8%** survival
   - Men 3rd class: **13.5%** survival

#### ❌ **Data Quality**
- **Cabin**: 77.1% missing values → Candidate for removal
- **Age**: 19.9% missing values → Requires strategic imputation
- **Embarked**: 0.2% missing values → Easy to fix

**Processing Decisions:**
- Remove non-predictive variables: PassengerId, Name, Ticket
- Imputation strategy for Age pending definition
- Feature engineering: family size, age categories, titles

**Tools Used:**
```python
# Effective visualizations generated
matplotlib + seaborn  # Statistical plots
plotly                # Interactive plots
pandas.crosstab()     # Categorical analysis
correlation matrix    # Numeric relationships
```

**Challenges Encountered:**

#### 🚧 **Challenge 1: Automatic Visualization**
**Problem**: Notebooks generate a lot of graphics that are lost when closing.  
**Implemented Solution**: 
- `save_plot()` function in `src/utils/helpers.py`.
- Automatically saves in multiple formats (PNG, SVG)
- Timestamp for versioning

#### 🚧 **Challenge 2: Complexity vs Insights Balance** 
**Problem**: Temptation to over-analyze vs need for clear insights
**Solution**: 
- Focus on top 3 predictive factors: Gender, Class, Age.
- Visualizations that tell a clear story
- Simple but effective metrics

#### 🚧 **Challenge 3: Interpretation of Correlations** 
**Problem**: Low correlations in numerical variables (-0.338 max).  
**Learning**: 
- Categorical variables more important than numerical variables.
- Need for feature engineering
- Interactions between critical variables

**References consulted:**
- [Kaggle Titanic Tutorials](https://www.kaggle.com/learn/intro-to-machine-learning)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- scikit-learn documentation for preprocessing

---

## 🔄 Phase 3: Data Cleaning & Preprocessing (Completed)

### ✅ **May 29, 2025 - Successful Data Cleaning**

**Implemented Strategies:**
- **Age (19.9% missing)**: Imputation by grouped median (Sex + Pclass)
- **Cabin (77.1% missing)**: Converted to binary variable `Cabin_Known`
- **Embarked (0.2% missing)**: Imputation with mode (Southampton)
- **Outliers**: Analyzed and retained (historically valid)

**Decisions Made:**
- Removal of PassengerId, Name, Ticket (non-predictive)
- Retained Fare outliers (legitimate luxury suites)
- Retained Age outliers (realistic infants/elderly in 1912)

---

## 🔧 Phase 4: Feature Engineering (Completed)

### ✅ **May 29, 2025 - Successful Feature Engineering**

**New Variables Created:**

#### 📊 **Successful Derived Variables:**
1. **FamilySize**: Families of 2-4 people → 55-72% survival
2. **IsAlone**: Accompanied (50.6%) vs Alone (30.4%) survival
3. **AgeGroup**: Children (57.4%) > Young Adults (33.7%) > Seniors (26.9%)
4. **FareBin**: Premium (58.1%) > High (45.5%) > Medium (30.4%) > Low (19.7%)
5. **Title**: Mrs (79.4%) > Miss (70.1%) > Master (57.5%) > Mr (15.7%)

#### 🔗 **Powerful Interaction Variables:**
- **Sex_Pclass**: female_Class1 (96.8%) vs male_Class3 (13.5%)
- **Age_Sex**: Adult_Female (75.3%) > Young (54.0%) > Adult_Male (16.6%)

**Strategic Encoding:**
- **Label**: Binary variables (Sex, Embarked)
- **Ordinal**: Ordered variables (AgeGroup, FareBin)  
- **One-Hot**: Nominal variables (Title, interactions)

**Final Result:**
- From 9 original variables → **29 features**
- **Top 3 predictors**: AgeSex_Adult_Female (0.486), SexPclass_female_Class1 (0.413), Title_Mrs (0.342)

#### 🚧 **Challenges Encountered:**

#### **Challenge 4: Feature Balance**
**Problem**: Risk of overfitting with 29 features in a dataset of 891 records  
**Solution Implemented**: 
- Correlation analysis to identify most important features
- Strategic encoding (avoiding dummy trap)
- Preparation for feature selection in modeling

#### **Challenge 5: Interpretability vs Performance**
**Problem**: Interaction variables improve prediction but complicate interpretation  
**Learning**: 
- Retain original variables for interpretation
- Use interaction variables for performance
- Clearly document each feature

---

## 🤖 Phase 5: Machine Learning Modeling (Completed)

### ✅ **May 29, 2025 - Successful Modeling**

**Implemented Algorithms:**
- **Logistic Regression**: Interpretable baseline (84.3% accuracy, AUC=0.91)
- **Random Forest**: Robust ensemble (83.2% accuracy, overfitting detected)
- **Support Vector Machine**: Complex boundaries (**WINNER**: 84.4% accuracy)
- **Naive Bayes**: Probabilistic baseline (82.0% accuracy)

**Final Best Model:**
- **Algorithm**: SVM with RBF kernel
- **Hyperparameters**: C=1, gamma='auto'
- **Test Performance**: 84.4% accuracy, F1=0.78, AUC=0.86
- **✅ GOAL ACHIEVED**: >80% accuracy

**Validation Process:**
- **Data Split**: 70% train, 10% validation, 20% test
- **Cross-Validation**: 5-fold stratified for robustness
- **Grid Search**: Hyperparameter optimization
- **Final Test**: Evaluation on unseen set

#### 🚧 **Challenges Encountered:**

#### **Challenge 7: Random Forest Overfitting**
**Problem**: Random Forest showed 99.2% accuracy in train vs 83.2% in validation
**Solution**: 
- Identified through train-val comparison
- SVM demonstrated better generalization
- Documented for future analysis

#### **Challenge 8: Optimal Metric Selection**
**Problem**: Balance between accuracy, precision, and recall for historical context
**Decision**: 
- F1-Score as main metric (balance precision-recall)
- AUC-ROC for discriminative capability
- Accuracy to meet academic goal (>80%)

#### **Challenge 9: Interpretability vs Performance**
**Problem**: SVM (winner) less interpretable than Logistic Regression
**Learning**: 
- Prioritize performance for academic goal
- Retain Logistic Regression for interpretation
- Feature importance not available in SVM (as expected)

---

## 📊 Phase 6: Model Evaluation & Interpretation (Completed)

### ✅ **May 29, 2025 - Deep Evaluation and Analysis Completed**

**Final Performance Analysis:**
- **Optimized SVM**: 84.4% test accuracy (goal >80% ✅)
- **Balanced Metrics**: F1=0.78, Precision=0.85, Recall=0.72, AUC=0.86
- **No Overfitting**: Consistent performance between train/val/test
- **Robustness Confirmed**: Stable cross-validation

**Revealing Error Analysis:**
- **16.2% Total Error**: 52 false positives + 92 false negatives
- **False Positives**: Mainly 3rd class women (optimistic prediction)
- **False Negatives**: Mostly men who survived unexpectedly
- **Human Insights**: Errors reflect exceptional cases from the tragedy

**Validation of Historical Hypotheses:**
- **✅ H1**: Women 3.9x more survival than men (74% vs 19%)
- **✅ H2**: 1st class (63%) > 2nd (47%) > 3rd (24%) survival
- **✅ H4**: 1st class women 97% vs 3rd class men 14%
- **Top Features**: AgeSex_Adult_Female, SexPclass_female_Class1, Title_Mrs

**Validated Historical Context:**
- **Birkenhead Protocol**: "Women and children first" clearly captured
- **Social Class**: Determined access to lifeboats
- **Limited Capacity**: Only 53% lifeboat capacity explained tragedy

#### 🚧 **Challenge 10: Error Case Interpretation**
**Problem**: How to explain why the model failed in specific cases?
**Analysis Performed**: 
- False positives: Young 3rd class women with high assigned probability
- False negatives: Men who survived against odds
- **Historical Insight**: Errors reflect the chaotic and human nature of the disaster

#### 🚧 **Challenge 11: Interpretability vs Accuracy Balance**
**Problem**: SVM doesn't offer direct feature importance like Random Forest
**Adopted Solution**: 
- Use feature importance from previous correlation analysis
- Validate with historical domain knowledge
- Prioritize final performance over immediate interpretability

#### 🚧 **Challenge 12: Demographic Subgroup Bias**
**Problem**: Uneven performance across genders and classes
**Finding**: 
- Model excellent at predicting female survival (Recall=97%)
- Conservative in predicting male survival (Precision=100%, Recall=21%)
- **Ethical Reflection**: Reflects real historical biases, not model biases

---

## 📊 Progress Metrics

| Phase | Completed | Estimated Time | Actual Time | Status |
|------|-----------|----------------|-------------|--------|
| Setup | 100% | 2h | 1.5h | ✅ |
| EDA | 100% | 6h | 4h | ✅ |
| Cleaning | 100% | 4h | 3h | ✅ |
| Feature Eng. | 100% | 3h | 2.5h | ✅ |
| Modeling | 100% | 6h | 4h | ✅ |
| Evaluation | 100% | 3h | 2h | ✅ |

**Total Progress**: 100% completed

---

## 🎓 Lessons Learned

### **Technical:**
1. **Structured EDA is fundamental** - Clear insights before modeling
2. **Visualization tells the story** - Graphs communicate better than numbers
3. **Categorical variables dominate** - In this dataset, gender/class > age/fare

### **Methodological:**
1. **Parallel documentation** - Write insights as they're discovered
2. **Modular code from start** - Helper functions save time
3. **Visual versioning** - Automatically save important graphs

### **Domain:**
1. **"Women and children first"** clearly reflected in data
2. **Social class** = lifeboat access
3. **Family** can be an advantage or disadvantage depending on size

---

## 🔮 Next Steps

### **Immediate (This Week):**
- [x] Implement Age imputation strategy
- [x] Basic feature engineering
- [x] Complete data cleaning pipeline
- [x] Notebook 02_data_cleaning.ipynb
- [x] Notebook 03_feature_engineering.ipynb
- [ ] Implement Machine Learning algorithms
- [ ] Notebook 04_modeling.ipynb

### **Next (Following Week):**
- [ ] Model comparison and tuning
- [ ] Cross-validation strategy
- [ ] Evaluation metrics
- [ ] Feature importance interpretation

### **Final:**
- [ ] Error analysis and model improvement
- [ ] Final storytelling
- [ ] Complete documentation
- [ ] Final technical report

---

## 📚 References and Resources

**Technical Documentation:**
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [Scikit-learn Preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)

**Analysis Inspiration:**
- Kaggle Titanic Kernels (Top notebooks)
- [Towards Data Science - Titanic](https://towardsdatascience.com/tagged/titanic)

**Methodology:**
- CRISP-DM Process
- ML-Practical.pdf (Course document)

---

*Log updated: May 29, 2025, 18:30*