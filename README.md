# Interactive CV

My CV, built as a small data project. Instead of writing my experience, skills and education directly into a webpage, I stored them as tables in an Azure SQL database. Python reads the data and Streamlit turns it into a website.

Live version: https://duarte-neves-cv.streamlit.app/

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

```bash
pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml   # then fill in the password
streamlit run app.py
```

The app connects to my own database with a read-only login, so it only works with the password for it.
