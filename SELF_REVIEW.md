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
