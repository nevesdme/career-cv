
import streamlit as st


def project_header(title, subtitle):
    if st.button("← Back to CV"):
        st.switch_page("app.py")

    st.title(title)
    st.caption(subtitle)
    st.divider()
