import streamlit as st
from utils.db import DatabaseManager

st.set_page_config(page_title="Profiles", page_icon="👥")

db_manager = DatabaseManager()

st.title("Profiles")

profiles = db_manager.get_profiles()

if not profiles:
    st.write("No profiles available.")
else:
    for profile in profiles:
        st.write(f"**Name**: {profile['name']} | **Email**: {profile['email']} | **Title**: {profile['title']} | **Profession**: {profile['profession']}")
