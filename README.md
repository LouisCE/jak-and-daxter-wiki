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

[AmiResponsive preview](https://ui.dev/amiresponsive?url=https://jak-and-daxter-wiki-420eda56706b.herokuapp.com)

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
  - Browse character pages, eco colours, weapon mods and collectables.  
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
- `#ffffff` - Default white
- `#ff9f1c` - Main Jak-orange text (titles, headers)
- `#ffd166` - Hover highlights
- `#ff0000` - "Red" eco theme
- `#ffff00` - "Yellow" eco theme
- `#00ffff` - "Blue" eco theme (represented by cyan for greater contrast)
- `#ff00ff` - "Dark" eco theme (respresented by magenta for greater contrast)
- `#0d0d0d` - Secondary dark (navbar + footer)

Blue (#0000ff) and purple (#800080) were originally used for the "Blue" and "Dark" styling on the weapon list and weapon detail pages but after WAVE testing and visual assessment, I decided to switch them to cyan and magenta for better accessibility.

I also switched to brighter shades of red and yellow for the same reason and ultimately decided to implement a colour picker into the CRUD functionality to give admin users the freedom to create and update colours as they see fit.

I used [Coolors](https://coolors.co/1a1a1a-ff9f1c-ffd166-ff0000-ffff00-00ffff-ff00ff-ffffff) to generate my color palette.

![screenshot](documentation/coolors.png)

I also used [EightShapes Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23000000%2C%0D%0A%23FF9F1C%2C%0D%0A%23FFD166%2C%0D%0A%23FF0000%2C%0D%0A%23FFFF00%2C%0D%0A%2300FFFF%2C%0D%0A%23FF00FF%2C%0D%0A%23FFFFFF%2C&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp) to generate my contrast grid.

As shown in the top row, all colours used are rated AAA or AA against the dark background by WCAG (Web Content Accessibility Guidelines).

![screenshot](documentation/contrast-grid.png)

---

### Typography

The site uses Google Fonts for one strong, thematic header font and a clean default body font. Typography choices were kept minimal to maintain readability while reinforcing the game’s tone.

- **[Black Ops One](https://fonts.google.com/specimen/Black+Ops+One)**
  Used for all headings (`h1`-`h6`), navigation branding, and major emphasis text.
  This font was chosen because it resembles stencil/military sci-fi lettering, matching Jak II’s dystopian industrial cyberpunk aesthetic.

- **Arial / Sans-Serif (Bootstrap default)**
  Used for general body text to ensure clarity across devices.

- **Icons**  
  No external icon libraries are used within the project.

Font import used in the project:

```css
@import url('https://fonts.googleapis.com/css2?family=Black+Ops+One&display=swap');
```

---

## Wireframes

Rather than producing wireframes at the very start of the project, early development prioritised back-end functionality to ensure that core features, data relationships, and user interactions functioned correctly as intended. This approach allowed the underlying logic, models, and workflows to be fully established before committing to detailed visual layouts.

Once the project had matured and the primary functionality was in place, focus shifted toward front-end design. At this stage, wireframes were created for mobile, tablet, and desktop screen sizes to support UI refinement. These wireframes were used to polish layout consistency, improve navigation flow, and ensure content hierarchy translated effectively across different devices.

Wireframes were designed using [Balsamiq](https://balsamiq.com/wireframes), with a focus on clarity, responsiveness, and usability for both guest users and registered users.

![screenshot](documentation/wireframes/mobile-wireframes.png)
![screenshot](documentation/wireframes/tablet-wireframes.png)
![screenshot](documentation/wireframes/desktop-wireframes.png)

During the later stages of development, the wireframes acted as a visual reference to guide front-end improvements. While some layouts evolved during implementation, the final interface closely reflects the structure and intent established in the wireframes.

---

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a guest user | I want a homepage that gives an overview of the three core Jak and Daxter games. | so I can see important content at a glance. |
| As a guest user | I want to view information about characters | so I can learn about the inhabitants of the Jak and Daxter universe. |
| As a guest user | I want to see the morph gun weapon mods organised by eco colour | so I can easily find the ones I’m looking for. |
| As a guest user | I want an overview of each weapon mod with descriptions and upgrading availability. | so I can understand its use in-game. |
| As a guest user | I want to view collectibles like Precursor Orbs and Power Cells | so I can track optional in-game items. |
| As a guest user | I want to see images across all website apps. | so I can associate information visually. |
| As a registered user | I want to sign up, log in, and log out | so that my account is secure and personalised. |
| As a registered user | I want to rate the twelve morph gun mods out of ten. | so I can share my opinion on which weapons are most effective and contribute to the community ratings. |
| As a registered user | I want the community rankings to show a change indicator. | so that I can see how my votes affected the average. |
| As a registered user | I want my account and weapon ratings to be secure | so that no one else can impersonate me and alter the ratings that I have given. |
| As an admin user | I want CRUD functionality across all website apps. | so I can manage content efficiently. |
| As an admin user | I want to be able to select a colour when creating new eco types and weapon mods | so that I can ensure that the styling is consistent with the content. |

User stories were refined during development to accurately reflect the final scope and implemented functionality of the project.

---

## Features

### Existing Features

The **Jak and Daxter Wiki** is designed to provide fans of the franchise with a structured, visual, and easy-to-navigate reference site.  
Features were implemented iteratively and refined during development to align with the final project scope and user needs.

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Hero Section | A themed hero image, title, and introductory text establish the tone and purpose of the site on first visit. | ![screenshot](documentation/features/home-hero.png) |
| Homepage Overview | The homepage provides an overview of the three core Jak and Daxter games, introducing users to the series and guiding them toward key content areas. | ![screenshot](documentation/features/game-intros.png) |
| Character Index | Users can browse a list of characters from the Jak and Daxter universe, presented in a clean and readable layout. | ![screenshot](documentation/features/character-grid.png) |
| Character Detail Pages | Each character has a dedicated page displaying descriptive information and imagery to support exploration of the game world. | ![screenshot](documentation/features/character-detail.png) |
| Morph Gun Overview | Introduces the Morph Gun system and explains how weapon mods are organised by eco colour across the games. | ![screenshot](documentation/features/morphgun-overview.png) |
| Eco Colour Grouping | Morph Gun weapon mods are grouped by eco colour, allowing users to easily locate and compare related weapons. | ![screenshot](documentation/features/eco-groups.png) |
| Weapon Mod Cards | Individual weapon mod cards display images, names, and visual styling to support quick recognition. | ![screenshot](documentation/features/weapon-cards.png) |
| Weapon Mod Detail Pages | Each Morph Gun weapon mod has a dedicated detail page containing descriptions and upgrade availability information. | ![screenshot](documentation/features/weapon-detail.png) ![screenshot](documentation/features/weapon-upgrades.png) |
| Admin Eco Colour Picker | Admin users can customise the eco styling used across **Weapon List** and **Weapon Detail** pages via a colour picker for eco types. The picker supports **HEX**, **RGB**, and **HSL** input so admins can work in whichever colour format they are most comfortable with. Selected colours are applied consistently to headings, borders, and weapon card styling to preserve the eco-themed UI across the Morph Gun section. | ![screenshot](documentation/features/colour-picker.png) |
| Weapon Rating System | Registered users can rate each of the twelve Morph Gun weapon mods out of ten, contributing to overall community ratings. | ![screenshot](documentation/features/rate-weapons.png) |
| Rating Submit Loader (Eco Beachball) | When a user submits their weapon ratings, JavaScript disables the **Save Ratings** button and changes the label to **"Saving..."** to prevent duplicate submissions. A Jak and Daxter themed **spinning beachball loader** appears alongside the message **"Updating Averages..."**. The spinner uses the **four primary eco colours** to match the Morph Gun theme and provides clear feedback that the update is in progress. | ![screenshot](documentation/features/eco-loader.png) |
| Weapon Rankings Page | Registered users can view a page that displays their weapon rankings and the community rankings. This page also lets users see how their votes affected the average. | ![screenshot](documentation/features/user-rankings.png) |
| Community Rankings & Change Indicators | The Community Rankings table includes a position-change system that shows how the user’s latest ratings affected the community order. A green **▲** indicates a weapon has been **promoted**, a red **▼** indicates a weapon has been **demoted**, and the number beside the icon shows **how many positions** the weapon moved. This makes ranking shifts easy to understand at a glance without needing to compare old and new tables manually. | ![screenshot](documentation/features/community-rankings.png) ![screenshot](documentation/features/change-indicators.png) |
| Collectables Index | A dedicated Collectables section displays items such as Precursor Orbs and Power Cells in a clear, ordered layout. | ![screenshot](documentation/features/collectables-list.png) |
| Image Integration | Images are displayed consistently across characters, weapons, and collectables to enhance visual recognition and usability. | (See above.) |
| User Authentication | Django authentication allows users to register, log in, and log out securely. | ![screenshot](documentation/features/register.png) ![screenshot](documentation/features/login.png) |
| Secure User Actions | Authentication and permissions ensure that only authorised users can submit weapon ratings and manage their own accounts. | ![screenshot](documentation/features/security.png) ![screenshot](documentation/features/security-2.png)|
| Admin Content Management | Site administrators can create, read, update, and delete content across all website apps using the Django admin interface. | ![screenshot](documentation/features/admin-crud.png) ![screenshot](documentation/features/admin-crud-2.png) |
| User Feedback Messages | Django messages provide clear feedback when user actions succeed or fail, improving usability and clarity. | ![screenshot](documentation/features/django-message.png) ![screenshot](documentation/features/django-message-2.png) ![screenshot](documentation/features/django-message-3.png) |
| Custom Error Pages | Custom 400, 403, 404, 429, and 500 error pages maintain site theming while improving error handling. | ![screenshot](documentation/defensive/400.png) ![screenshot](documentation/defensive/403.png) ![screenshot](documentation/defensive/404.png) ![screenshot](documentation/defensive/429.png) ![screenshot](documentation/defensive/500.png) |
| Responsive Design | The site is fully responsive and accessible across desktop, tablet, and mobile devices. | ![screenshot](documentation/features/responsive-mobile.png) ![screenshot](documentation/features/responsive-tablet.png) ![screenshot](documentation/features/responsive-desktop.png) |
| Cloudinary Media Hosting | All uploaded images are stored and served via Cloudinary to ensure performance and reliability. | ![screenshot](documentation/features/cloudinary.png) |
| Production Deployment | The project is deployed to Heroku, a live production environment and accessible online. | ![screenshot](documentation/features/deployment.png) |

---

### Future Features

The following features were identified during planning but were outside the scope of the current project iteration. These features would further enhance user engagement, depth of content, and long-term scalability of the **Jak and Daxter Wiki**.

- **Search Functionality**  
  Implement a global search feature allowing users to search for weapons, characters, collectables, and future content such as enemies or lore pages.

- **Enemy Database**  
  Add a dedicated section for enemies, including behaviour descriptions, strengths, weaknesses, and images to expand the encyclopaedic nature of the site.

- **Dark and Light Jak Pages**  
  Introduce detailed pages covering Jak’s Dark and Light forms, explaining how abilities evolve across the series.

- **User Comments and Discussions**  
  Allow registered users to comment on characters, weapons, and collectables to encourage community interaction and discussion.

- **User Profiles**  
  Provide registered users with profile pages showing their activity, such as comments made or content interacted with.

- **Featured Content System**  
  Enable admins to mark weapons, characters, or collectables as “featured” for display on the homepage.

- **Advanced Filtering and Sorting**  
  Add filters for weapons (eco colour, type), characters (role, faction), and collectables to improve content discoverability.

- **Lore and Story Pages**  
  Expand the wiki to include story summaries, locations, factions, and timeline-based lore content.

- **Favourites System**  
  Allow users to save favourite weapons, characters, or collectables for quick access later.

- **Admin Analytics Dashboard**  
  Provide site administrators with insights into popular pages, most viewed weapons, and user engagement metrics.

- **Improved SEO Optimisation**  
  Add meta descriptions, structured data, and SEO-friendly URLs to improve search engine visibility.

- **Multilingual Support**  
  Support multiple languages to make the wiki accessible to a wider international audience.

- **Game Rating and Reviews System**
  Allow registered users to rate the three core Jak and Daxter games out of ten and optionally provide written reasons for their ratings. This would encourage community discussion, surface differing player perspectives, and add comparative insight across the trilogy.

- **Expanded Franchise Coverage**
  Extend the wiki to cover the remaining Jak and Daxter titles released after the original trilogy, including Jak X: Combat Racing (2005), Daxter (2006), and Jak and Daxter: The Lost Frontier (2009). Each game could include dedicated pages for gameplay mechanics, characters, and unique features.

These features directly map to several defined user stories, particularly those focused on searchability, deeper lore exploration, user engagement, and expanded content coverage. They represent logical next steps should development continue beyond the current assessment scope.

---

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | Loader handling on Weapon Rating page. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Used as a learning aid for debugging, explanations and planning. |

---

## Database Design

### Data Model

Entity Relationship Diagrams (ERDs) are used to visualise the database architecture of the **Jak and Daxter Wiki** project.

The ERD for this project has been created **directly from the implemented Django models** across the `characters`, `morphgun`, and `collectables` apps to ensure the diagram accurately reflects how data is stored, related, and accessed at runtime.

The data model supports:
- Multiple content domains (Characters, Morph Gun, Collectables data).
- Controlled CRUD access via authentication and staff permissions.
- User-generated content (weapon ratings).
- Clear one-to-many and many-to-one relationships without unnecessary complexity.

![Entity Relationship Diagram](documentation/erd.png)

---

### Mermaid ERD

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram

    USER {
        int id PK
        string username
        string email
        boolean is_staff
    }

    CHARACTER {
        int id PK
        string name
        string quote
        string image
        string sex
        string age
        string skin
        string hair
        string eyes
        string height
        string weight
        string occupation
        string appearance
        string personality
    }

    COLLECTABLE {
        int id PK
        string name
        string description
        string image
    }

    COLOUR {
        int id PK
        string name
        string description
        string image
    }

    WEAPON {
        int id PK
        string name
        string description
        string image
    }

    UPGRADE {
        int id PK
        string name
        string effect
        string requirement
        int price
        string game
    }

    RATING {
        int id PK
        int score
    }

    COLOUR ||--o{ WEAPON : "groups"
    WEAPON ||--o{ UPGRADE : "has"
    USER ||--o{ RATING : "submits"
    WEAPON ||--o{ RATING : "receives"
```

Source: [Mermaid](https://mermaid.live/edit#pako:eNq9VO9v2jAQ_Vei-wwoIBJovqUUddNYQSlo0hSpcpNLYpXYqX9sZZT_vU4glM5Um1Sp_mQ_v7t395zcFhKeIgSA4oqSXJAyZjFzzFrdTiNnu9_XizLl0NRZfHuFpBKU5Y6WKBgp0brAktD1K3rP-RoJc6i8k4pk2f5m1wpOvoRROFn-r-pZxUfNlY3SkuQ2KvHJws7yHiizwIJQYfe7QWkzkeaFsuDf52GeJLoiinJbklQVEkFYYpdYoZCckTVVm79Nnc9m08kyvJxNP2BrijIRtDpb1om5p6rzVfSJgj-m4WJ-84mCq8V1FF59xFPMMkzsD0Dgo6YCS2TqbepK0DMvnx9TH0uLwuXXm-t_VFZDMuHinZd7fu52-ba1NXBiyAXXlYzhjd8HWmtGzSvIkdRMkAPlUFTNkPq-pOqdVCc8gQnSX-aPAugYeZpCoITGDpQozGAxR2h6jEEVxq8Y6qCUiIc6887EVIT95Lxsw0wDeQFBRtbSnHSVEoWHmddSiFb8dsOSYwiyFMWEa6Yg8JqMEGzhCYKBP-4N_ZHn-a7XHw3dQQc2EHTdnusPvL43vhhceOORP-wPdx3401Th9sYjkwNTqrj4vp-6zfDdvQBGNqCD)

---

### ERD Explanation

- **User**
  - Represents authenticated site users.
  - Used to control access to restricted functionality such as weapon rating.
  - Staff users (`is_staff=True`) are permitted to create, update, and delete site content.

- **Character**
  - Stores detailed encyclopaedic information about characters from the Jak and Daxter universe.
  - Includes descriptive fields such as appearance and personality.
  - Displayed publicly as read-only content.

- **Collectable**
  - Represents collectible items from the game series.
  - Managed by staff users and displayed independently within the site.

- **Colour**
  - Represents Morph Gun eco types (e.g. Red, Yellow, Blue, Dark).
  - Acts as a parent entity for Morph Gun weapons.

- **Weapon**
  - Represents individual Morph Gun weapon modifications.
  - Each weapon belongs to a single **Colour**, forming a one-to-many relationship.
  - Weapons are publicly viewable, with staff-only CRUD functionality.

- **Upgrade**
  - Represents Morph Gun upgrades available in *Jak II* and *Jak 3*.
  - Each upgrade is linked to a single weapon.
  - Supports game-specific data such as requirements and optional pricing.

- **Rating**
  - Represents user-submitted weapon ratings (1-10).
  - Forms a many-to-one relationship between **User** and **Weapon**.
  - Used to calculate community averages and rankings.

---

### Relationship Design Rationale

The database structure has been intentionally designed to remain **simple, logical, and scalable**:

- One-to-many relationships are used where appropriate (Colours → Weapons, Weapons → Upgrades).
- User-generated data (Ratings) is separated from core content to maintain data integrity.
- No unnecessary many-to-many relationships were introduced, keeping queries efficient and models readable.
- Staff-only content management is enforced at the view and template level rather than through database complexity.

This structure fully supports the current feature set while allowing for future expansion, such as:
- Linking characters or collectables to specific games or locations.
- Expanding user interaction features beyond weapon ratings.

---

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/LouisCE/jak-and-daxter-wiki/projects) was used as the primary Agile planning and tracking tool for the **Jak and Daxter Wiki** project.

The project board followed a Kanban-style workflow and was used to:

* Plan and track EPICs and User Stories
* Break down features into manageable development tasks
* Track progress from *To Do* through *In Progress* to *Done*
* Record bugs and technical issues discovered during development

The board was updated regularly throughout the build process to reflect the current state of development and priorities.

![screenshot](documentation/gh-projects.png)

---

### GitHub Issues

[GitHub Issues](https://www.github.com/LouisCE/jak-and-daxter-wiki/issues) were available as a supporting tool but were not used as the primary method of tracking work during development.

Instead, User Stories and tasks were managed directly within the GitHub Projects board, where items were created, prioritised, and moved through the Kanban workflow from *To Do* to *In Progress* to *Done*. Bugs were logged manually within **TESTING.md**, allowing all planning, progress tracking, and issue documentation to remain centralised during development.

GitHub Issues may be used in future iterations to separately log bugs and enhancements once the project moves beyond the current assessment scope.


| Link                                                                                                                                                                                                                                                                                      | Screenshot                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| [![GitHub open issues](https://img.shields.io/github/issues-search/LouisCE/jak-and-daxter-wiki?query=is%3Aissue%20is%3Aopen%20-label%3Abug\&label=Open%20Issues\&color=yellow)](https://www.github.com/LouisCE/jak-and-daxter-wiki/issues?q=is%3Aissue%20is%3Aopen%20-label%3Abug)        | ![screenshot](documentation/gh-issues-open.png)   |
| [![GitHub closed issues](https://img.shields.io/github/issues-search/LouisCE/jak-and-daxter-wiki?query=is%3Aissue%20is%3Aclosed%20-label%3Abug\&label=Closed%20Issues\&color=green)](https://www.github.com/LouisCE/jak-and-daxter-wiki/issues?q=is%3Aissue%20is%3Aclosed%20-label%3Abug) | ![screenshot](documentation/gh-issues-closed.png) |

---

### MoSCoW Prioritisation

User Stories were prioritised using the **MoSCoW** method to ensure that core functionality was delivered first, while still allowing room for enhancements if time permitted.

Each User Story was labelled accordingly within GitHub Issues:

* **Must Have** – Core features required for the site to function correctly and meet the project’s assessment criteria
* **Should Have** – Important features that significantly improve user experience but are not strictly essential
* **Could Have** – Nice-to-have features that add extra polish if time allows
* **Won’t Have** – Features intentionally deferred to future development beyond the scope of this submission

This prioritisation helped guide development decisions and ensured the project remained achievable within the available timeframe.

---

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found here:  
[Heroku Deployment – Jak and Daxter Wiki](https://jak-and-daxter-wiki-420eda56706b.herokuapp.com)

### Heroku Deployment

This project is deployed using **Heroku**, a cloud-based Platform as a Service (PaaS) used to run Django applications in production.

Below are the exact steps I followed to deploy the Jak and Daxter Wiki.

#### Create a New Heroku App

1. Log into the Heroku Dashboard.
2. Click **New** → **Create new app**.
3. Choose a unique app name (in my case, `jak-and-daxter-wiki`).
4. Select the region closest to me (in my case, the EU as a UK user).
5. Click **Create App**.

#### Config Vars

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

#### Required Heroku Files

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

#### Python Version File

The **[.python-version](.python-version)** file tells Heroku the specific version of Python to use when running your application.

- In my case, the version is `3.12`

#### Connecting GitHub to Heroku

For Heroku deployment, I followed these steps to connect my GitHub repository to the newly created app:

1. In the Heroku app dashboard, I went to the **Deploy** tab.
2. I chose **GitHub** as the deployment method.
3. I searched for my repository: `LouisCE/jak-and-daxter-wiki`.
4. I clicked **Enable Automatic Deploys**.

#### Deployment Complete

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

- Submitted my email address to the [CI PostgreSQL Database provisioning page](https://dbs.ci-dbs.net)
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
   [Jak and Daxter Wiki repository](https://www.github.com/LouisCE/jak-and-daxter-wiki)
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
> Instructions can be found here: [Gitpod browser extension setup](https://www.gitpod.io/docs/configure/user-settings/browser-extension)

#### Forking

By forking the GitHub repository, you create a copy of the original project on your own GitHub account. This allows you to view and edit the project freely without affecting the original repository. You can fork this repository by following these steps:

1. Log in to GitHub and navigate to the **Jak and Daxter Wiki** repository:  
   [Jak and Daxter Wiki repository](https://www.github.com/LouisCE/jak-and-daxter-wiki)
2. At the top-right of the repository page, just below the “Settings” tab, click the **Fork** button.
3. After clicking Fork, GitHub will create a copy of the repository under your own account. You can now work on your fork independently!

### Local vs. Deployment

There are no remaining major differences between the local version of the Jak and Daxter Wiki and the deployed version online. Both environments function the same, with identical features, structure, and behaviour.

---

## Credits

### General Guidance

The following learning resources were used as reference material and general guidance during development:

- The **Code Institute LMS** and the **I Think Therefore I Blog** walkthrough project were used as a reference for setting up core Django functionality, project structure, and deployment workflows.  
  [Code Institute LMS – I Think Therefore I Blog walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+11/courseware/713441aba05441dfb3a7cf04f3268b3f/824fccecd0fe4e44871eeabcbf69d830/)

- The **PP4 Assessment Criteria** provided by Code Institute were used to shape the structure, scope, and documentation standards of the project.
  [PP4 Assessment Criteria (Code Institute)](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST_PAGPPF+2/courseware/8f9fd8690aad4776a05eaf462b430f46/995834f1924a4086af51870bf92f6516/)

### Content

The following resources were used during the development of the **Jak and Daxter Wiki** project. Any external code, tools, frameworks, or guidance have been referenced here to ensure full transparency.

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Used as a structural guide for README.md and TESTING.md documentation |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | Guidance on writing clear, meaningful Git commit messages |
| [Code Institute](https://codeinstitute.net) | General project structure guidance and best practices |
| [Bootstrap](https://getbootstrap.com) | Responsive layout, grid system, and UI components |
| [MDBootstrap – Registration & Login Forms](https://mdbootstrap.com/docs/standard/extended/registration/#!) | Used as inspiration for the layout and structure of the `register.html` and `login.html` templates. Adapted to fit Django form rendering and project styling. |
| [Django Documentation](https://docs.djangoproject.com) | Reference for Django models, views, templates, and settings |
| [Cloudinary](https://cloudinary.com) | Hosting and management of image/media assets |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file handling in production |
| [Mermaid](https://mermaid.live) | Creation of an interactive ERD for database visualisation |
| [Python Tutor](https://pythontutor.com) | Assistance with understanding Python logic during development |
| [ChatGPT](https://chatgpt.com) | Help with debugging and explanations |

### Media

The following external sources were used for images and reference material related to the Jak and Daxter franchise:

- **Official Jak and Daxter Wiki (Fandom):** Source of character images, collectibles, and general reference material.
  [Jak and Daxter Wiki (Fandom)](https://jakanddaxter.fandom.com/)

- **IGN – Jak 3 Weapons:** Used as reference for weapon mod descriptions.
  [IGN – Jak 3 Weapons](https://www.ign.com/wikis/jak-3/Weapons)

- **Morph Gun image references:** Sourced from the Jak and Daxter Wiki.
  [Morph Gun (Fandom)](https://jakanddaxter.fandom.com/wiki/Morph_Gun)

- **Morph Gun upgrade references:** Used to fill weapon upgrade information.
  [Morph Gun upgrades (Fandom)](https://jakanddaxter.fandom.com/wiki/Morph_Gun_upgrades)

### Code & Feature References

The following resources were used to understand and implement grouped data display in Django templates using the `regroup` template tag, as applied in the `weapon_list.html` template.

- Django documentation on the **Regroup** template tag, used for grouping data within templates.
  [Django docs – `regroup` template tag](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#regroup)

- Example of grouping content by category (FAQs):
  [Grouping content example (FAQs)](https://www.iraqikurdistanguide.com/faqs/)

- Regroup implementation reference from Mentor Tim’s repository:
  [Mentor Tim regroup reference (GitHub)](https://github.com/TravelTimN/iraqikurdistanguide/blob/main/faqs/templates/faqs/faqs.html#L21)

### Acknowledgements

I would like to acknowledge the following people and communities for their support throughout the development of this project:

- I would like to thank my Code Institute mentor, **Tim Nelson** ([TravelTimN](https://www.github.com/TravelTimN)), for his guidance, patience, feedback, and support throughout the development of this project.
- I would like to thank the **Code Institute Slack** and **Discord communities** for ongoing encouragement, advice, and moral support during challenging stages of the project.