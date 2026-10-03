import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Mon CV Interactif", page_icon="📄", layout="wide")

# --- BARRE LATÉRALE (SIDEBAR) ---
with st.sidebar:
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
st.subheader("Professional experience")

    # Poste 1
    st.markdown("### **Développeur Python Senior** | Entreprise Tech")
    st.caption("📅 2024 - Présent | Paris")
    st.write(
        "- Développement et maintenance d'applications web avec Streamlit et FastAPI."
    )
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

# Onglet Formations et Compétences
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎓 Formations")
        st.markdown("#### **Master en Informatique / Data Science**")
        st.write("Université de Paris | 2020 - 2022")

        st.markdown("#### **Licence en Mathématiques et Informatique**")
        st.write("Université de Lyon | 2017 - 2020")

    with col2:
        st.subheader("🛠️ Compétences")
        st.write("**Langages :** Python, SQL, JavaScript")
        st.write("**Librairies :** Streamlit, Pandas, NumPy, Scikit-Learn")
        st.write("**Outils :** Git, Docker, PostgreSQL, AWS")

# Onglet Projets
with tab3:
    st.subheader("Projets Récents")

    # Projet 1
    with st.expander(
        "📊 Application de prédiction immobilière (Streamlit + Machine Learning)"
    ):
        st.write(
            "Développement d'une application web permettant d'estimer le prix d'un bien immobilier en fonction de sa surface et sa localisation."
        )
        st.write("[Voir le code sur GitHub](https://github.com)")

    # Projet 2
    with st.expander("🤖 Bot Discord d'automatisation"):
        st.write(
            "Création d'un bot Python connecté à une API météo pour envoyer des alertes quotidiennes automatisées."
        )
