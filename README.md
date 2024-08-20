Final Year Project using AI to help predict the pitch location of Stephen Cluxton's championship kickouts based on past data.

1. Open CMD and navigate to folder of app
Eg. “C:\Users\deang\Documents\App”

2. Run the following commands:
python -m venv env

env\Scripts\activate

pip install flask pandas numpy tensorflow joblib scikit-learn

python app.py

Note: You can ignore warnings outputted

3. Navigate to “http://127.0.0.1:5000/” in your preferred browser
 
4. Input factors of the match. It is in the perspective of the team taking the
kickout (Trained on Dublin keeper Stephen Cluxton)

5. Click the “Predict!” button and the model will predict the outcome of the
kickout on the next page.
