"""Build the static CV website from the Azure SQL tables.

Run it with:  python build_site.py
The finished site is written to the docs/ folder.
"""

import shutil
import subprocess
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from database import load_table

TEMPLATES_DIR = Path("templates")
OUTPUT_DIR = Path("docs")

# Which project gets which page
PROJECT_PAGES = {
    "Analytical Database": "analytical_database.html",
    "Tableau Dashboards": "tableau_dashboards.html",
    "Digital Solutions": "techportal.html",
}

# Picture folders used by the project pages
IMAGE_FOLDERS = [
    "analytical_databases_pic",
    "tableau_dashboard_pics",
    "techportal_pic",
]


def get_data():
    # Extract: read the four tables from Azure SQL
    experience = load_table("experience")
    projects = load_table("projects")
    skills = load_table("skills")
    education = load_table("education")

    # Transform: put the data in the shape the template needs

    # Jobs, newest first, each with its own list of projects
    jobs = []
    for job in experience.sort_values("start_year", ascending=False).to_dict("records"):
        job_projects = projects[projects["experience_id"] == job["id"]].to_dict("records")
        for project in job_projects:
            project["page"] = PROJECT_PAGES.get(project["project"])
        job["projects"] = job_projects
        jobs.append(job)

    # Skills grouped by category, categories in alphabetical order
    skills_by_category = {
        category: list(group["skill"])
        for category, group in skills.groupby("category", sort=True)
    }

    # Degrees, newest first
    degrees = education.sort_values("end_year", ascending=False).to_dict("records")

    return {
        "experience": jobs,
        "skills": skills_by_category,
        "education": degrees,
    }


def build():
    data = get_data()

    # autoescape makes sure text from the database is shown as text, not as HTML
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=True)

    # Load: write the finished files to docs/
    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / "images").mkdir(exist_ok=True)

    html = env.get_template("index.html").render(**data)
    (OUTPUT_DIR / "index.html").write_text(html, encoding="utf-8")

    # Project pages: their text is in the templates, not in the database
    for page in PROJECT_PAGES.values():
        html = env.get_template(page).render()
        (OUTPUT_DIR / page).write_text(html, encoding="utf-8")

    # Draw the database diagram as an SVG image (needs Graphviz installed)
    subprocess.run(
        ["dot", "-Tsvg", TEMPLATES_DIR / "schema.dot", "-o", OUTPUT_DIR / "schema.svg"],
        check=True,
    )

    shutil.copy(TEMPLATES_DIR / "style.css", OUTPUT_DIR / "style.css")
    shutil.copy("extra_files/IMG_2520.jpg", OUTPUT_DIR / "images" / "IMG_2520.jpg")

    for folder in IMAGE_FOLDERS:
        shutil.copytree(
            Path("extra_files") / folder,
            OUTPUT_DIR / "images" / folder,
            dirs_exist_ok=True,
        )

    print(f"Site built in {OUTPUT_DIR}/")


if __name__ == "__main__":
    build()
