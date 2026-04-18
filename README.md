# Basketball Performance Analysis Pipeline

## Project Overview

This project implements a professional, linear data science workflow for analyzing NCAA basketball performance data spanning 40+ years (1979-2021). The primary goal is to predict a team's win percentage and whether they are a winning team (classification) based on various performance drivers.

Our models are built entirely from scratch using fundamental Linear Algebra/Gradient Descent concepts in NumPy and validated against `scikit-learn`.

## Pipeline Structure

The pipeline is sequentially organized into 8 distinct Jupyter notebooks, ensuring reproducible data cleaning, EDA, hypothesis testing, feature engineering, and model training:

1. **`01_data_cleaning.ipynb`**: Loads raw basketball data, handles missing values (median imputation), removes duplicates, and performs IQR clipping for outlier treatment.
2. **`02_eda_visualization.ipynb`**: Conducts exploratory data analysis, visualizes outliers, distributions, correlations, and identifies performance drivers.
3. **`03_hypothesis_testing.ipynb`**: Statistically validates assumptions (e.g., impact of assist-to-turnover ratio, home-court advantage, defense vs offense metrics).
4. **`04_feature_engineering.ipynb`**: Develops features driven by EDA and Hypothesis insights (e.g., `point_diff`, `assist_turnover_ratio`, `home_win_pct`).
5. **`05_linear_regression.ipynb`**: A Simple Linear Regression model (scratch vs. sklearn baseline) using `simple_rating`.
6. **`06_multiple_regression.ipynb`**: A Multiple Linear Regression model estimating continuous `win_percentage` based on the 10-feature set.
7. **`07_logistic_regression.ipynb`**: A custom Logistic Regression model using class-weighted binary cross-entropy to handle class imbalance (70/30) aiming to predict `is_winning_team`.
8. **`08_model_comparison.ipynb`**: Compares evaluation metrics (MSE, RMSE, R2, Accuracy, Precision, Recall, F1) across all trained models.

## Results Context
Due to the dataset encompassing diverse eras of basketball (40+ years, inclusion of the 3-point line, pacing drift), baseline R2 and Accuracy metrics are inherently constrained. However, the models successfully capture the directional relationships of fundamental basketball metrics on team success and effectively show data science processes, model creation, and evaluation. 

## Requirements & Setup

- A Python 3.9+ environment is recommended.
- You can find all package specifications in `requirements.txt`.

### How to Run

A unified pipeline runner is provided to execute the entire analysis continuously.

From your command prompt in the project root directory, simply run:

```bash
python run_pipeline.py
```

This script will:
1. Automatically install the necessary Python dependencies.
2. Execute all notebooks (`01` through `08`) in chronological order and update them in place.
