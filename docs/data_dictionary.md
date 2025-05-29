# 📊 Data Dictionary - Dataset Titanic

## 📋 General Information

- **Source**: [Kaggle - Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- **Dimensions**: 891 rows × 12 columns
- **Problem type**: Binary classification (Survival)
- **Target variable**: `Survived`.

## 📝 Description of Variables

| Variable | Type | Description | Possible Values | Missing Values |
|----------|------|-------------|------------------|-------------------|
| **PassengerId** | int64 | Unique passenger identifier | 1-891 | 0 (0.0%) |
| **Survived** | int64 | **Target variable** - Survival of passenger | 0 = Died<br>1 = Survived | 0 (0.0%) |
| **Pclass** | int64 | Ticket class 1 = First class<br>2 = Second class<br>3 = Third class<br>4 = Third class<br>5 = First class<br>5 = Second class<br>5 = Third class<br>6 = Third class 0 (0.0%) |
| **Name** | object | Passenger's full name | Free text | 0 (0.0%) |
| **Sex** | object | Passenger's gender: 'male' = Male<br>'female' = Female | 0 (0.0%) |
| **Age** | float64 | Passenger age in years | 0.42 - 80.0 years | 177 (19.9%) |
| **SibSp** | int64 | Number of siblings/spouses on board | 0-8 | 0 (0.0%) |
| **Parch** | int64 | Number of parents/children on board | 0-6 | 0 (0.0%) |
| **Ticket** | object | Ticket number | Alphanumeric | 0 (0.0%) |
| **Fare** | float64 | Fare paid for the ticket | $0.00 - $512.33 | 0 (0.0%) |
| **Cabin** | object | Booth number | Alphanumeric (ej: C85) | 687 (77.1%) |
| **Embarked** | object | Port of embarkation | C = Cherbourg<br>Q = Queenstown<br>S = Southampton | 2 (0.2%) |

## 📈 Descriptive Statistics

### Numerical Variables

| Statistics | PassengerId | Survived | Pclass | Age | SibSp | Parch | Fare |
|-------------|-------------|----------|--------|-----|-------|-------|------|
| **Mean** | 446.0 | 0.384 | 2.31 | 29.7 | 0.52 | 0.38 | 32.20 |
| **Median** | 446.0 | 0.0 | 3.0 | 28.0 | 0.0 | 0.0 | 14.45 |
| **Mode** | - | 0 | 3 | 24.0 | 0 | 0 | 8.05 |
| **Standard Deviation** | 257.4 | 0.487 | 0.84 | 14.5 | 1.10 | 0.81 | 49.69 |
| **Minimum** | 1.0 | 0.0 | 1.0 | 0.42 | 0.0 | 0.0 | 0.00 |
| **Maximun** | 891.0 | 1.0 | 3.0 | 80.0 | 8.0 | 6.0 | 512.33 |

### Categorical Variables

| Variable | Unique Values | Most Frequent Value | Frequency |
|----------|----------------|---------------------|------------|
| **Sex** | 2 | 'male' | 577 (64.8%) |
| **Embarked** | 3 | 'S' | 644 (72.4%) |
| **Pclass** | 3 | 3 | 491 (55.1%) |

## 🎯 Target Variable: Survived

- **Distribution**:
  - Fatalities (0): 549 passengers (61.6%).
  - Survivors (1): 342 passengers (38.4%)
- Overall Survival Rate**: 38.4%.

## 🔍 Identified Patterns

### 👫 By Gender
- **Women**: 74.2% survival (233/314)
- **Men**: 18.9% survival (109/577)
- **Difference**: Females were ~4x more likely to survive.

### 🎫 By Class
- **First class**: 63.0% survival rate (136/216)
- **Second class**: 47.3% survival rate (87/184)
- **Third class**: 24.2% survival (119/491)
- **Pattern**: Survival inversely proportional to the class

### ⚓ By Port of Embarkation
- **Cherbourg (C)**: 55.4% survival rate (93/168)
- **Queenstown (Q)**: 39.0% survivability (30/77)
- **Southampton (S)**: 33.7% survival (217/644)

### 👨‍👩‍👧‍👦 Combined Analysis (Gender + Class)
| Gender | Class | Survival Rate |
|--------|-------|----------------------|
| Women | 1 | 96.8% |
| Women | 2 | 92.1% |
| Women | 3 | 50.0% |
| Men | 1 | 36.9% |
| Men | 2 | 15.7% |
| Men | 3 | 13.5% |

## 🔗 Correlations with Survival

| Variable | Correlation | Interpretation |
|----------|-------------|----------------|
| **Fare** | +0.257 | Higher rate → Higher survival |
| **Parch** | +0.082 | More family members (parents/children) → Slight improvement. |
| **Age** | -0.077 | Older age → Slight decrease |
| **SibSp** | -0.035 | More siblings/spouses → Slight decrease. |
| **Pclass** | -0.338 | Higher class (lower number) → Greater survival |

## ❌ Data Quality

### Missing Values by Priority of Care

1. **Cabin (77.1% missing)**: 
   - Possible deletion of variable
   - Or creation of binary variable "Cabin_Known".

2. **Age (19.9% missing)**:
   - Requires imputation (mean, median, or predictive model).
   - Important variable for analysis

3. **Embarked (0.2% missing)**:
   - Easy to impute (mode = 'S')
   - Minimal impact

## 🚀 Processing Recommendations

1. **Remove**: PassengerId, Name, Ticket (not predictive)
2. **Impute**: Age (with appropriate strategy)
3. **Code**: Categorical variables (Sex, Embarked)
4. **Feature Engineering**: 
   - Family size (SibSp + Parch)
   - Age categories
   - Titles extracted from the name
5. **Outliers**: Review extreme values in Fare and Age

---
*Last update: May 26, 2025.