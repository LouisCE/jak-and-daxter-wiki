# [jak-and-daxter-wiki](https://jak-and-daxter-wiki-420eda56706b.herokuapp.com)

Developer: Louis Cowell-English ([LouisCE](https://www.github.com/LouisCE))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/LouisCE/jak-and-daxter-wiki)](https://www.github.com/LouisCE/jak-and-daxter-wiki/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/LouisCE/jak-and-daxter-wiki)](https://www.github.com/LouisCE/jak-and-daxter-wiki/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/LouisCE/jak-and-daxter-wiki)](https://www.github.com/LouisCE/jak-and-daxter-wiki)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://jak-and-daxter-wiki-420eda56706b.herokuapp.com)

## Project Overview

The **Jak and Daxter Wiki** is a fan-driven knowledge base dedicated to celebrating and documenting one of the most iconic action-adventure franchises in PlayStation history. The goal of this project is to provide a clean, structured, and interactive platform where users can explore detailed information about characters, eco colours, weapon mods, collectibles, and other lore-rich elements from the Jak and Daxter universe. Because the series spans multiple games with a wide range of features, this wiki aims to consolidate this information in a way that is accessible, visually thematic, and easy to navigate for both new fans and long-time enthusiasts.

This project is designed for **gamers, franchise fans, lore hunters, and nostalgic players** who want a central space to visit the world of Jak and Daxter. The platform includes authenticated features that allow authorised users to participate in improving and growing the content by creating, updating and deleting characters, eco types, weapon mods, collectibles and other in-universe elements. By blending fan passion with structured database functionality, the wiki demonstrates how Django can be used to build community-focused, data-rich web platforms.

**Why this project?**  
I chose this theme because Jak and Daxter has been my favourite video game series of all time since childhood. Its captivating world, memorable characters, unique weapon systems, satisfying collectible hunting, and rich lore made a lasting impression on me. Building a project around a universe that I already know intimately meant that I could focus my time on the technical aspects of web development rather than researching the subject matter. My familiarity with the games helped me decide which apps to create, how to structure the data, and how to present the content in a polished and accessible format that fans would appreciate.

Developing this wiki allowed me to combine personal enthusiasm with the technical challenge of creating a fully functional Django application, complete with authentication, CRUD (create, read, update, delete) functionality, responsive design, and visually thematic styling. Creating a project that I am passionate about helped maintain motivation throughout development and ensured that the final result feels meaningful, cohesive, and engaging. This concept also aligns perfectly with the Full Stack Toolkit (PP4) learning outcomes, allowing me to showcase my growing full-stack development skills.

The Jak and Daxter Wiki not only serves as a tribute to the franchise but also fulfills the core learning outcomes of the module by demonstrating robust backend logic, user interaction, form handling, data modelling, and front-end presentation. It is a project driven equally by technical ambition and long-standing personal passion.

At the time of writing, there are six games in the Jak and Daxter franchise. However, to prevent overengineering, I have decided that this project will be focusing primarily on the core trilogy:

- Jak and Daxter: The Precursor Legacy (2001)
- Jak II (2003)
- Jak 3 (2004)

![screenshot](documentation/mockup.png)

[jak-and-daxter-wiki amiresponsive](https://ui.dev/amiresponsive?url=https://jak-and-daxter-wiki-420eda56706b.herokuapp.com)

---

## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**

- Provide fans of the **Jak and Daxter series** with a clear, visually themed, and community-focused wiki.
- Allow authenticated users to contribute and manage structured content such as **characters, eco colours, weapon mods, and collectables**.
- Present information in a way that is easy to browse for newcomers while still being detailed enough for long-time fans.

**Primary User Needs**

- **Guests**  
  - Browse character pages, eco colours, weapon wods and collectables.  
  - Understand game features through images and structured descriptions.
  - Navigate the site easily without needing to register.

- **Registered users**  
  - Create, edit, or delete their own contributions where permitted.
  - Interact with authenticated-only features.

- **Admins / Superusers**  
  - Maintain accuracy and consistency across all wiki entries.
  - Perform full CRUD operations across all models.
  - Moderate user-generated content to ensure quality and relevance.

**Project Goals**

- Build a fan-friendly, visually thematic wiki styled after the Jak universe.
- Encourage community contributions while maintaining structured, reliable information.
- Maintain a respectful, well-moderated knowledge base for the franchise.
- Deliver a responsive and accessible experience across mobile devices, tablet and desktop.

---

#### 2. Scope

**Planned Features**  
(see [Features](#features) section)

- A responsive home page with overview, hero banner and an image for each of the core three Jak and Daxter games.
- Character pages with stats and descriptions.
- Morph Gun pages with eco colour classifications with custom borders and visual themes and weapon mod information.
- A Collectables page displaying items such as Power Cells and Precursor Orbs.
- User registration, login, and logout.
- Role-based authorisation for full CRUD management.
- Navigation to all major areas of the site.
- Footer with link to GitHub.
- Custom error handling (400, 403, 404, 429 and 500 pages).

**Content Requirements**

- Images for characters, eco colours, weapon mods and collectables.
- Structured descriptions including origins, lore, gameplay purpose, and appearances.
- Authenticated forms for adding and editing and deleting content.
- Error feedback for user actions (e.g., login errors, validation errors).  
- Custom 400, 403, 404, 429 and 500 pages.

---

#### 3. Structure

**Information Architecture**

- **Navigation Bar**
  - Home
  - Characters
  - Morph Gun
  - Collectables
  - Login / Register
  - Logout (visible only to authenticated users)

- **Front Page Structure**
  - Hero banner featuring the Jak II promo art.
  - Intro describing the Jak and Daxter Wiki.
  - Cards linking to Characters, Weapons, and Eco Colours.

  - **Home Page Structure**
  - Hero section introducing the Jak and Daxter Wiki and its purpose.
  - Brief overview of the three core Jak and Daxter games with corresponding art.

- **Data Structure**
  - Character model
  - Colour model
  - Weapon model
  - Collectable model
  - User authentication handled via Django’s built-in auth system

**User Flow**

1. **Guest browsing**  
   - User lands on Home page and sees the wiki overview.
   - User clicks to browse the Characters page with sixteen character options (will be expanded on in the future).
   - User can click on specific characters to see their information (e.g. Jak, Daxter, Samos, Keira).
   - User clicks to Morph Gun page with eco type overview (e.g. Red, Yellow, Blue, Dark).
   - User clicks to view the individual weapon mod pages (e.g. Scatter Gun, Blaster Mod, Vulcan Fury, Peace Maker).
   - User clicks to the Collectables page to see specific in-game items (Power Cells, Precursor Orbs, Scout Flies, Skull Gems).

2. **Registration Path**  
   - Guest selects Register → completes registration → logs in.

3. **Authenticated User Actions**
   - Edits or deletes their own entries where permitted (if desired and allowed).
   - Gains access to authenticated-only navigation options.
   - Option to logout.

4. **Admin User Actions**  
   - Full CRUD access across all models.  
   - Moderation and management of community-submitted content.

---

#### 4. Skeleton

**[Wireframes](#wireframes)**

Wireframes were created during the planning stage to define layout, navigation, and content hierarchy for all key pages.

(See the [Wireframes](#wireframes) section for mobile, tablet, and desktop designs.)

---

#### 5. Surface

**Visual Design Elements**

The visual theme of the site is inspired by the **dark gunmetal / eco-charged look** of the Jak and Daxter games.

The design focuses on:

- High-contrast orange text against a near-black world for user accessibility.
- Heavy, bold titles styled in the *Black Ops One* font for a shooter game vibe.
- Borders and badges in eco-inspired colours (red, yellow, blue, purple).

You can see these implemented throughout the CSS file.

(See the **[Colour Scheme](#colour-scheme)** and **[Typography](#typography)** sections below for more information.)

---

### Colour Scheme

I generated the following custom colour palette specifically to reflect a **Jak II inspired atmosphere**, with dark dystopian sci-fi tones while using eco colours as visual highlights.

- `#1a1a1a` - Primary dark background
- `#ff9f1c` - Main Jak-orange text (titles, headers)
- `#ffd166` - Hover highlights
- `dc3545` - Red eco theme
- `ffc107` - Yellow eco theme
- `0d6efd` - Blue eco theme
- `#6f42c1` - Purple eco theme
- `#0d0d0d` - Secondary dark (navbar + footer)

I used [coolors.co](https://coolors.co/1a1a1a-ff9f1c-ffd166-dc3545-ffc107-0d6efd-6f42c1-0d0d0d) to generate my color palette.

![screenshot](documentation/coolors.png)

---


---

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

#### Cloning

You can clone this repository by following these steps:

1. Go to the **Jak and Daxter Wiki** GitHub repository:  
   https://www.github.com/LouisCE/jak-and-daxter-wiki
2. Click the green **Code** button at the top of the page.
3. Choose whether you want to clone using **HTTPS**, **SSH**, or **GitHub CLI**, then click the **copy** icon to copy the URL.
4. Open **Git Bash**, **Terminal**, or your preferred command-line tool.
5. Navigate to the directory where you want the project to be saved.
6. Run the following command to clone the repository:

    ```bash
    git clone https://www.github.com/LouisCE/jak-and-daxter-wiki.git
    ```

7. Press **Enter** and the repository will be cloned into a new folder on your machine.

Alternatively, if you're using **Ona (formerly Gitpod)**, you can launch a cloud development workspace directly from your browser using the button below:

[![Open in Ona-Gitpod](https://ona.com/run-in-ona.svg)](https://gitpod.io/#https://www.github.com/LouisCE/jak-and-daxter-wiki)

> [!NOTE]  
> To use Ona/Gitpod with one click, you must have the browser extension installed.  
> Instructions can be found here: https://www.gitpod.io/docs/configure/user-settings/browser-extension

#### Forking

By forking the GitHub repository, you create a copy of the original project on your own GitHub account. This allows you to view and edit the project freely without affecting the original repository. You can fork this repository by following these steps:

1. Log in to GitHub and navigate to the **Jak and Daxter Wiki** repository:  
   https://www.github.com/LouisCE/jak-and-daxter-wiki
2. At the top-right of the repository page, just below the “Settings” tab, click the **Fork** button.
3. After clicking Fork, GitHub will create a copy of the repository under your own account. You can now work on your fork independently!

### Local vs. Deployment

There are no remaining major differences between the local version of the Jak and Daxter Wiki and the deployed version online. Both environments function the same, with identical features, structure, and behaviour.