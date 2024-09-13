import streamlit as st
from utils.db import DatabaseManager
import streamlit as st

# Initialize the database manager
db_manager = DatabaseManager()

def main():
    st.title("👤 User Profile")

    # Fetch existing profile data
    user_profile = db_manager.get_user_profile()

    # Prepopulate form with user profile data if available
    if user_profile:
        name = user_profile.get("name", "")
        title = user_profile.get("title", "")
        profession = user_profile.get("profession", "")
        degree = user_profile.get("degree", "")
        university = user_profile.get("university", "")
        social_media = user_profile.get("social_media", {})
        signature = user_profile.get("signature", "")
    else:
        name = title = profession = degree = university = signature = ""
        social_media = {"linkedin": "", "X": "", "github": "", "personal_website": ""}

    # Form for user profile input
    with st.form("user_profile_form"):
        col1, col2, col3= st.columns(3)
        with col1:
            title = st.text_input("Title", title)
            degree = st.text_input("Degree", degree)

        with col2:
            name = st.text_input("Name", name)
            university = st.text_input("University", university)
        with col3:
            profession = st.text_input("Profession", profession)


        st.subheader("Social Media")
        col1, col2 = st.columns(2)
        with col1:
            linkedin = st.text_input("LinkedIn", social_media.get("linkedin", ""))
            X = st.text_input("X (Twitter)", social_media.get("X", ""))
        with col2:
            github = st.text_input("GitHub", social_media.get("github", ""))
            personal_website = st.text_input("Personal Website", social_media.get("personal_website", ""))

        signature = st.text_area("Email Signature", signature)

        submit_button = st.form_submit_button("Save Profile")

    # Handle form submission
    if submit_button:
        social_media = {
            "linkedin": linkedin,
            "X": X,
            "github": github,
            "personal_website": personal_website
        }

        # If a profile exists, update it; otherwise, add a new profile
        if user_profile:
            db_manager.update_user_profile(name, title, profession, degree, university, social_media, signature)
            st.success("Profile updated successfully!")
        else:
            db_manager.add_user_profile(name, title, profession, degree, university, social_media, signature)
            st.success("Profile added successfully!")

if __name__ == '__main__':
    main()

