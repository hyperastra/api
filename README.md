# Hyperastra

Django REST Framework based backend API

## Requirements
- [Python 3.6+](https://www.python.org/)
- [Postgres 9.2+](https://www.postgresql.org/download/)
- [PIP](https://pypi.org/project/pip/)
- Virtualenvwrapper
    - [MacOS](https://virtualenvwrapper.readthedocs.io/en/latest/)
    - [Windows](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#windows-command-prompt)

## Installation
1. Create a folder for the Hyperastra project
2. Create a virtual environment (name should be hyperastra) on [MacOS](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation) or [Windows](https://pypi.org/project/virtualenvwrapper-win/)
3. Run the command `workon hyperastra` to activate the virtual environment
4. Clone this repository to a folder inside the project
5. Change directory to the cloned repository and run `pip install -r requirements.txt` to install application packages in the virtual environment.
6. Create a Postgres database called `hyperastra`.
7. Log into the database and run `CREATE EXTENSION IF NOT EXISTS citext;`
8. Duplicate the file `/config/settings/dev.template.py` to `dev.py`
9. Open `dev.template.py` and update the database credentials to for login to your local Postgres and rename to `dev.py`
10. On the command line move to the root directory of the repository and run `python manage.py migrate` to build the application database.

## CI / CD
The guide to setup CI / CD for a Django application for Google Cloud could be found following this [Link](https://cloud.google.com/python/django?hl=es-419)