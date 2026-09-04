# W1D1 Self-Review Checklist

## NumPy Fundamentals

- ✓ NumPy installed in virtual environment
- ✓ 1D array created and shape verified
- ✓ 2D array created and shape verified
- ✓ 3D array created and shape verified
- ✓ Broadcasting demonstrated
- ✓ Vectorised operations demonstrated
- ✓ No Python loops used
- ✓ Matrix multiplication completed

## Statistics

- ✓ Real CSV dataset loaded
- ✓ Mean calculated
- ✓ Standard deviation calculated
- ✓ Correlation calculated

## Code Quality

- ✓ Clear variable names used
- ✓ Code is readable
- ✓ No unnecessary loops
- ✓ No debug print statements left in code
- ✓ Dataset path uses pathlib

## Evidence

- ✓ Notebook outputs verified
- ✓ CIA review completed
- ✓ Second CIA interaction completed

## Git

- ✓ Working on feature branch
- ✓ Minimum 2 meaningful commits
- ✓ Changes pushed to GitHub
- ✓ Pull Request created

---

# W1D2 — Pandas Data Manipulation

## Pandas

- ✓ Pandas imported successfully
- ✓ DataFrame created and inspected
- ✓ Rows and columns selected
- ✓ Data filtered using conditions
- ✓ Data sorted successfully
- ✓ GroupBy operation completed
- ✓ Aggregation operations completed
- ✓ Merge operation completed
- ✓ Pandas operations verified

## Code Quality

- ✓ Clear variable names used
- ✓ Code is readable
- ✓ Appropriate Pandas operations used
- ✓ No unnecessary code left in notebook
- ✓ Notebook outputs verified

## Evidence

- ✓ Notebook outputs verified
- ✓ CIA review completed
- ✓ Second CIA interaction completed

## Git

- ✓ Feature branch used
- ✓ Meaningful commits completed
- ✓ Changes pushed to GitHub
- ✓ Pull Request created
- ✓ Pull Request merged into main

### W1D2 Status

✓ COMPLETE

---

# W1D3 — Data Loading, Cleaning & Inspection

## Data Loading

- ✓ CSV dataset loaded successfully
- ✓ Dataset shape inspected
- ✓ Column names inspected
- ✓ Data types checked
- ✓ Dataset values inspected

## Data Cleaning

- ✓ Missing values checked
- ✓ Duplicate rows checked
- ✓ Data cleaning completed
- ✓ Clean dataset verified
- ✓ Output dataset exported successfully

## Code Quality

- ✓ Clear variable names used
- ✓ Code is readable
- ✓ Appropriate Pandas operations used
- ✓ Dataset path handled correctly
- ✓ Notebook outputs verified

## Evidence

- ✓ Notebook outputs verified
- ✓ CIA review completed
- ✓ Second CIA interaction completed

## Git

- ✓ Feature branch used
- ✓ Meaningful commits completed
- ✓ Changes pushed to GitHub
- ✓ Pull Request created
- ✓ Pull Request merged into main

### W1D3 Status

✓ COMPLETE

---

# W1D4 — Exploratory Data Analysis

## Dataset Inspection

- ✓ Dataset loaded and inspected
- ✓ Summary statistics generated
- ✓ Missing values checked
- ✓ Duplicate rows checked

## EDA

- ✓ Five key observations documented
- ✓ Numeric distributions visualized
- ✓ Correlation heatmap created
- ✓ Category counts analyzed
- ✓ EDA findings documented
- ✓ Output dataset exported

## Key Observations

1. ✓ Highest population: Delhi
2. ✓ Lowest population: Kochi
3. ✓ Highest literacy rate: Kochi
4. ✓ Lowest literacy rate: Jaipur
5. ✓ Highest temperature: Chennai

## Data Quality

- ✓ Missing values: 0
- ✓ Duplicate rows: 0
- ✓ City counts verified

## Evidence

- ✓ Notebook outputs verified
- ✓ CIA review completed
- ✓ Second CIA interaction completed

## Git

- ✓ Feature branch used
- ✓ Meaningful commits completed
- ✓ Changes pushed to GitHub
- ✓ Pull Request created
- ✓ Pull Request merged into main

### W1D4 Status

✓ COMPLETE

---

# W1D5 — Data Visualisation

## Visualisation

- ✓ Dataset loaded successfully
- ✓ Numeric distributions visualized
- ✓ Bar chart created
- ✓ Population comparison visualized
- ✓ Temperature comparison visualized
- ✓ Literacy rate comparison visualized
- ✓ Correlation heatmap created
- ✓ Charts inspected and verified

## Data Analysis

- ✓ Population patterns visualized
- ✓ Temperature patterns visualized
- ✓ Literacy rate patterns visualized
- ✓ Correlation relationships visualized
- ✓ Visual findings documented

## Code Quality

