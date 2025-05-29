# 🚢 Titanic Survival Prediction

## 📖 Project Description

This project uses Machine Learning techniques to predict RMS Titanic passenger survival based on demographic and socioeconomic characteristics. Developed as an academic project for the course COM 139 - Simulation & Visualization at Universidad Panamericana.

### 🎯 Objectives
- Analyze factors influencing Titanic survival
- Implement and compare different classification algorithms
- Create visualizations that tell the data story
- Discover hidden patterns in historical data
- Quantitatively validate the "women and children first" protocol

## 🏆 Key Results

- **🎯 Academic Goal**: ✅ **ACHIEVED** - Accuracy exceeding the required 80%
- **🤖 Best Model**: Support Vector Machine (SVM) with RBF kernel
- **📊 Final Performance**: **84.4% accuracy** on test set
- **🔍 Balanced Metrics**: F1-Score: 0.78, Precision: 0.85, Recall: 0.72, AUC-ROC: 0.86
- **🧪 Demonstrated Validation**: 87.0% accuracy on final validation data

### 📈 Algorithm Comparison

| Model | Accuracy | F1-Score | AUC-ROC | Interpretability |
|--------|----------|----------|---------|-------------------|
| **SVM (Winner)** | **84.4%** | **0.781** | **0.859** | Medium |
| Logistic Regression | 84.3% | 0.781 | **0.910** | **High** |
| Random Forest | 83.2% | 0.783 | 0.879 | Medium |
| Naive Bayes | 82.0% | 0.750 | 0.876 | Medium |

## 📊 Dataset and Features

