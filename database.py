
import time

import mssql_python
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, text
from sqlalchemy.exc import DBAPIError


def connection_string():
    # Read-only login, stored in .streamlit/secrets.toml locally
    # and in the app's secrets on Streamlit Cloud
    s = st.secrets["azure_sql"]
    password = s["password"].replace("}", "}}")

    return (
        f"Server=tcp:{s['server']},1433;"
        f"Database={s['database']};"
        f"Uid={s['username']};"
        f"Pwd={{{password}}};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
    )


def connect():
    # Give the database up to 60 seconds to log in (it may be waking up)
    login_timeout = mssql_python.constants.ConstantsDDBC.SQL_ATTR_LOGIN_TIMEOUT.value
    return mssql_python.connect(
        connection_string(),
        attrs_before={login_timeout: 60},
    )


@st.cache_resource
def get_engine():
    return create_engine(
        "mssql+mssqlpython://",
        creator=connect,
        pool_pre_ping=True,
    )


def load_table(table_name):
    allowed_tables = {"experience", "education", "skills", "projects"}

    if table_name not in allowed_tables:
        raise ValueError("Invalid table name")

    # The free database auto-pauses, so the first tries can fail
    # while it wakes up
    attempts = 3

    for attempt in range(1, attempts + 1):
        try:
            with get_engine().connect() as conn:
                return pd.read_sql_query(
                    text(f"SELECT * FROM {table_name}"),
                    conn
                )
        except DBAPIError:
            if attempt == attempts:
                raise
            time.sleep(10)
