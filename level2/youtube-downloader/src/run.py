import streamlit as st



st.set_page_config(page_title="YTD ", page_icon="🚀", layout="wide", )     
st.markdown(f"""
            <style>
            .stApp {{background-image: url("https://images.unsplash.com/photo-1516557070061-c3d1653fa646?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80"); 
                     background-attachment: fixed;
                     background-size: cover}}
         </style>
         """, unsafe_allow_html=True)


st.title("YouTube Downloader 🚀")
rl = st.text_input("Paste URL here 👇", placeholder='https://www.youtube.com/')
st.subheader("Video Details ⚙️")
button = st.button("Download ⚡️", type="primary")

