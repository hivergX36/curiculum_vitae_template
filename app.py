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
    st.write("[linkedin](https://www.linkedin.com)")
    st.subheader("Languages")
    st.write("- French")
    st.write("- English (Advanced - C1)")


# --- CORPS PRINCIPAL ---
st.title("My  Curriculum Vitae")
st.write("My description")

st.markdown("---")


# Onglet Expériences

# Poste 1
st.markdown("### **Job** | Company")
st.caption("2024 - Présent |Company | City")
st.write("- Description")
st.write("Description")

st.markdown("---")

# Poste 2
st.markdown("### **Job** | Company")
st.caption("2022 - Présent |Company | City")
st.write("- Description")
st.write("Description")

st.subheader("Degrees")
st.markdown("#### **Master degree**")
st.write("University of XXXXX | 2020 - 2022")

st.markdown("#### **Bachelor Degree**")
st.write("Université of XXXXX | 2017 - 2020")

st.subheader("Skills")
st.write("**Programming:**")
st.write("**Libraries:**")
st.write("**Tools:**")

# Onglet Projets
st.subheader("My Projects")

# Projet
st.write("Project_1")

# Projet 2
st.write("Project_2")
