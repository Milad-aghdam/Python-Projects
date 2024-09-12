import streamlit as st
from utils.db import DatabaseManager

st.set_page_config(page_title="Profiles", page_icon="")

db_manager = DatabaseManager()

def main():
    st.title("👥 Profiles")
    st.header("Add new profile")
    
    with st.form("Add new profile"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name")
            email = st.text_input("Email")
        with col2:
            title = st.text_input("Title")
            profession = st.text_input("Profession")

        submit_button = st.form_submit_button("Add Profile")
        if submit_button:
            if name and email and title and profession:
            # Add the profile to the database
                profile_id = db_manager.add_profile(name, email, title, profession)
                st.success(f"Profile '{name}' added successfully with ID {profile_id}")
             
            else:
                st.error("Please fill out all required fields")
    st.header("Existing Profiles")
    profiles = db_manager.get_profiles()

    if not profiles:
        st.info("No profiles found. Add a new profile above.")
    else:
        for profile in profiles:
            with st.expander(f"Name: {profile['name']}"):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**Email:** {profile['email']}")
                    st.markdown(f"**Title:** {profile['title']}")
                    st.markdown(f"**Profession:** {profile['profession']}")
                
                with col2:
                    # Add a delete button for each profile
                    if st.button("Delete", key=f"delete_{profile.doc_id}"):
                        db_manager.profiles_table.remove(doc_ids=[profile.doc_id])
                        st.success(f"Profile {profile['name']} deleted.")
                        # st.experimental_rerun()
main()