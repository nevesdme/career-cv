import streamlit as st
from components import project_header, project_footer

st.set_page_config(
    page_title="Tableau Dashboards",
    layout="wide"
)

project_header(
    "Tableau Dashboards",
    "VanWonen · Tableau · Business Intelligence"
)

IMAGES_DIR = "extra_files/tableau_dashboard_pics"

col_text, _ = st.columns([3, 1])

with col_text:
    st.write(
        "A closer look at the type of dashboards I built for VanWonen."
    )

    st.write(
        "Once the data was structured and stored in our analytical databases, "
        "the next step was to make it easy for people to use. Instead of going "
        "through hundreds of Excel files and documents for hours, employees "
        "could open a dashboard and compare projects, phases and numbers in "
        "seconds, and explore the data themselves."
    )

    st.write(
        "I never connected Tableau directly to the source platforms. Their data "
        "structures were made to run software, not for analysis. Every dashboard "
        "reads from the databases I prepared with Python, so the data is already "
        "shaped for what people need to see."
    )

    st.write(
        "The dashboards covered many different types of data: business cases "
        "from Reasult, budgets and real costs from Microsoft Business Central, "
        "acquisition leads from our GIS system, customer satisfaction from our "
        "CRM, and even how often people used the different tools in our "
        "TechPortal."
    )

    st.write(
        "In the end, all these dashboards were brought together in a data portal "
        "inside our TechPortal, where every employee could find the dashboards "
        "relevant to their work, in one place."
    )

    st.space("medium")

    for i in range(1, 6):
        st.image(f"{IMAGES_DIR}/Picture{i}.png", width=1050)
        st.space("medium")

project_footer()
