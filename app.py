import streamlit as st
from print_function import create_pdf, pdf_bytes

# Configuration de la page
st.set_page_config(page_title="My curriculum vitae", page_icon="📄", layout="wide")

# --- BARRE LATÉRALE (SIDEBAR) ---
# Optionnel : Ajouter une photo de profil (placez une image 'profile.png' dans le même dossier)
# st.image("profile.png", width=150)

st.title("Name FirstName")
st.write("Job")
st.write("City")
st.write("Mail")

st.markdown("---")
st.subheader("Langues")
st.write("- Français (Langue maternelle)")
st.write("- Anglais (Avancé - C1)")

# --- CORPS PRINCIPAL ---
st.title("My  Curriculum Vitae")
st.write(
    "Passionné par le développement Python et la valorisation des données, je recherche de nouvelles opportunités."
)


# Onglet Expériences

# Poste 1
st.markdown("### **Développeur Python Senior** | Entreprise Tech")
st.caption("2024 - Présent | Paris")
st.write("- Développement et maintenance d'applications web avec Streamlit et FastAPI.")
st.write(
    "- Automatisation de pipelines de données (ETL) permettant de gagner 5h par semaine."
)

st.markdown("---")

# Poste 2
st.markdown("### **Data Analyst Junior** | Agence Data")
st.caption("📅 2022 - 2024 | Lyon")
st.write(
    "- Création de tableaux de bord interactifs (PowerBI / Streamlit) pour le suivi des KPI."
)
st.write(
    "- Analyse des comportements d'achat pour optimiser les campagnes marketing (+12% de conversion)."
)


st.subheader("🎓 Formations")
st.markdown("#### **Master en Informatique / Data Science**")
st.write("University of XXXXX | 2020 - 2022")

st.markdown("#### **Licence en Mathématiques et Informatique**")
st.write("Université de Lyon | 2017 - 2020")

st.subheader("🛠️ Compétences")
st.write("**Langages :** Python, SQL, JavaScript")
st.write("**Librairies :** Streamlit, Pandas, NumPy, Scikit-Learn")
st.write("**Outils :** Git, Docker, PostgreSQL, AWS")

# Onglet Projets
st.subheader("Projets Récents")

# Projet
st.write(
    "Développement d'une application web permettant d'estimer le prix d'un bien immobilier en fonction de sa surface et sa localisation."
)
st.write("[Voir le code sur GitHub](https://github.com)")

# Projet 2
st.write(
    "Création d'un bot Python connecté à une API météo pour envoyer des alertes quotidiennes automatisées."
)

with open("cv.pdf", "file_bytes") as f:
    pdf_data = f.read()

# Create the download button
st.download_button(
    label="Download CV as PDF",
    data=pdf_data,
    file_name="my_cv.pdf",
    mime="application/pdf",
)
