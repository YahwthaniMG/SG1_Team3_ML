# 🔬 Project Methodology - Titanic Survival Prediction

## 📋 Methodological Framework

**Base Process**: CRISP-DM (Cross-Industry Standard Process for Data Mining)  
**Approach**: Exploratory analysis → Comparative modeling → Interpretive storytelling  
**Paradigm**: Supervised Learning - Binary classification  

---

## 🎯 1. Business Understanding

### **Problem Definition**
- **Type**: Binary classification (Survived: Yes/No)
- **Context**: Historical analysis with sociological implications
- **Target metrics**: Accuracy >80%, High interpretability
- **Stakeholders**: Academics, historians, ML students

### **Success Criteria**
1. **Technical**: Model performance better than random baseline (50%)
2. **Academic**: Meet 100% of ML-Practical.pdf requirements
3. **Interpretive**: Generate historically validatable insights
4. **Educational**: Demonstrate mastery of course algorithms

---

## 📊 2. Data Understanding

### **Exploratory Analysis Strategy**

#### **2.1 Univariate Analysis**
```python
# For each variable:
# - Distribution (histograms, boxplots)
# - Descriptive statistics (mean, median, mode)
# - Missing values (quantity, pattern)
# - Outliers (visual and statistical detection)
```

#### **2.2 Bivariate Analysis**
```python
# Target variable vs predictors:
# - Contingency tables (categorical)
# - Correlations (numeric)
# - Comparative visualizations
# - Statistical significance tests
```

#### **2.3 Multivariate Analysis**
```python
# Variable interactions:
# - Correlation matrices
# - Exploratory factor analysis
# - Clustering to identify groups
# - Correspondence analysis
```

### **Data Quality - Criteria**

| Dimension | Criterion | Action |
|-----------|----------|---------|
| **Completeness** | <5% missing → OK<br>5-20% → Impute<br>>20% → Evaluate removal | Age: 19.9% → Impute<br>Cabin: 77.1% → Remove |
| **Consistency** | Values in expected ranges | Age: [0-80] ✓<br>Fare: [0-512] ✓ |
| **Accuracy** | Consistency with historical sources | Validate with Encyclopedia Titanica |
| **Relevance** | Correlation with target variable | Keep \|corr\| > 0.05 |

---

## 🛠️ 3. Data Preparation

### **3.1 Cleaning Strategy**

#### **Missing Values**
```python
# Age (19.9% missing):
strategies = {
    'simple': df['Age'].fillna(df['Age'].median()),
    'group_median': df.groupby(['Sex', 'Pclass'])['Age'].transform('median'),
    'predictive': RandomForestRegressor(features=['Pclass', 'Sex', 'SibSp', 'Parch', 'Fare'])
}
# Selection: Compare resulting distributions
```

#### **Outliers**
```python
# Criterion: IQR method
def detect_outliers(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    return (column < Q1 - 1.5*IQR) | (column > Q3 + 1.5*IQR)

# Action: Investigate, don't automatically remove
```

### **3.2 Feature Engineering Strategy**

#### **Derived Variables**
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

#### **Theoretical Justification**
- **FamilySize**: Hypothesis of family protection vs overload
- **Title**: More granular social status indicator than Pclass
- **AgeGroup**: "Children first" policy in age groups
- **FareBin**: Wealth proxy independent of class

### **3.3 Encoding Strategy**

#### **Categorical Variables**
```python
encoding_strategy = {
    'Sex': 'LabelEncoder',  # Binary: male=0, female=1
    'Embarked': 'OneHotEncoder',  # Nominal: C, Q, S
    'Title': 'TargetEncoder',  # High cardinality
    'AgeGroup': 'OrdinalEncoder',  # Natural ordinal
    'Pclass': 'keep_numeric'  # Already ordinal
}
```

### **3.4 Feature Selection**

#### **Selection Criteria**
1. **Correlation**: |correlation| > 0.05 with target
2. **Variance**: Variance threshold > 0.01
3. **Multicollinearity**: VIF < 5.0
4. **Domain knowledge**: Historical/theoretical relevance

