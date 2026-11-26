# Interactive CV

My CV, built as a small data project. Instead of writing my experience, skills and education directly into a webpage, I stored them as tables in an Azure SQL database. Python reads the data and Streamlit turns it into a website.

Live version: coming soon.

## How it works

The data lives in four tables on Azure SQL:

- `experience`: the companies and roles I worked in
- `projects`: projects linked to each job
- `education`: degrees and programmes
- `skills`: skills grouped by category

The code:

- `app.py`: the main page (intro, database diagram, experience, skills and education)
- `database.py`: connects to Azure SQL and loads the tables
- `components.py`: shared parts, like the header and the "Back to CV" button
- `pages/`: one page per project, with its own text and pictures

## Running it locally

You need Python, the Microsoft ODBC Driver 18 for SQL Server and the Azure CLI.

```bash
pip install -r requirements.txt
az login
streamlit run app.py
```

The app connects to my own database, so it only works with an account that has access to it.
