from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Charger le modèle sauvegardé
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Route de prédiction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les données envoyées par le client
        data = request.get_json()
        df = pd.DataFrame([data])  # Convertir en DataFrame
        
        # Faire la prédiction
        prediction = model.predict(df)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)