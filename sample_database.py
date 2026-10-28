import pandas as pd


def load_table(table_name):
    data = {
        "experience": [
            {
                "id": 1,
                "company": "Example Energy",
                "role": "Engineering Intern",
                "start_year": 2013,
                "end_year": 2013,
            },
            {
                "id": 2,
                "company": "Example Manufacturing",
                "role": "Production Planning",
                "start_year": 2018,
                "end_year": 2021,
            },
            {
                "id": 3,
                "company": "Example Company",
                "role": "Data Engineer",
                "start_year": 2022,
                "end_year": 2026,
            },
        ],
        "education": [
            {
                "id": 1,
                "institution": "Example University",
                "programme": "Engineering",
                "start_year": 2008,
                "end_year": 2013,
            },
        ],
        "skills": [
            {"id": 1, "skill": "Python", "category": "Programming"},
            {"id": 2, "skill": "SQL", "category": "Programming"},
            {"id": 3, "skill": "Tableau", "category": "Visualisation"},
        ],
        "projects": [
            {
                "id": 1,
                "experience_id": 3,
                "project": "Analytical Database",
                "description": "Built a database and ETL pipelines.",
            },
            {
                "id": 2,
                "experience_id": 3,
                "project": "Tableau Dashboards",
                "description": "Created analytical dashboards.",
            },
            {
                "id": 3,
                "experience_id": 3,
                "project": "Digital Solutions",
                "description": "Developed internal digital tools.",
            },
        ],
    }

    if table_name not in data:
        raise ValueError("Invalid table name")

    return pd.DataFrame(data[table_name])