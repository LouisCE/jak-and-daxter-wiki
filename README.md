# [jak-and-daxter-wiki](https://jak-and-daxter-wiki-420eda56706b.herokuapp.com)

Developer: Louis Cowell-English ([LouisCE](https://www.github.com/LouisCE))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/LouisCE/jak-and-daxter-wiki)](https://www.github.com/LouisCE/jak-and-daxter-wiki/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/LouisCE/jak-and-daxter-wiki)](https://www.github.com/LouisCE/jak-and-daxter-wiki/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/LouisCE/jak-and-daxter-wiki)](https://www.github.com/LouisCE/jak-and-daxter-wiki)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://jak-and-daxter-wiki-420eda56706b.herokuapp.com)

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a guest user | I want to see the weapons organised by eco colour | so I can easily find what I’m looking for. |
| As a guest user | I want an overview of each weapon with stats and description | so I can understand its use in-game. |
| As a guest user | I want to see images for weapons and characters | so I can associate information visually. |
| As a registered user | I want to sign up, log in, and log out | so that my account is secure and personalised. |
| As an admin user | I want CRUD functionality for weapons | so I can manage weapon-related content efficiently. |
| As an admin user | I want CRUD functionality for colours | so I can manage colour classifications efficiently. |
| As a registered user | I want to edit or delete my posts and comments | so I can manage my shared content. |
| As a registered user | I want my account and comments to be secure | so that no one else can impersonate me. |
| As a registered user | I want to leave posts or reviews | so I can share my experience and opinions about the games. |
| As a guest user | I want to view information about characters | so I can learn about the Jak and Daxter universe. |
| As a registered user | I want to comment under posts | so I can engage with other users. |
| As a guest user | I want a homepage that shows featured weapons and characters | so I can see important content at a glance. |
| As a guest user | I want to search for weapons, characters, or posts | so I can find content quickly. |
| As a guest user | I want to view collectibles like Precursor Orbs and Power Cells | so I can track optional in-game items. |
| As a guest user | I want to view information about enemies in the Jak and Daxter games | so I can learn about their behaviour, strengths, and weaknesses. |
| As a guest user | I want to view information about Jak’s Dark and Light forms | so I can understand how his abilities evolve in the story. |

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Used as a learning aid for debugging, explanations and planning. |

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found here:  
[Heroku Deployment – Jak and Daxter Wiki](https://jak-and-daxter-wiki-420eda56706b.herokuapp.com)

## Heroku Deployment

This project is deployed using **Heroku**, a cloud-based Platform as a Service (PaaS) used to run Django applications in production.

Below are the exact steps I followed to deploy the Jak and Daxter Wiki.

### Create a New Heroku App

1. Log into the Heroku Dashboard.
2. Click **New** → **Create new app**.
3. Choose a unique app name (in my case, `jak-and-daxter-wiki`).
4. Select the region closest to me (in my case, the EU as a UK user).
5. Click **Create App**.

### Config Vars

Inside my app, I went to the **Settings** tab and clicked **Reveal Config Vars** to enter the required environment variables used in my `env.py` file.

> [!IMPORTANT]  
> These values below are placeholders for demonstration only.  
> It is important to remember **not** use real keys here and **not** to commit actual keys into the repository.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | any-random-secret-key |

### Required Heroku Files

Heroku requires these supporting files in the project root to correctly build and run a Django application:

- `requirements.txt`
- `Procfile`
- `.python-version`

#### requirements.txt

I installed this project's **[requirements.txt](requirements.txt)** by using:

- `pip3 install -r requirements.txt`

When new packages were installed during development, the requirements file had to be updated using:

- `pip3 freeze --local > requirements.txt`

#### Procfile

I created the **[Procfile](Procfile)** with the following command:

- `echo web: gunicorn main.wsgi > Procfile`

### Python Version File

The **[.python-version](.python-version)** file tells Heroku the specific version of Python to use when running your application.

- In my case, the version is `3.12`

### Connecting GitHub to Heroku

For Heroku deployment, I followed these steps to connect my GitHub repository to the newly created app:

1. In the Heroku app dashboard, I went to the **Deploy** tab.
2. I chose **GitHub** as the deployment method.
3. I searched for my repository: `LouisCE/jak-and-daxter-wiki`.
4. I clicked **Enable Automatic Deploys**.

### Deployment Complete

Once the build was finished, my Jak and Daxter Django project was fully deployed, live and accessible at my Heroku domain.

### Cloudinary API

The Jak and Daxter Wiki uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

> [!IMPORTANT]  
> Again, the value shown below is only an example placeholder.  
> I never commit real API keys, secrets, or environment variables to my repository.  
> My actual Cloudinary key is stored securely in my local env.py (excluded via .gitignore) and in Heroku Config Vars.

To obtain my Cloudinary API key, I had to create an account and log in.

- For "Primary Interest", I chose **Programmable Media for image and video API**.
- On my Cloudinary Dashboard, I copied my **API Environment Variable**.
- The variable looks like this:

`CLOUDINARY_URL=cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5`

When adding to my local env.py and to Heroku Config Vars:

- I made sure to remove the leading `CLOUDINARY_URL=` as part of the API **value** as this is the **key**.
- The key and value went into my `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL` and the **value** which looks like `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5`

| Key | Value (example) |
| --- | --- |
| CLOUDINARY_URL | cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5 |

### PostgreSQL

This project uses a **Code Institute PostgreSQL Database** as the relational database for the Jak and Daxter Wiki, which is connected to Django via the `DATABASE_URL` environment variable.

> [!CAUTION]
> - PostgreSQL databases provided by Code Institute are only available to CI students.
> - Anyone cloning or forking this repository must obtain their own PostgreSQL database from another provider.
> - Code Institute students have a limit of 8 active databases.
> - Databases may be deleted automatically after 18 months.

To obtain my PostgreSQL Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link: <https://dbs.ci-dbs.net>
- I received an email containing my unique PostgreSQL database credentials.
- The database URL provided follows this format:
  - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- This URL was added to both:
  - my local `env.py` file as `DATABASE_URL`
  - and the Heroku **Config Vars** dashboard under the same key.

Once set, Django automatically used this PostgreSQL database for all models, migrations, and relational data within the project.

### WhiteNoise

This project uses **[WhiteNoise](https://whitenoise.readthedocs.io/en/latest/)** to handle static files on the live Heroku deployment for the Jak and Daxter Wiki. WhiteNoise allows Django to serve static files efficiently without requiring an external storage service for CSS, JavaScript, or other static assets.

To include WhiteNoise in this project, I followed these steps:

- Installed the WhiteNoise package:
  - `pip install whitenoise`

- Updated the `requirements.txt` file:
  - `pip freeze --local > requirements.txt`

- Added WhiteNoise to the `MIDDLEWARE` list inside `settings.py`, placed directly **under** Django’s `SecurityMiddleware`:

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # other middleware listed below
]
```

WhiteNoise works together with Heroku to efficiently serve static assets for the Jak and Daxter Wiki in production.

### Local Development

This project can be cloned or forked in order to create a local development copy of the **Jak and Daxter Wiki**.

After cloning or forking, you will need to install all required packages listed inside the [requirements.txt](requirements.txt) file:

- `pip3 install -r requirements.txt`

You will also need to create a new file named `env.py` in the project root directory.  
This file must contain the same environment variables used in your Heroku deployment setup.

> [!IMPORTANT]  
> The example values below are **demo placeholders only**.  
> **Do NOT** paste your real keys publicly.  
> When cloning or forking, replace these placeholders with your own secure environment variable values.

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary

# local environment only (do not include these in production!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, follow these steps to run it locally:

> [!NOTE]  
> Depending on your operating system, you may need to use either `python` or `python3` when running Django commands.  
> For example, `python manage.py runserver` (Windows) vs `python3 manage.py runserver` (macOS/Linux).  
> Use whichever command works on your system.

- Start the Django server:  
  `python3 manage.py runserver`

- Stop the server after confirming it loads:  
  `CTRL+C` (Windows/Linux) or `⌘+C` (Mac)

- Make migrations:  
  `python3 manage.py makemigrations --dry-run`  
  then  
  `python3 manage.py makemigrations`

- Apply migrations:  
  `python3 manage.py migrate --plan`  
  then  
  `python3 manage.py migrate`

- Create a superuser:  
  `python3 manage.py createsuperuser`

- Load fixtures (if using any):  
  `python3 manage.py loaddata file-name.json`  
  *(repeat for each fixture file)*

- Run the Django server again:  
  `python3 manage.py runserver`

If you'd like to back up data from specific models, you can create fixture files with:

- `python3 manage.py dumpdata your-model > your-model.json`
- *(repeat this for each model you want to back up)*

**NOTE:** Never include backups of default Django **admin** or **auth/user** tables, as they contain sensitive information.