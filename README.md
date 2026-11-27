# Interactive CV

My CV, built as a small data project. Instead of writing my experience, skills and education directly into a webpage, I stored them as tables in an Azure SQL database. Python reads the data and turns it into a website.

There are two versions:

- Static site: https://nevesdme.github.io/career-cv/
- Streamlit app: https://duarte-neves-cv.streamlit.app/

The static site is built ahead of time from the database, so it loads instantly. The Streamlit app reads the database live, so it can take a few seconds when the free database is waking up.

## How it works

The data lives in four tables on Azure SQL:

- `experience`: the companies and roles I worked in
- `projects`: projects linked to each job
- `education`: degrees and programmes
- `skills`: skills grouped by category

Shared:

- `database.py`: connects to Azure SQL and loads the tables

Static site:

- `build_site.py`: reads the tables, fills the HTML templates and writes the finished site to `docs/`
- `templates/`: the HTML templates and the stylesheet
- `docs/`: the generated site, served by GitHub Pages (don't edit it by hand, it gets overwritten)

Streamlit app:

- `app.py`: the main page (intro, database diagram, experience, skills and education)
- `components.py`: shared parts, like the header and the "Back to CV" button
- `pages/`: one page per project, with its own text and pictures

## Running it locally

```bash
pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml   # then fill in the password
```

Build the static site:

```bash
python build_site.py
```

Then open `docs/index.html` in a browser. After changing the data or the templates, build again and push.

Run the Streamlit app:

```bash
streamlit run app.py
```

Both connect to my own database with a read-only login, so they only work with the password for it.
