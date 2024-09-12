import streamlit as st

# Configure the page title and icon
st.set_page_config(page_title="Email Management System", page_icon="📧")
st.image('https://blog.tryshiftcdn.com/uploads/2021/03/email-management-1.png')
# Main title of the dashboard
st.title("📧 Email Management System")

# Dashboard Content
st.write("Here you'll see an overview of your recent email activities and key statistics.")

# Placeholder for recent emails section
st.subheader("Recent Emails")
st.table({
    "Recipient": ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown"],
    "Subject": ["Meeting Reminder", "Project Update", "Welcome Email", "Weekly Newsletter"],
    "Date": ["2024-09-10", "2024-09-09", "2024-09-08", "2024-09-07"]
})

# Placeholder for statistics section
st.subheader("Statistics")
col1, col2, col3 = st.columns(3)

# Displaying different metrics for emails sent, open rate, and response rate
col1.metric("Emails Sent", "50")
col2.metric("Open Rate", "75%")
col3.metric("Response Rate", "40%")
