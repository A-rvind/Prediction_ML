from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

app = Flask(__name__)

# Load the dataset
try:
    df = pd.read_csv('Housing_2025.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: Dataset file not found.")
    exit()

# Preprocess the data
# Features which are important

features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade','sqft_living15', 'sqft_lot15']
try:
    X = df[features]
    y = df['price']
except KeyError as e:
    print(f"Error: Column {e} not found in the dataset.")
    exit()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'house_price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    try:
        # Load the model
        model = joblib.load('house_price_model.pkl')

        # Get the input features from the form
        bedrooms = int(request.form.get('bedrooms',0))
        bathrooms = float(request.form.get('bathrooms',0))
        sqft_living = int(request.form.get('sqft_living',0))
        sqft_lot = int(request.form.get('sqft_lot',0))
        floors = int(request.form.get('floors',0))
        waterfront = int(request.form.get('waterfront',0))
        view = int(request.form.get('view',0))
        condition = int(request.form.get('condition',0))
        grade = int(request.form.get('grade',0))
        sqft_living15 = int(request.form.get('sqft_living15',0))
        sqft_lot15 = int(request.form.get('sqft_lot15',0))

        # Create a DataFrame with the input features
        input_features = pd.DataFrame([[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, sqft_living15, sqft_lot15]],
                                    columns=features)

        # Predict the house price
        predicted_price = model.predict(input_features)[0]

        return render_template('index.html', prediction_text=f'Predicted House Price: ${predicted_price:,.2f}')
    except KeyError as e:
        return f"Error: Missing form field - {e}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
if __name__ == '__main__':
    app.run(debug=False) # change to True if needed 