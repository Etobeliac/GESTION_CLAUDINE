import streamlit as st
import pandas as pd
import random

# Fonction pour générer une ancre aléatoire
def generer_ancre():
    ancres = [
    "Cliquez ici pour découvrir les détails.",
    "Pour plus d'infos, suivez ce lien.",
    "En savoir plus en cliquant ici.",
    "Accédez à plus d'informations en suivant ce lien.",
    "Cliquez ici pour en apprendre davantage.",
    "Pour découvrir plus, cliquez ici.",
    "Explorez ce sujet en cliquant ici.",
    "Cliquez ici pour en savoir plus.",
    "Pour plus de détails, suivez ce lien.",
    "En savoir plus sur ce sujet en cliquant ici.",
    "Cliquez ici pour explorer ce sujet en détail.",
    "Pour plus d'informations, visitez ce lien.",
    "Découvrez tout ce qu'il faut savoir en suivant ce lien.",
    "Cliquez ici pour accéder à plus de détails.",
    "Pour explorer davantage, cliquez ici.",
    "Cliquez ici pour obtenir des informations supplémentaires.",
    "Pour en savoir plus, suivez ce lien.",
    "Découvrez-en davantage en cliquant ici.",
    "Cliquez ici pour plus d'informations.",
    "Pour des détails supplémentaires, cliquez ici.",
    "Accédez à plus de contenu en suivant ce lien.",
    "Cliquez ici pour découvrir ce sujet.",
    "Pour explorer en profondeur, cliquez ici.",
    "En savoir plus sur ce sujet en cliquant ici.",
    "Cliquez ici pour accéder à toutes les informations.",
    "Pour plus de renseignements, cliquez ici.",
    "Découvrez tous les détails en cliquant ici.",
    "Cliquez ici pour explorer davantage ce sujet.",
    "Pour obtenir plus d'infos, cliquez ici.",
    "En apprendre plus en suivant ce lien.",
    "Cliquez ici pour découvrir plus d'informations.",
    "Pour en savoir plus, suivez ce lien.",
    "Accédez à plus de détails en cliquant ici.",
    "Cliquez ici pour en savoir plus sur ce sujet.",
    "Pour plus d'infos, cliquez ici.",
    "Découvrez toutes les informations en suivant ce lien.",
    "Cliquez ici pour explorer ce sujet en profondeur.",
    "Pour tout savoir sur ce sujet, cliquez ici.",
    "En savoir plus en cliquant ici.",
    "Cliquez ici pour obtenir plus de détails.",
    "Pour des informations supplémentaires, suivez ce lien.",
    "Découvrez-en davantage en suivant ce lien.",
    "Cliquez ici pour en savoir plus.",
    "Pour explorer ce sujet, cliquez ici.",
    "Accédez à plus d'informations en cliquant ici.",
    "Cliquez ici pour découvrir tous les détails.",
    "Pour plus de détails, suivez ce lien.",
    "En savoir plus sur ce sujet en cliquant ici.",
    "Cliquez ici pour explorer davantage.",
    "Pour plus d'informations, cliquez ici.",
    "Découvrez tous les détails en suivant ce lien.",
    "Cliquez ici pour accéder à plus de contenu.",
    "Pour en savoir plus, suivez ce lien.",
    "Explorez ce sujet en cliquant ici.",
    "Cliquez ici pour découvrir plus d'informations.",
    "Pour des détails supplémentaires, cliquez ici.",
    "En apprendre davantage en suivant ce lien.",
    "Cliquez ici pour tout savoir sur ce sujet.",
    "Pour plus de renseignements, suivez ce lien.",
    "Découvrez toutes les informations nécessaires en cliquant ici.",
    "Cliquez ici pour explorer ce sujet en détail.",
    "Pour accéder à plus d'infos, cliquez ici.",
    "En savoir plus sur ce sujet en suivant ce lien.",
    "Cliquez ici pour obtenir toutes les informations.",
    "Pour en apprendre plus, cliquez ici.",
    "Découvrez-en plus en suivant ce lien.",
    "Cliquez ici pour explorer davantage ce sujet.",
    "Pour plus d'informations, visitez ce lien.",
    "En savoir plus sur ce sujet en cliquant ici.",
    "Cliquez ici pour découvrir ce sujet en profondeur.",
    "Pour des détails supplémentaires, suivez ce lien.",
    "Explorez toutes les options en cliquant ici.",
    "Cliquez ici pour obtenir des informations supplémentaires.",
    "Pour plus de détails, cliquez ici.",
    "En savoir plus sur ce sujet en suivant ce lien.",
    "Cliquez ici pour accéder à plus de contenu.",
    "Pour découvrir plus, cliquez ici.",
    "Explorez ce sujet en suivant ce lien.",
    "Cliquez ici pour plus d'informations.",
    "Pour plus de détails, suivez ce lien.",
    "En savoir plus sur ce sujet en cliquant ici.",
    "Cliquez ici pour en apprendre davantage.",
    "Pour plus d'informations, cliquez ici.",
    "Découvrez tout ce qu'il faut savoir en cliquant ici.",
    "Cliquez ici pour explorer ce sujet en profondeur.",
    "Pour obtenir plus d'infos, cliquez ici.",
    "En savoir plus en suivant ce lien.",
    "Cliquez ici pour découvrir tous les détails.",
    "Pour explorer davantage, cliquez ici.",
    "Découvrez-en davantage en cliquant ici.",
    "Cliquez ici pour obtenir plus d'informations.",
    "Pour des renseignements supplémentaires, suivez ce lien.",
    "Explorez ce sujet en détail en cliquant ici.",
    "Cliquez ici pour découvrir plus d'informations.",
    "Pour en savoir plus, suivez ce lien.",
    "En apprendre plus en cliquant ici.",
    "Cliquez ici pour tout savoir sur ce sujet.",
    "Pour explorer davantage, cliquez ici.",
    "Découvrez toutes les informations en cliquant ici.",
    "Cliquez ici pour accéder à plus de détails.",
    "En savoir plus sur ce sujet en cliquant ici.",
    "Découvrez davantage d'informations en suivant ce lien.",
    "Pour en savoir plus, visitez cette page.",
    "Cliquez ici pour explorer ce sujet en profondeur.",
    "Apprenez-en plus en accédant à cette page.",
    "Pour plus d'informations, cliquez ici.",
    "Explorez toutes les options en suivant ce lien.",
    "Visitez cette page pour en savoir plus.",
    "Obtenez plus de détails en cliquant ici.",
    "Découvrez tout ce qu'il faut savoir en cliquant ici.",
    "Pour plus de détails, cliquez ici.",
    "En savoir plus en visitant cette page.",
    "Cliquez ici pour découvrir plus d'informations.",
    "Pour en apprendre davantage, suivez ce lien.",
    "Découvrez toutes les informations nécessaires en cliquant ici.",
    "Pour explorer ce sujet, cliquez ici.",
    "Accédez à plus de détails en suivant ce lien.",
    "Cliquez ici pour obtenir des informations supplémentaires.",
    "En savoir plus sur ce sujet en visitant cette page.",
    "Pour plus d'infos, cliquez ici.",
    "Découvrez les détails complets en cliquant ici.",
    "Visitez ce lien pour plus d'informations.",
    "Pour en savoir plus sur ce sujet, cliquez ici.",
    "Cliquez ici pour plus de renseignements.",
    "Découvrez-en davantage en suivant ce lien.",
    "Pour des détails supplémentaires, cliquez ici.",
    "En apprendre plus sur ce sujet en cliquant ici.",
    "Pour tout savoir sur ce sujet, cliquez ici.",
    "Cliquez ici pour accéder à plus de contenu.",
    "Pour explorer davantage ce sujet, cliquez ici.",
    "Découvrez plus d'informations en suivant ce lien.",
    "Accédez à toutes les infos en cliquant ici.",
    "Pour plus de détails, suivez ce lien.",
    "Cliquez ici pour tout savoir sur ce sujet.",
    "En savoir plus en cliquant ici.",
    "Découvrez les informations complètes en cliquant ici.",
    "Cliquez ici pour obtenir des détails supplémentaires.",
    "Pour plus d'informations, visitez cette page.",
    "Accédez à plus d'infos en suivant ce lien.",
    "Cliquez ici pour découvrir ce sujet en profondeur.",
    "En apprendre davantage en suivant ce lien.",
    "Pour des détails supplémentaires, visitez cette page.",
    "Cliquez ici pour explorer davantage ce sujet.",
    "Pour en savoir plus, suivez ce lien.",
    "Découvrez tout ce qu'il faut savoir en suivant ce lien.",
    "Cliquez ici pour accéder à plus de détails.",
    "En savoir plus en cliquant sur ce lien.",
    "Pour plus d'informations, cliquez ici.",
    "Accédez à toutes les informations en cliquant ici.",
    "Pour découvrir plus de contenu, cliquez ici.",
    "Cliquez ici pour tout savoir sur ce sujet.",
    "En savoir plus en suivant ce lien.",
    "Découvrez toutes les informations nécessaires ici.",
    "Pour explorer ce sujet en profondeur, cliquez ici.",
    "Cliquez ici pour plus de détails.",
    "Accédez à plus d'informations en cliquant ici.",
    "Pour en savoir plus, visitez cette page.",
    "Cliquez ici pour découvrir ce sujet.",
    "Découvrez-en davantage en cliquant ici.",
    "Pour plus de renseignements, cliquez ici.",
    "En savoir plus en visitant cette page.",
    "Cliquez ici pour obtenir plus de détails.",
    "Pour tout savoir, cliquez ici.",
    "Découvrez tout ce qu'il faut savoir en suivant ce lien.",
    "Pour des informations supplémentaires, cliquez ici.",
    "Cliquez ici pour explorer ce sujet en détail.",
    "En apprendre plus en cliquant ici.",
    "Pour plus d'infos, suivez ce lien.",
    "Accédez à plus de détails en cliquant ici.",
    "Cliquez ici pour en savoir plus sur ce sujet.",
    "Pour des renseignements supplémentaires, cliquez ici.",
    "Découvrez plus de détails en cliquant ici.",
    "Cliquez ici pour obtenir toutes les informations.",
    "En savoir plus en suivant ce lien.",
    "Pour explorer ce sujet, cliquez ici.",
    "Accédez à plus de contenu en cliquant ici.",
    "Cliquez ici pour plus d'informations.",
    "Pour découvrir tout ce qu'il faut savoir, cliquez ici.",
    "Cliquez ici pour accéder à toutes les infos.",
    "Pour des détails supplémentaires, suivez ce lien.",
    "En apprendre davantage en cliquant ici.",
    "Pour en savoir plus, cliquez ici.",
    "Cliquez ici pour découvrir plus d'infos.",
    "Pour explorer ce sujet en profondeur, suivez ce lien.",
    "Accédez à toutes les informations nécessaires en cliquant ici.",
    "Pour plus de détails, visitez cette page.",
    "Cliquez ici pour obtenir plus d'infos.",
    "Découvrez toutes les informations en suivant ce lien.",
    "Pour explorer ce sujet, cliquez ici.",
    "Cliquez ici pour découvrir ce sujet en détail.",
    "En savoir plus sur ce sujet en cliquant ici.",
    "Pour tout savoir sur ce sujet, suivez ce lien.",
    "Accédez à plus de détails en cliquant ici.",
    "Cliquez ici pour explorer davantage ce sujet.",
    "Pour découvrir plus de contenu, cliquez ici.",
    "En savoir plus en visitant cette page.",
    "Cliquez ici pour accéder à plus d'informations.",
    "Pour explorer ce sujet, cliquez ici.",
    "Découvrez toutes les informations en cliquant ici.",
    "Pour plus de renseignements, cliquez ici."
]

