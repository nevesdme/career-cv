import streamlit as st
from components import project_header

st.set_page_config(
    page_title="Analytical Database",
    layout="wide"
)

project_header(
    "Analytical Database",
    "VanWonen · Python · SQL · Data Integration"
)

IMAGES_DIR = "extra_files/analytical_databases_pic"

col_text, _ = st.columns([3, 1])

with col_text:
    st.write(
        "A closer look at the analytical database project I developed for VanWonen."
    )

    st.write(
        "The initial goal was to build a set of databases to store structured "
        "and standardized information about real estate development projects "
        "and their business cases. By organizing this information properly, "
        "we could connect it to dashboards and make it much easier to track "
        "project progress, compare different projects and business cases, and "
        "make better informed decisions without spending so much time gathering "
        "and processing information."
    )

    st.image(f"{IMAGES_DIR}/Picture2.png", width=1050)

    st.space("medium") 

    st.write(
        "Over time, we applied the same approach to other types of information, "
        "such as market research, potential acquisitions, customer and partner "
        "information, and more."
    )

    st.write(
        "But regardless of the type of data, I think the biggest challenge is "
        "always the same: figuring out how to structure it properly while "
        "keeping in mind what people actually need from it."
    )

    st.write(
        "For me, that's the most interesting part of this kind of work. It's not "
        "just about building databases or moving data around. It's about "
        "understanding how people work, what they're trying to achieve, and how "
        "we can make their jobs easier and more efficient, while ultimately "
        "helping the company make better decisions and achieve better business "
        "results."
    )

    st.image(f"{IMAGES_DIR}/Picture1.png", width=1050)

    st.space("medium")

    st.write(
        "To structure the data and make it useful for different purposes, I used "
        "Python to connect to various sources of information, including Microsoft "
        "applications, real estate software, APIs, customer information, public "
        "data and statistics, etc."
    )

    st.write(
        "I then used Python to clean, transform and organize the data according "
        "to what the end users needed, before loading it into SQL databases. From "
        "there, the data could be connected to visualization tools like Tableau, "
        "making it easier to explore, analyse and use in everyday decision making "
        "or analysis."
    )

    st.image(f"{IMAGES_DIR}/Picture3.png", width=1050)

    st.space("medium")

    st.image(f"{IMAGES_DIR}/Picture4.png", width=1050)