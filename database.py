
import struct
import pandas as pd
from azure.identity import AzureCliCredential
from sqlalchemy import create_engine, event, text


def get_engine():
    connection_url = (
        "mssql+pyodbc://@cvadmin.database.windows.net/"
        "free-sql-db-4505384"
        "?driver=ODBC+Driver+18+for+SQL+Server"
        "&Encrypt=yes"
        "&TrustServerCertificate=no"
    )

    engine = create_engine(connection_url)

    @event.listens_for(engine, "do_connect")
    def add_azure_token(dialect, conn_rec, cargs, cparams):
        cargs[0] = cargs[0].replace(";Trusted_Connection=Yes", "")

        credential = AzureCliCredential()
        token = credential.get_token(
            "https://database.windows.net/.default"
        ).token

        token_bytes = token.encode("utf-16-le")
        token_struct = struct.pack("<I", len(token_bytes)) + token_bytes

        cparams["attrs_before"] = {1256: token_struct}

    return engine


def load_table(table_name):
    allowed_tables = {"experience", "education", "skills", "projects"}

    if table_name not in allowed_tables:
        raise ValueError("Invalid table name")

    engine = get_engine()

    with engine.connect() as conn:
        df = pd.read_sql_query(
            text(f"SELECT * FROM {table_name}"),
            conn
        )

    engine.dispose()
    return df