# Fonction pour générer une ancre aléatoire
def generer_ancre():
    ancres = [
        # Ajoutez vos ancres ici
    ]
    return random.choice(ancres)

# Fonction pour tronquer le lien jusqu'au TLD
def tronquer_lien(lien):
    return '/'.join(lien.split('/')[:3])

# Charger les fichiers Excel
uploaded_file = st.file_uploader("Choisissez votre fichier Excel", type="xlsx")

if uploaded_file is not None:
    # Lire les feuilles Excel et vérifier leur présence
    xls = pd.ExcelFile(uploaded_file)
    sheet_names = xls.sheet_names

    if 'SITE A LINKER' not in sheet_names:
        st.error("La feuille 'SITE A LINKER' n'existe pas dans le fichier Excel.")
    else:
        # Lire la feuille 'SITE A LINKER'
        df_site_a_linker = pd.read_excel(uploaded_file, sheet_name='SITE A LINKER')

        # Vérifier si les colonnes nécessaires existent
        required_columns = ['Nombre de lien', 'Lien', 'Thématique']
        missing_columns = [col for col in required_columns if col not in df_site_a_linker.columns]
        if missing_columns:
            st.error(f"Les colonnes suivantes sont manquantes dans la feuille 'SITE A LINKER': {', '.join(missing_columns)}")
        else:
            # Vérifier si la feuille 'ARTICLE LINKER' existe, sinon la créer
            if 'ARTICLE LINKER' not in sheet_names:
                df_article_linker = pd.DataFrame(columns=['Lien', 'Ancre', 'Thématique', 'Lien Base'])
            else:
                df_article_linker = pd.read_excel(uploaded_file, sheet_name='ARTICLE LINKER')

            # Créer les nouvelles lignes dans la feuille 'ARTICLE LINKER'
            nouvelles_lignes = []
            for index, row in df_site_a_linker.iterrows():
                nombre_de_liens = row['Nombre de lien']
                lien = row['Lien']
                thematique = row['Thématique']
                lien_tronque = tronquer_lien(lien)

                for _ in range(nombre_de_liens):
                    nouvelles_lignes.append({
                        'Lien': lien,
                        'Ancre': generer_ancre(),
                        'Thématique': thematique,
                        'Lien Base': lien_tronque
                    })

            # Ajouter les nouvelles lignes au DataFrame 'ARTICLE LINKER'
            df_nouvelles_lignes = pd.DataFrame(nouvelles_lignes)
            df_article_linker = pd.concat([df_article_linker, df_nouvelles_lignes], ignore_index=True)

            # Afficher le DataFrame mis à jour
            st.write("Feuille 'ARTICLE LINKER' mise à jour :")
            st.dataframe(df_article_linker)

            # Sauvegarder le fichier Excel mis à jour
            with pd.ExcelWriter('output.xlsx') as writer:
                df_site_a_linker.to_excel(writer, sheet_name='SITE A LINKER', index=False)
                df_article_linker.to_excel(writer, sheet_name='ARTICLE LINKER', index=False)

            st.download_button(
                label="Télécharger le fichier Excel mis à jour",
                data=open('output.xlsx', 'rb'),
                file_name='output.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
