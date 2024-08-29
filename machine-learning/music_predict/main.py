from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the model pipeline
model_pipeline = joblib.load('music_genre_model.joblib')

@app.route('/predict' , methods=['POST'])
def predict():
    data = request.json
    age = data['age']
    gender = data['gender']

    # Prepare the data for prediction
    input_data = pd.DataFrame({
        'age': [age],
        'gender': [gender]
    })

    # Make prediction using the pipeline
    pred = model_pipeline.predict( input_data )[0]

    return jsonify( {'predicted_genre': pred } )


app.run(debug=True)