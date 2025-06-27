
import streamlit as st
import sys
import os
import json

# Ajouter le chemin parent pour accéder à main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pipotron.core import my_function, generate_random_phrase


st.title(" Pipotron Checker")

p_size = st.number_input("Nombre de composants", min_value=2, value=3)
list_possibilities = {}

# Pas d'espace avant ponctuation
default_dict = {
    1: 'Je|Tu|Demain je',
    2: 'mange|bois|vole|voles',
    3: '.|!|?|…'
}

# Fichier JSON ou TXT uploadé
uploaded_file = st.file_uploader(" Charger un dictionnaire (.json ou .txt)", type=["json", "txt"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith('.json'):
            data = json.load(uploaded_file)
        elif uploaded_file.name.endswith('.txt'):
            content = uploaded_file.read().decode("utf-8")
            data = json.loads(content)
        else:
            data = {}
        list_possibilities = {int(k): v for k, v in data.items()}
        st.success(" Dictionnaire chargé avec succès.")
        p_size = len(list_possibilities)
    except Exception as e:
        st.error(f"Erreur de chargement du fichier : {e}")

# Construction des champs dynamiques si pas de fichier
if not uploaded_file:
    for i in range(1, p_size + 1):
        default = default_dict.get(i, "")
        comps = st.text_input(
            f"Composants possibles pour la position {i} (séparés par |)",
            value=default,
            key=f"comp_{i}"
        )
        list_possibilities[i] = [x.strip() for x in comps.split('|') if x.strip()]

sentence = st.text_input("Phrase à vérifier")

st.caption(" Astuce : les signes de ponctuation ne doivent pas être précédés d’espace sauf ('!', '?', ':', ';', '»','«', '(', '[', '{', '«', '»')")
st.caption(" Ce projet ne vérifie pas la validité grammaticale des phrases, uniquement leur conformité à une structure donnée (pipotron).")

case_sensitive = st.checkbox("Respecter la casse (case sensitive)", value=True)

if st.button("Vérifier"):
    result = my_function(p_size, list_possibilities, sentence, case_sensitive)
    if result is True:
        st.success(" Phrase valide (pipotron)")
    else:
        st.error(result)

if st.button(" Générer une phrase aléatoire"):
    generated = generate_random_phrase(p_size, list_possibilities)
    st.info(f" Phrase générée : {generated}")