- ✓ Clear variable names used
- ✓ Code is readable
- ✓ Appropriate visualization libraries used
- ✓ Notebook outputs verified
- ✓ No unnecessary code left in notebook

## Evidence

- ✓ Notebook outputs verified
- ✓ CIA review completed
- ✓ Second CIA interaction completed

## Git

- ✓ Feature branch used
- ✓ Meaningful commits completed
- ✓ Changes pushed to GitHub
- ✓ Pull Request created
- ✓ Pull Request merged into main

### W1D5 Status

✓ COMPLETE

---

# WEEK 1 FINAL STATUS

| W1D1 | NumPy Fundamentals | ✓ COMPLETE |
| W1D2 | Pandas Data Manipulation | ✓ COMPLETE |
| W1D3 | Data Loading, Cleaning & Inspection | ✓ COMPLETE |
| W1D4 | Exploratory Data Analysis | ✓ COMPLETE |
| W1D5 | Data Visualisation | ✓ COMPLETE |

---

## CIA Mentor Interactions

### Interaction 1 — Code Review

Discussed the implementation of SMOTE with the CIA mentor and reviewed the approach for handling class imbalance.

Key feedback:

- Check the class distribution before applying SMOTE.
- Use SMOTE only on the training data after train-test splitting.
- Verify the class distribution after resampling.
- Avoid data leakage when using oversampling techniques.

### Interaction 2 — Concept Review

Discussed how SMOTE generates synthetic minority-class samples instead of simply duplicating existing samples.

Key learning:

- SMOTE helps balance minority and majority classes.
- Synthetic samples are generated using interpolation between minority-class observations.
- The value of `k_neighbors` affects how synthetic samples are generated.
- The resampled dataset should be checked after applying SMOTE.

## CIA Outcome

The CIA interactions helped me understand both the practical implementation and the correct use of SMOTE in a machine learning workflow.

---

# Week 2 — Day 4 Self Review

## Topic

Train/Test Split & Cross-Validation

## What I Learned

Today I learned how to split a dataset into training and testing sets and how cross-validation is used to evaluate model performance.

## Practical Work Completed

- Created a dataset with numerical features and a binary target.
- Separated features (X) and target (y).
- Applied an 80/20 train-test split.
- Used `stratify=y` to maintain class distribution.
- Built a Pipeline using `StandardScaler` and `LogisticRegression`.
- Trained the model and made predictions.
- Evaluated the model on the test data.
- Applied 5-fold cross-validation.
- Calculated the mean cross-validation accuracy.
- Documented the cross-validation warning caused by the small minority class.

## Results

Test Accuracy: **100%**

Cross-validation scores:

- Fold 1: 100%
- Fold 2: 100%
- Fold 3: 66.67%
- Fold 4: 100%
- Fold 5: 66.67%

Mean Cross-Validation Accuracy: **86.67%**

## Key Learning

Train-test splitting helps evaluate a model on unseen data.

Cross-validation provides a more reliable estimate of model performance by evaluating the model across multiple folds.

Using `StandardScaler` inside a Pipeline helps prevent data leakage during cross-validation.

## Challenges

The dataset has only 3 minority-class samples, so using 5-fold cross-validation produced a warning.

A larger dataset would be more suitable for reliable cross-validation in a real project.

## CIA Interaction

- CIA Interaction 1: Completed — Train/Test Split
- CIA Interaction 2: Completed — Cross-Validation

## Final Takeaway

I learned how to split data correctly, build a preprocessing and model pipeline, evaluate test performance, and use cross-validation to better understand model performance.

---

# Week 2 — Day 5 Self Review

## Topic

End-to-End Preprocessing Pipeline

## What I Learned

Today I learned how to build an end-to-end preprocessing pipeline for machine learning.

## Practical Work Completed

- Created a dataset containing missing values and categorical data.
- Separated features and target.
- Identified numeric and categorical features.
- Applied median imputation to numeric features.
- Applied most-frequent imputation to categorical features.
- Applied StandardScaler to numeric features.
- Applied OneHotEncoder to categorical features.
- Combined preprocessing using ColumnTransformer.
- Created a complete preprocessing and Logistic Regression pipeline.
- Exported processed features to a CSV file.
- Verified the exported processed dataset.
- Tested the complete ML pipeline with predictions.

## Results

Original features: **4**

Processed features: **7**

Processed dataset: **10 rows × 7 columns**

Predictions matched the actual target values for all 10 samples.

## Key Learning

A preprocessing pipeline allows missing-value handling, encoding, scaling, and model training to be performed consistently as one workflow.

Using a Pipeline and ColumnTransformer makes the preprocessing process cleaner and helps avoid data leakage.

## CIA Interaction

- CIA Interaction 1: Completed — End-to-End Preprocessing Pipeline
- CIA Interaction 2: Completed — Missing Values, Encoding and Scaling

## Final Takeaway

I learned how to prepare raw data and transform it into ML-ready features using an end-to-end preprocessing pipeline.
