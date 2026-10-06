import streamlit as st
from print_function import create_pdf, pdf_bytes

# Configuration de la page
st.set_page_config(page_title="My curriculum vitae")

# --- BARRE LATÉRALE (SIDEBAR) ---
# Optionnel : Ajouter une photo de profil (placez une image 'profile.png' dans le même dossier)
with st.sidebar:
    st.title("Name FirstName")
    st.write("Job: XXXXXX")
    st.write("City: XXXXXX")
    st.write("Mail: XXXXXX")
    st.write("[github](https://github.com)")
    st.write("[linkedin](https://www.linkedin.com/in/yourprofile)")
    st.subheader("Langues")
    st.write("- Français (Langue maternelle)")
    st.write("- Anglais (Avancé - C1)")


# --- CORPS PRINCIPAL ---
st.title("My  Curriculum Vitae")
st.write(
    "Passionné par le développement Python et la valorisation des données, je recherche de nouvelles opportunités."
)

st.markdown("---")


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


st.subheader("Degrees")
st.markdown("#### **Master en Informatique / Data Science**")
st.write("University of XXXXX | 2020 - 2022")

st.markdown("#### **Licence en Mathématiques et Informatique**")
st.write("Université of XXXXX | 2017 - 2020")

st.subheader("Skills")
st.write("**Programming:** Python, SQL, JavaScript")
st.write("**Libraries:** Streamlit, Pandas, NumPy, Scikit-Learn")
st.write("**Tools:** Git, Docker, PostgreSQL, AWS")

# Onglet Projets
st.subheader("Projets Récents")

# Projet
st.write("Projet_1")

# Projet 2
st.write("Project_2")
