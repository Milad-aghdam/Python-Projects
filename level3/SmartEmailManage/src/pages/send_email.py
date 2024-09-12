import streamlit as st
from utils.db import DatabaseManager
from utils.helper import send_email

st.set_page_config(page_title="Send Email", page_icon=":email:")

# Initialize the database manager
db_manager = DatabaseManager()

st.title("Send an Email")

# Retrieve profiles from the database
profiles = db_manager.get_profiles()
profile_options = {profile['name']: profile['email'] for profile in profiles}

if not profile_options:
    st.warning("No profiles found. Please add a profile first.")
else:
    # Input form to select recipient and email content
    with st.form(key="send_email_form"):
        recipient_name = st.selectbox("Select recipient", list(profile_options.keys()))
        subject = st.text_input("Subject")
        body = st.text_area("Email Body")
        send_button = st.form_submit_button(label="Send Email")

    if send_button:
        # Get the recipient's email address
        recipient_email = profile_options[recipient_name]
        
        # Send the email
        if send_email(to=recipient_email, subject=subject, contents=body):
            st.success(f"Email sent successfully to {recipient_name} ({recipient_email})")
        else:
            st.error("Failed to send email")
