import pandas as pd
from bs4 import BeautifulSoup
import random

# Charger le fichier Excel
df = pd.read_excel('ton_fichier.xlsx')

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

# Sauvegarder le DataFrame modifié dans un nouveau fichier Excel
df.to_excel('fichier_modifie.xlsx', index=False)
