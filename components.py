
import streamlit as st


def page_style():
    st.html("""
    <style>
    [data-testid="stElementToolbar"] {
        display: none;
    }
    button[data-testid="stBaseButton-primary"] {
        background-color: #555555;
        border-color: #555555;
        color: #F0F2F4;
    }
    button[data-testid="stBaseButton-primary"]:hover {
        background-color: #666666;
        border-color: #666666;
        color: #F0F2F4;
    }
    </style>
    """)


def back_button(key):
    if st.button("← Back to CV", type="primary", key=key):
        st.session_state["scroll_to_tabs"] = True
        st.switch_page("app.py")


def project_footer():
    st.divider()
    back_button("back_bottom")


def project_header(title, subtitle):
    page_style()
    back_button("back_top")

    st.title(title)
    st.caption(subtitle)
    st.divider()
