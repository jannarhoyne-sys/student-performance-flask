### Predicting Race/Ethnicity from Test Scores - Flask App
Can predict a student's race/ethnicity group (A-E) from their math, reading, and writing
scores. Model deployed to Heroku with GitHub Actions CI/CD pipeline.

live app:
https://student-performance-hoyne-18f09f53590a.herokuapp.com/


### Model
- **Dataset:** [Kaggle Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Model:** Logistic Regression, 36% test accuracy (75/25 stratified split, random_state=29), compared with a 32% baseline from always guessing the largest group
- **Design:** Page styling ('static/style.css') is adapted from [breast cancer Flask app](https://github.com/jannarhoyne-sys/breast-cancer-flask), with a teal color scheme and new proability-bar styles added for this app.

##
### Results

**Model comparison** (test set of 250 students; baseline = always guess group C)

| Model | Accuracy |
|---|---|
| Logistic Regression | 0.360 |
| Kernel SVM | 0.356 |
| Baseline (always group C) | 0.320 |
| KNN | 0.308 |
| Random Forest | 0.276 |

The best model only beats guessing by 4 points, and worse than Random Forest prediction.

##
When Logistic Regression scored alone and in combinations:

| Features | Accuracy | vs. baseline |
|---|---|---|
| math + reading + writing | 0.360 | +0.040 |
| math + reading | 0.336 | +0.016 |
| math | 0.336 | +0.016 |
| math + writing | 0.320 | 0.000 |
| reading | 0.320 | 0.000 |
| reading + writing | 0.320 | 0.000 |
| writing | 0.292 | −0.028 |

All combinations land within a few points of the baseline. Math is the only score with any
signal, reading adds nothing on its own, and writing alone is worse than guessing.

- **It predicts group C for about 68% of students**, even though only 32% are in group C.
  Class imbalance drives the predictions more than the scores do.
