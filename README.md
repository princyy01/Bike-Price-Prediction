This repository contains a machine learning model to predict bike prices and a Flask web application to interact with the model through a web interface.
## Project Overview
The project aims to predict the price of used bikes based on features such as brand, kilometers driven, owner type, age, and power. 
The machine learning model is trained using linear regression, and the Flask web application allows users to input bike features and receive price predictions.

## Dataset
The dataset used for training the model includes the following columns:
- `bike_name`: The name of the bike
- `price`: The selling price of the bike
- `city`: The city where the bike is being sold
- `kms_driven`: The number of kilometers driven by the bike
- `owner`: The type of owner (e.g., First Owner, Second Owner)
- `age`: The age of the bike in years
- `power`: The power of the bike in cc
- `brand`: The brand of the bike

The dataset is preprocessed to remove duplicates and convert categorical variables to numerical values.

## Model Training
The model is trained using the following steps:
1. Load and preprocess the dataset
2. Convert categorical features to numerical values
3. Split the dataset into training and testing sets
4. Train a linear regression model
5. Evaluate the model using metrics such as mean squared error and R² score
6. Save the trained model using Joblib

## Web Application
The Flask web application provides an interface for users to input bike features and receive price predictions. 