#### **Methods to Compare**
```python
selection_methods = [
    'SelectKBest(chi2)',  # Univariate
    'RFE(LogisticRegression)',  # Wrapper
    'SelectFromModel(RandomForest)',  # Embedded
    'manual_domain_knowledge'  # Expert
]
```

---

## 🤖 4. Modeling Strategy

### **4.1 Selected Algorithms**

#### **Algorithm Justification**

| Algorithm | Justification | Expected Strengths | Weaknesses |
|-----------|---------------|---------------------|-------------|
| **Logistic Regression** | Interpretable baseline, linear assumptions | Interpretable coefficients, calibrated probabilities | Assumes linearity |
| **Random Forest** | Handles interactions, robust | Feature importance, handles outliers | Less interpretable |
| **SVM** | Complex boundaries, kernels | Effective in high dimensions | Sensitive hyperparameters |
| **Naive Bayes** | Probabilistic baseline | Fast, handles missing values | Assumes independence |

### **4.2 Validation Strategy**

#### **Data Splitting**
```python
# Stratified to maintain survival proportion
train_size = 0.70  # 623 samples
val_size = 0.15    # 134 samples  
test_size = 0.15   # 134 samples

# Stratified for class balance
stratify_on = ['Survived', 'Sex', 'Pclass']
```

#### **Cross-Validation**
```python
cv_strategy = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
# For model selection and hyperparameter tuning
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

### **5.1 Performance Metrics**

#### **Primary Metrics**
```python
primary_metrics = {
    'accuracy': 'Total correct proportion',
    'f1_score': 'Precision-recall balance',
    'roc_auc': 'Discriminative capability',
    'classification_report': 'Class detail'
}
```

#### **Context-Specific Metrics**
- **Academic**: Accuracy (interpretive simplicity)
- **Medical/Safety**: Recall (avoid false negatives)
- **Historical**: Precision (confidence in positive predictions)
- **Scientific**: AUC-ROC (threshold-independent)

### **5.2 Model Comparison Framework**

#### **Comparison Criteria**
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

#### **Misclassified Case Analysis**
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

#### **Structured Narrative**
1. **Context Setting**: "It was April 14, 1912..."
2. **Data Introduction**: "891 human stories in numbers..."
3. **Pattern Discovery**: "The data reveals that..."
4. **Model Insights**: "Our algorithms discovered..."
5. **Historical Validation**: "This confirms that..."
6. **Modern Implications**: "Today this means..."

### **6.2 Visualization Strategy**

#### **By Project Phase**
```python
viz_by_phase = {
    'EDA': ['distributions', 'correlations', 'crosstabs'],
    'Preprocessing': ['before_after_cleaning', 'feature_distributions'],
    'Modeling': ['learning_curves', 'validation_curves'],
    'Evaluation': ['confusion_matrices', 'roc_curves', 'feature_importance'],
    'Interpretation': ['decision_boundaries', 'prediction_examples']
}
```

#### **Design Principles**
- **Clarity**: Clear message in 5 seconds
- **Honesty**: No misleading scales/colors
- **Accessibility**: Colorblind-friendly palettes
- **Narrative**: Each chart tells part of the story

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
- **Rationale**: Why each technical decision was made
- **Alternatives**: Other options considered
- **Trade-offs**: Advantages/disadvantages of the choice
- **Results**: Measurable impact of the decision

---

## ✅ 9. Quality Assurance

### **9.1 Reproducibility Checklist**
- [ ] Fixed random seeds throughout pipeline
- [ ] Library versions specified
- [ ] Original data preserved and immutable
- [ ] Pipeline documented step-by-step
- [ ] Independently verifiable results

### **9.2 Validation Protocol**
- [ ] Cross-validation in model selection
- [ ] Hold-out test set never seen until final
- [ ] Metrics reported with confidence intervals
- [ ] Model assumptions verified
- [ ] Results consistent with domain knowledge

---

*Methodology approved: May 26, 2025*  
*Version: 1.0*  
*Next review: Upon completing each phase*