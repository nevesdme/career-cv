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

IMAGES_DIR = "extra_files/techportal_pic"

col_text, _ = st.columns([3, 1])

with col_text:
    st.write(
        "A closer look at the TechPortal and the digital tools we developed "
        "for VanWonen."
    )

    st.write(
        "The TechPortal was initially created to centralize all our data and "
        "tools in one place, so it would be easier for employees to find and "
        "use them. We used the normal Microsoft 365 login, so people only had "
        "to log in once, making it an even more seamless experience."
    )

    st.write(
        "In the TechPortal, employees could consult all the company dashboards, "
        "built on very different data sources, and use the tools they needed in "
        "their daily work, all in the same place. Tools like an enterprise "
        "closed AI agent, a GIS system used for acquisition leads, an AI "
        "knowledge sharer with information about how the company's projects are "
        "structured and how they work, an internal secure file transfer system, "
        "and a couple of other tools."
    )

    st.image(f"{IMAGES_DIR}/Picture1.png", width=1050)

    st.space("medium")

    st.write(
        "I also helped design and develop a new tool that allowed our financial "
        "controllers and project managers to follow how their projects were "
        "doing every quarter. It combined data from the different systems we "
        "used, like the ERP, the real estate software and the tool's own data. "
        "In the end, it was possible to see how each project was developing, "
        "the status of its financial data, the important dates of the project, "
        "and follow the direction the project was going, while comparing it "
        "with its different stages."
    )

    st.image(f"{IMAGES_DIR}/Picture2.png", width=1050)

    st.space("medium")

project_footer()
