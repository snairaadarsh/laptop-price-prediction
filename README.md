💻 Laptop Price Prediction System
📌 Project Overview

This project is an end-to-end machine learning application that predicts the price of a laptop based on its hardware specifications and features.
It combines data preprocessing, feature engineering, model training, and an interactive web interface to deliver real-time price predictions.

A trained Random Forest Regression model is deployed using Streamlit, allowing users to input laptop configurations and instantly receive an estimated price.

🎯 Problem Statement

Laptop prices depend on multiple interrelated factors such as brand, processor, RAM, storage type, display characteristics, GPU, and operating system.
Manual price estimation is unreliable due to the non-linear relationships between these features.

Objective:
To build a robust regression model that accurately predicts laptop prices using historical data and deploy it as an interactive web application.

🧠 Methodology
1️⃣ Data Preprocessing & Cleaning

Removed irrelevant columns and duplicates

Converted categorical attributes (RAM, Weight, OS, CPU, GPU, etc.) into meaningful numerical representations

Extracted screen resolution into X_res, Y_res, and computed Pixels Per Inch (PPI)

Transformed price using log scaling to handle skewed distributions

2️⃣ Feature Engineering

Binary encoding for:

Touchscreen support

IPS display

Extracted:

CPU brand categories

GPU brand

Consolidated OS classes

Separated memory into HDD and SSD capacities

3️⃣ Model Development

Pipeline-based architecture using:

ColumnTransformer for categorical encoding

OneHotEncoder (drop-first strategy)

Regression Model:

Random Forest Regressor

Tuned hyperparameters for depth, features, and sampling

4️⃣ Model Evaluation

Metrics used:

R² Score

Mean Absolute Error (MAE)

Target variable trained on log(Price) for improved stability and accuracy

The trained pipeline and processed dataset were serialized using pickle for deployment 

ml_project_code

.

🌐 Web Application (Streamlit)

An interactive Streamlit UI allows users to:

Select laptop brand, CPU, GPU, OS

Choose RAM, SSD/HDD capacity

Adjust screen size, resolution, touchscreen, and IPS options

The app dynamically computes PPI and feeds the inputs into the trained pipeline to predict the final laptop price in real time 

App_code

.

📊 Results & Performance

The Random Forest model achieves strong predictive performance with:

High R² score

Low Mean Absolute Error

Log transformation of price significantly improves regression stability

Feature engineering (PPI, CPU/GPU categorization) plays a major role in accuracy

🧪 Technologies Used

Python

Pandas, NumPy

Scikit-learn

Matplotlib, Seaborn

Streamlit

Pickle

🚀 Future Improvements

Hyperparameter tuning using Grid Search / Bayesian Optimization

Model comparison with XGBoost / Gradient Boosting

Deployment using Docker or cloud platforms

Adding confidence intervals to predictions

Enhancing UI with visual explanations (feature importance)
