import streamlit as st
import requests

# URL de l'API Flask
API_URL = "http://127.0.0.1:5000/predict"

st.title("Application de Prédiction du Prix Moyen d'un Avocat avec Flask et Streamlit")

# Saisie des données par l'utilisateur
st.write("**Entrez les valeurs pour chaque caractéristique :**")
total_volume = st.number_input("Volume Total", min_value=0.0, step=0.1)
small_bags = st.number_input("Petits Sacs", min_value=0.0, step=0.1)
large_bags = st.number_input("Grands Sacs", min_value=0.0, step=0.1)
xlarge_bags = st.number_input("Très Grands Sacs", min_value=0.0, step=0.1)
quality1 = st.number_input("Qualité 1", min_value=0.0, step=0.1)
quality2 = st.number_input("Qualité 2", min_value=0.0, step=0.1)
quality3 = st.number_input("Qualité 3", min_value=0.0, step=0.1)
type_ = st.selectbox("Type d'Avocat", ["conventionnel", "organique"])
year = st.number_input("Année", min_value=2000, step=1)
region = st.text_input("Région")

# Bouton de prédiction
if st.button("Prédire"):
    input_data = {
        "Total Volume": total_volume if total_volume else 0,
        "Small Bags": small_bags if small_bags else 0,
        "Large Bags": large_bags if large_bags else 0,
        "XLarge Bags": xlarge_bags if xlarge_bags else 0,
        "Quality1": quality1 if quality1 else 0,
        "Quality2": quality2 if quality2 else 0,
        "Quality3": quality3 if quality3 else 0,
        "type": type_,
        "year": year,
        "region": region
    }
    try:
        # Envoi des données à l'API Flask
        response = requests.post(API_URL, json=input_data)
        prediction = response.json()
        
        # Affichage de la prédiction
        if "prediction" in prediction:
            st.success(f"Prix Moyen Prédit : {prediction['prediction'][0]} $")
        else:
            st.error(f"Erreur : {prediction['error']}")
    except Exception as e:
        st.error(f"Erreur lors de la requête : {e}")