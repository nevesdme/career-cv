import streamlit as st
from database import load_table

@st.cache_data(ttl=600)
def get_cv_data(table_name):
    return load_table(table_name)

st.set_page_config(
    page_title="Interactive CV",
    page_icon="💼",
    layout="wide"
)


st.html("""
<div style="padding: 65px 0 45px 0;">
    <p style="color: #8BB8E8; font-size: 13px; letter-spacing: 3px; margin-bottom: 20px;">
        DATA ENGINEERING / ANALYTICS / DIGITAL SOLUTIONS
    </p>

    <h1 style="font-size: clamp(32px, 4vw, 48px); font-weight: 600; letter-spacing: -2px; line-height: 1.1; margin-bottom: 24px;">
        Turning data into<br>
        practical solutions<span style="color: #8BB8E8;">.</span>
    </h1>

    <p style="color: #AAB7C4; font-size: 18px; line-height: 1.8; max-width: 650px;">
        Engineering background. Business perspective.
        Building data platforms, analytics and digital tools
        that solve real-world problems.
    </p>
</div>
""")

st.divider()

st.markdown("**A CV with a backend.**")
st.caption(
    "Instead of putting my experience, skills and education "
    "directly into a webpage, I turned them into SQL tables "
    "hosted on Azure. Python pulls the data, and Streamlit "
    "puts it all together. Most likely unnecessary but, what the hell."
)

st.graphviz_chart("""
digraph {
    graph [bgcolor="transparent", rankdir="LR"]
    node [shape="record", style="rounded,filled",
          fillcolor="#192530", color="#526579",
          fontcolor="#F0F2F4", fontname="Helvetica"]
    edge [color="#8BB8E8"]

    experience [
        label="{experience|id (PK)\\lcompany\\lrole\\lstart_year\\lend_year\\l}"
    ]

    projects [
        label="{projects|id (PK)\\lexperience_id (FK)\\lproject\\ldescription\\l}"
    ]

    education [
        label="{education|id (PK)\\linstitution\\lprogramme\\lstart_year\\lend_year\\l}"
    ]

    skills [
        label="{skills|id (PK)\\lskill\\lcategory\\l}"
    ]

    experience -> projects [label="1 to many", fontcolor="#8BB8E8"]
}
""")


# Load data from Azure SQL
experience = get_cv_data("experience")
projects = get_cv_data("projects")
skills = get_cv_data("skills")
education = get_cv_data("education")

# Load professional experience

tab1, tab2, tab3, tab4 = st.tabs([
    "💼 Experience & Projects",
    "🛠️ Skills",
    "🎓 Education",
    "About me"
])

with tab1:
    st.header("Professional Experience")

    for _, job in experience.sort_values(
        "start_year", ascending=False
    ).iterrows():
        with st.container(border=True):
            st.markdown(f"### {job['role']}")
            st.markdown(f"**{job['company']}**")
            st.caption(f"{job['start_year']} — {job['end_year']}")

            job_projects = projects[
                projects["experience_id"] == job["id"]
            ]

            if not job_projects.empty:
                st.divider()

                for _, project in job_projects.iterrows():
                    st.markdown(f"**↗ {project['project']}**")
                    st.caption(project["description"])
                    project_pages = {
                        "Analytical Database": "pages/analytical_database.py",
                        "Tableau Dashboards": "pages/tableau_dashboards.py",
                        "Digital Solutions": "pages/techportal.py",
                    }

                    page = project_pages.get(project["project"])

                    if page:
                        if st.button("View project →", key=f"project_{project['id']}"):
                            st.switch_page(page)

# Load skills table
with tab2:
    st.header("Skills")

    for category, group in skills.groupby("category", sort=True):
        st.subheader(category)
        st.write(" · ".join(group["skill"]))

# Load education table
with tab3:
    st.header("Education")

    for _, degree in education.sort_values(
        "end_year", ascending=False
    ).iterrows():
        with st.container(border=True):
            st.subheader(degree["institution"])
            st.write(f"**{degree['programme']}**")
            st.caption(
                f"{degree['start_year']} – {degree['end_year']}"
            )

# Load About me section
with tab4:
    st.header("About me")

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.subheader("Engineer by background. Data engineer by choice.")

        st.write(
            "I started in industrial management and production planning "
            "before moving into data engineering. These days I work with "
            "Python, SQL, analytics and digital tools — usually somewhere "
            "between the technical and business sides of a problem."
        )

    with col2:
        st.image("extra_files/IMG_2520.jpg", width=220)