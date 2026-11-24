import streamlit as st
from components import project_header, project_footer

st.set_page_config(
    page_title="TechPortal",
    layout="wide"
)

project_header(
    "TechPortal",
    "VanWonen · Digital Solutions"
)

st.write("Project details, screenshots and demos coming later.")

project_footer()