- **Source**: [Kaggle - Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- **Dimensions**: 891 passengers × 12 original features → **29 engineered features**
- **Target variable**: Survived (38.4% historical survival rate)
- **Quality**: Complete missing value processing and advanced feature engineering

### 🔍 Top Most Predictive Features
1. **AgeSex_Adult_Female** (r=0.486): Adult women
2. **SexPclass_female_Class1** (r=0.413): First-class women  
3. **Title_Mrs** (r=0.342): Female social status

## 🏛️ Validated Historical Insights

- **✅ "Women and Children First" Protocol**: Women 74.2% vs Men 18.9% survival (4:1 ratio)
- **✅ Social Class Determinant**: 1st class (63%) > 2nd class (47%) > 3rd class (24%)
- **✅ Critical Intersection**: 1st class women 96.8% vs 3rd class men 13.5%
- **✅ Quantitative Validation**: Data confirms historical disaster narratives

## 📁 Project Structure

```
SG1_Team3_ML/
├── 📋 DOCUMENTATION
│   ├── docs/
│   │   ├── project_proposal.md          # Initial project proposal
│   │   ├── methodology.md               # Detailed CRISP-DM methodology
│   │   ├── data_dictionary.md           # Complete data dictionary
│   │   ├── development_log.md           # ⭐ Detailed development log
│   │   └── final_technical_report.md    # ⭐ Complete technical report
│
├── 📓 NOTEBOOKS (Complete ML Pipeline)
│   ├── notebooks/
│   │   ├── 01_exploratory_data_analysis.ipynb    # Complete EDA
│   │   ├── 02_data_cleaning.ipynb               # Data cleaning
│   │   ├── 03_feature_engineering.ipynb        # Feature engineering
│   │   ├── 04_modeling.ipynb                   # ⭐ Model training
│   │   ├── 05_model_evaluation.ipynb           # Evaluation and analysis
│   │   └── 06_final_predictions.ipynb          # ⭐ Final predictions
│
├── 📊 DATA
│   ├── data/
│   │   ├── raw/titanic.csv              # Original Kaggle dataset
│   │   └── processed/                   # Processed data and features
│
├── 🤖 MODELS
│   ├── models/
│   │   ├── best_model_svm.pkl          # ⭐ Final trained SVM model
│   │   └── model_metrics.json          # Model metrics and parameters
│
├── 📈 RESULTS
│   ├── results/
│   │   ├── figures/                    # All generated visualizations
│   │   └── reports/                    # Automatic HTML reports
│
├── 🔧 SOURCE CODE
│   ├── src/
│   │   └── utils/helpers.py            # Utility functions
│
└── 📋 CONFIGURATION
    ├── requirements.txt                 # Python dependencies
    ├── environment.yml                  # Conda environment
    └── setup.py                        # Package configuration
```

## 🔑 Key Files to Review

### 📋 **Main Documentation**
- **`docs/final_technical_report.md`** - Complete technical report with all results
- **`docs/development_log.md`** - Detailed development process log
- **`docs/methodology.md`** - Implemented CRISP-DM methodology

### 🧪 **Executable Notebooks**
- **`notebooks/04_modeling.ipynb`** - Model training and comparison
- **`notebooks/06_final_predictions.ipynb`** - Final predictions demonstration
- **`notebooks/01_exploratory_data_analysis.ipynb`** - Complete exploratory analysis

### 🤖 **Production Model**
- **`models/best_model_svm.pkl`** - Trained SVM model ready for use
- **`models/model_metrics.json`** - Complete performance metrics

## 🛠️ Installation and Execution

### Option 1: Conda (Recommended)
```bash
# Clone repository
git clone https://github.com/YahwthaniMG/SG1_Team3_ML.git
cd SG1_Team3_ML

# Create environment
conda env create -f environment.yml
conda activate SG1_Team3_ML

# Run notebooks
jupyter notebook notebooks/
```

### Option 2: pip + venv
```bash
# Clone repository
git clone https://github.com/YahwthaniMG/SG1_Team3_ML.git
cd SG1_Team3_ML

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run notebooks
jupyter notebook notebooks/
```

### 🚀 Quick Start

To see results immediately:

1. **View Results**: Open `docs/final_technical_report.md`
2. **Run Predictions**: Notebook `06_final_predictions.ipynb`
3. **Complete Pipeline**: Run notebooks 01-06 in order

## 📊 Prediction Demonstration

The final model can predict survival on new data:

```python
# Example usage of trained model
import joblib
model = joblib.load('models/best_model_svm.pkl')

# Model achieved in demonstration:
# - 87.0% accuracy on 100 test passengers
# - 35% predicted as survivors (vs 38.4% historical)
# - 78% high-confidence predictions
```

## 🎓 Demonstrated Academic Value

### ✅ **Achieved Technical Objectives**
- **Complete ML Pipeline**: CRISP-DM implemented end-to-end
- **Algorithm Comparison**: 4 algorithms systematically evaluated
- **Superior Performance**: 84.4% accuracy (target >80% ✅)
- **Rigorous Validation**: Cross-validation, test set holdout, balanced metrics

### 🏛️ **Historical Contribution**
- **Quantitative Validation**: "Women and children first" protocol statistically confirmed
- **Intersectionality**: Gender + Social class as critical determining factor  
- **Exceptional Cases**: Error analysis reveals extraordinary human stories
- **Modern Lessons**: Insights applicable to current emergency protocols

### 🔬 **Methodological Rigor**
- **Reproducibility**: All code and pipeline documented
- **Transparency**: Development log with all challenges and decisions
- **Validation**: Consistent and statistically significant results

## 👨‍🎓 Development Team

**SG1_Team3_ML** - Universidad Panamericana, Spring 2025

- **Andrés López Álvarez** - Feature Engineering & Modeling
- **Héctor Manuel Eguiarte Carlos** - Visualization & Storytelling  
- **Yahwthani Morales Gómez** - Project Lead & Data Pipeline
- **Omar Vidaña Rodríguez** - Model Evaluation & Performance Analysis

**Instructor**: Gabriel Castillo Cortés  
**Course**: COM 139 - Simulation & Visualization

## 📚 References and Sources

### **Historical Data**
- [Kaggle Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- Encyclopedia Titanica (historical validation)
- British Board of Trade Report (1912)

### **Technical Methodology**
- James, G. et al. "An Introduction to Statistical Learning"
- Castillo, G. "ML-Practical.pdf" (course base document)
- Scikit-learn documentation

### **Historical Context**
- Lord, Walter. "A Night to Remember" (1955)
- Official British disaster investigation (1912)

---

## 🎯 Conclusion

This project successfully demonstrates the application of Machine Learning to validate historical narratives, achieving not only academic technical objectives but also generating valuable insights about one of the most studied events in maritime history.

**The final SVM model not only predicts survival with 84.4% accuracy but also quantitatively reveals how 1912 social structure literally determined life and death on the Titanic.**

---

*Want to explore more? Start with `docs/final_technical_report.md` for the complete analysis or run `notebooks/06_final_predictions.ipynb` to see the model in action.*