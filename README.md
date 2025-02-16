**House Price Prediction using Flask and Machine Learning**

<ins>Project Overview</ins>

This project is a **Flask-based web application** that predicts house prices based on user input features such as the number of bedrooms, bathrooms, square footage, location factors, and more. The prediction is train simple model algorithm by a **Linear Regression model** trained on a housing dataset.

<ins>Technologies Used</ins>

- **Python** (Flask, Pandas, Scikit-learn, Joblib)
- **HTML, CSS, JavaScript** (Frontend for UI)
- **Machine Learning** (Linear Regression)
- **Jupyter and VsCode**

<ins>Setup & Installation</ins>

1. Install Dependencies

   Make sure you have installed – Python on your machine.

   To install required libraries and Framework:

   pip install flask pandas scikit-learn joblib

1. Run the Flask Application

   Run in Terminal : Python app.py

   You don’t need html file to run separate, Flask will handle  

1. Open in Browser

   After the successfully running,

   Open <http://127.0.0.1:5000/> in your web browser

   Default port is 5000 of flask

<ins>Working</ins>

1. User enters house details in the web form.
1. App processes the input and sends it to the trained model.
1. The Linear Regression model predicts the house price.
1. The predicted price is displayed on the webpage.

Note: 

Static folder for CSS, templates folder for html are the default directories used in Flask, Flask automatically looks for files in these directories when serving your web application.

<ins>Images:</ins>

<ins>Sample</ins>

Input: 

|Feature|Value|
| :- | :- |
|Bedrooms|3|
|Bathrooms|2|
|Sqft Living|1800|
|Sqft Lot|4000|
|Floors|1|
|Waterfront|0|
|View|2|
|Condition|3|
|Grade|7|
|Sqft Living nearby|2000|
|Sqft Lot nearby|5000|

output:

Predicted House Price: $533,834.28

<ins>Future Goal</ins>

1. Add interactive Visualization
1. Adding more dataset for training model for accuracy
1. Deployment
