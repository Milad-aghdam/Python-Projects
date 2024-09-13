import streamlit as st
from utils.db import DatabaseManager

st.set_page_config(page_title="Email Templates", page_icon="")

db_manager = DatabaseManager()


def main():
    st.title("📝 Templates")
    st.header("Add new Templates")
    
    with st.form("Add new  Templates"):
        
        name_template = st.text_input("Template Name")
        body_template = st.text_area("Template Body")
     

        submit_button = st.form_submit_button("Add Template")
        if submit_button:
            
            if name_template and body_template:
            # Add the profile to the database
                template_id = db_manager.add_template(template_name=name_template, template_body=body_template)
                st.success(f"Profile '{name_template}' added successfully with ID {template_id}")
             
            else:
                st.error("Please fill out all required fields")

    st.header("Existing Templates")
    templates = db_manager.get_templates()

    if not templates:
        st.info("No templates found. Add a new template above.")
    else:
        for template in templates:
            with st.expander(f"Tamplate Name: {template['template_name']}"):
                
                st.write(f"**Tamplate Body**")
                st.text_area("", 
                                value=template['template_body'],
                                height=150, 
                                disabled=True,
                                key=f"Body:{template['template_body']}")
                
                # Add a delete button for each template
                if st.button("Delete", key=f"delete_{template.doc_id}"):
                    db_manager.templates_table.remove(doc_ids=[template.doc_id])
                    st.success(f"Profile {template['template_name']} deleted.")

if __name__ == "__main__":
    main()