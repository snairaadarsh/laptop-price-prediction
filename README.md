# Laptop Price Prediction Using Machine Learning Regression

## Overview
This repository presents the implementation of an automated laptop price prediction
system using machine learning techniques. The proposed framework learns the relationship
between laptop hardware specifications and their corresponding market prices in a
supervised regression setting. The trained model is integrated with an interactive
web-based interface to provide real-time price estimation.

## Motivation
Estimating laptop prices accurately is a complex task due to the presence of multiple
interdependent factors such as brand, processor type, RAM, storage configuration,
display quality, graphics unit, and operating system. Manual estimation or rule-based
approaches are often inconsistent. This work explores a machine learning–based solution
to efficiently model non-linear relationships between features and price.

## Dataset
- Publicly available laptop specification dataset
- Includes features such as company, laptop type, RAM, weight, screen size,
  resolution, touchscreen support, IPS display, CPU brand, GPU brand, storage,
  and operating system
- Target variable is laptop price
- Price values are log-transformed to handle skewness and improve regression stability

## Methodology
1. Data cleaning and preprocessing
2. Feature engineering:
   - Extraction of screen resolution and computation of Pixels Per Inch (PPI)
   - Binary encoding of touchscreen and IPS display
   - Consolidation of CPU brands, GPU brands, and operating systems
   - Separation of HDD and SSD storage capacities
3. Categorical feature encoding using one-hot encoding
4. Regression model training using a pipeline-based approach
5. Model evaluation using regression performance metrics

## Model
- Regression Algorithm: Random Forest Regressor
- Preprocessing: ColumnTransformer with One-Hot Encoding
- Target Transformation: Logarithmic price scaling
- End-to-end pipeline used for both training and inference

## Results
- The trained model achieves strong predictive performance with:
  - High R² score
  - Low Mean Absolute Error (MAE)
- Log transformation improves model stability and prediction accuracy
- Features such as RAM, SSD capacity, CPU brand, and screen PPI significantly
  influence laptop price prediction

## Application
A Streamlit-based web application allows users to:
- Select laptop specifications such as brand, CPU, GPU, and operating system
- Configure RAM, storage, screen size, and resolution
- Enable or disable touchscreen and IPS display options
- Instantly obtain predicted laptop prices based on the trained model

## Technologies Used
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit
