import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import random

# Interface pour télécharger le fichier Excel
uploaded_file = st.file_uploader("Choisissez un fichier Excel", type="xlsx")

if uploaded_file is not None:
    # Lire le fichier Excel téléchargé
    df = pd.read_excel(uploaded_file)

    # Afficher les colonnes du DataFrame pour le diagnostic
    st.write("Colonnes du DataFrame :", df.columns)

    # Vérifier si les colonnes nécessaires existent
    required_columns = ['C', 'D', 'E']
    for col in required_columns:
        if col not in df.columns:
            st.error(f"La colonne '{col}' est manquante dans le fichier Excel.")
            break
    else:
        # Fonction pour insérer l'ancre et le lien dans le contenu HTML
        def inserer_ancre_lien(html_content, ancre, lien):
            soup = BeautifulSoup(html_content, 'html.parser')
            paragraphes = soup.find_all('p')

            if paragraphes:
                paragraphe_choisi = random.choice(paragraphes)
                ancre_lien = f'<a id="{ancre}" href="{lien}">{ancre}</a>'
                paragraphe_choisi.append(BeautifulSoup(ancre_lien, 'html.parser'))

            return str(soup)

        # Appliquer la fonction à chaque ligne du DataFrame
        df['F'] = df.apply(lambda row: inserer_ancre_lien(row['C'], row['D'], row['E']), axis=1)

        # Afficher le DataFrame modifié
        st.write(df)

        # Optionnel : Sauvegarder le DataFrame modifié dans un nouveau fichier Excel
        # df.to_excel('fichier_modifie.xlsx', index=False)
else:
    st.write("Veuillez télécharger un fichier Excel.")
