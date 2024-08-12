import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import random

# Titre de l'application
st.title("Modifier le contenu HTML dans un fichier Excel")

# Interface pour télécharger le fichier Excel
uploaded_file = st.file_uploader("Choisissez un fichier Excel", type="xlsx")

if uploaded_file is not None:
    # Lire le fichier Excel téléchargé
    df = pd.read_excel(uploaded_file)

    # Afficher les colonnes du DataFrame pour le diagnostic
    st.write("Colonnes du DataFrame :", df.columns)

    # Sélection des colonnes par l'utilisateur
    st.write("Sélectionnez les colonnes à utiliser :")
    col_html = st.selectbox("Colonne contenant le HTML de l'article", df.columns)
    col_ancre = st.selectbox("Colonne contenant l'ancre", df.columns)
    col_lien = st.selectbox("Colonne contenant le lien", df.columns)

    # Bouton pour lancer le script
    if st.button("Lancer le script"):
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
        df['G'] = df.apply(lambda row: inserer_ancre_lien(row[col_html], row[col_ancre], row[col_lien]), axis=1)

        # Afficher le DataFrame modifié
        st.write(df)

        # Sauvegarder le DataFrame modifié dans un nouveau fichier Excel avec une meilleure mise en page
        output_file = 'fichier_modifie.xlsx'
        with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
            workbook = writer.book
            worksheet = writer.sheets['Sheet1']

            # Ajuster la largeur des colonnes pour une meilleure lisibilité
            for col_num, col_name in enumerate(df.columns):
                max_length = max(df[col_name].astype(str).map(len).max(), len(col_name))
                worksheet.set_column(col_num, col_num, max_length + 2)

            # Formater le contenu HTML pour une meilleure lisibilité
            for row_num, row in enumerate(df['G']):
                worksheet.write(row_num + 1, df.columns.get_loc('G'), row)

        st.success(f"Le fichier a été modifié et sauvegardé sous le nom : {output_file}")
        st.download_button(
            label="Télécharger le fichier modifié",
            data=open(output_file, 'rb'),
            file_name=output_file,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
else:
    st.write("Veuillez télécharger un fichier Excel.")
