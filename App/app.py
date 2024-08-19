from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from keras.models import load_model
import joblib  

app = Flask(__name__)

# Load the model and the preprocessor with joblib
model = load_model('model.h5')
preprocessor = joblib.load('preprocessor.pkl')
encoder = joblib.load('encoder.pkl')

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # Extract the input data from the form
        data = {
            'Score_diff': request.form.get('Score_diff', type=int),
            'Score_diff_change': request.form.get('Score_diff_change', type=int),  
            'LastPlay': request.form.get('LastPlay'),
            'Press': request.form.get('Press'),
            'MatchQuarter': request.form.get('MatchQuarter')
        }
        # Convert input data to DataFrame
        input_df = pd.DataFrame([data])
        # Process the new input using the same preprocessor used on the training data
        input_processed = preprocessor.transform(input_df)
        # Make predictions
        predictions = model.predict(input_processed)

        # Transform predictions to right format
        predictions_percentages = pd.DataFrame(predictions, columns=encoder.get_feature_names_out()).iloc[0] * 100
        predictions_formatted = predictions_percentages.round(2).astype(str) + '%'
        
        # Remove the 'x0_' 
        predictions_formatted.index = predictions_formatted.index.str.replace('x0_', '')

        # Display the results
        return render_template("results.html", result=predictions_formatted.to_dict())
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
