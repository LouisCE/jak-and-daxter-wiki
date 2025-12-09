# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Bugs

For convenience, I have used manual logs to track bugs during development.

### Fixed Bugs

Below is a detailed summary of the most significant bugs that I encountered and fixed during the project:

---

#### 1. Heroku CLI Not Detectable in PowerShell  
**Issue:**  
PowerShell could not find the `heroku` command unless I typed the full path:

```bash
& 'C:\Program Files\heroku\bin\heroku.cmd'
```

**Cause:**  
The Python virtual environment PATH on Windows overshadowed the system PATH.

**Fix:**  
Stopped relying on the CLI entirely, as recommended by Mentor Tim, and used the Heroku Dashboard instead.

---

#### 2. Heroku Was Not Updating Deployed Changes  
**Issue:**  
My local project worked perfectly, but Heroku stopped showing updates whenever I clicked **Deploy Branch**.  
At first I thought it was the Heroku CLI being broken, because commands on PowerShell failed unless I prefixed them with the full path to `heroku.cmd`.

**Cause:**  
It turned out the problem was *not* the CLI, my Heroku deployment was crashing due to internal server errors on the `/morphgun/` page, so the deploy “succeeded” but the app couldn't load.

**Fix:**  
Investigated logs, identified a failing URL pattern and a missing database configuration (see below), then redeployed.

---

#### 3. PostgreSQL vs SQLite Confusion  
**Issue:**  
I believed my local data should automatically appear on Heroku. Superuser accounts also didn’t match.

**Cause:**  
SQLite was being used locally, while Heroku always uses PostgreSQL.  
These databases are completely separate.

**Fix:**  
Used PostgreSQL for both environments by putting Heroku’s `DATABASE_URL` into `env.py`.  
Later learned SQLite is only needed when writing unit tests.

---

#### 4. Local Database Did Not Match Heroku Database  
**Issue:**  
I could not log into the Heroku admin panel and none of my weapon objects or colour objects appeared on Heroku.

**Cause:**  
My local environment had no `DATABASE_URL` variable, meaning Django was using SQLite locally.  
Heroku, however, was using PostgreSQL.  
Because they were completely separate, all migrations and superuser accounts were out of sync.

**Fix:**  
Added the same PostgreSQL `DATABASE_URL` from Heroku into my local `env.py` file so both environments used the same database.

---

#### 5. DEBUG and ALLOWED_HOSTS Blocking Error Visibility on Heroku  
**Issue:**  
Heroku only displayed a generic **Application Error**, making debugging impossible.

**Cause:**  
`DEBUG` was hard-coded in `settings.py`, preventing temporary debugging on Heroku.

**Fix:**  
Refactored `settings.py` to use environment variables:
```python
DEBUG = os.environ.get("DEBUG")
ALLOWED_HOSTS = []
CSRF_TRUSTED_ORIGINS = []

host = os.environ.get("HOST")
if host:
    ALLOWED_HOSTS.append(host)
    CSRF_TRUSTED_ORIGINS.append(f"https://{host}")
```
Then temporarily added `DEBUG=True` on Heroku (later removed).

---

### 6. Static Files Not Loading on Deployment  
**Issue:**  
CSS/images failed to load on Heroku.

**Cause:**  
Static folder placed in wrong directory before WhiteNoise integration.

**Fix:**  
Moved `/static/` to project root and updated settings.

---

#### 7. Placeholder `settings.py` Code Broke Deployment  
**Issue:**  
Heroku was throwing a 500 error on the homepage even before I built new features.

**Cause:**  
I had placeholder/incomplete configuration still inside `settings.py`, which crashed production.

**Fix:**  
Removed the placeholder code and applied the corrected configuration method provided by Mentor Tim.

---

#### 8. App Naming Structure Mistake (“weapons” Should’ve Been “morphgun”)  
**Issue:**  
Originally created the `morphgun` app as `weapons`, but the logical structure should have been:

```
morphgun/
    colours/
        weapons/
```

Instead, my structure became:

```
weapons/
    colours/
        weapons/
```

**Fix:**  
Created a new `morphgun` app and migrated all the code there. After verifying the new app worked, I safely deleted the old `weapons` app after migrations.

---

#### 9. Navbar and Templates Not Rendering Due to Structure Changes  
**Issue:**  
After moving everything into the new `morphgun` app, templates stopped rendering correctly.

**Cause:**  
Template directories changed, but some old paths still referenced `weapons/` instead of `morphgun/`.

**Fix:**  
Updated all template directory paths, `{% include %}` references, and view imports to match the new app structure.

---

### 10. Template Inheritance Errors After Adding base.html   
**Issue:**  
Pages lost styling or rendered incorrectly.

**Cause:**  
Templates still using old paths like `morphgun/base.html`.

**Fix:**  
Converted all templates to `{% extends "base.html" %}`.

---

#### 11. Internal Server Error (500) on `/morphgun/`  
**Issue:**  
Locally the page worked, but on Heroku it threw a 500 error.

**Cause:**  
The `weapon_list.html` template linked to  
`{% url 'weapon_detail' weapon.pk %}`  
but in `morphgun/urls.py` the detail view path was missing the `weapon/` prefix.  
It expected:  
`path('weapon/<int:pk>/', ...)`

**Fix:**  
Updated the URL pattern:
```python
path("weapon/<int:pk>/", views.weapon_detail, name="weapon_detail")
```
Redeployment fixed the routing error.

---

### 12. Character Pages Returning 404  
**Issue:**  
Character CRUD existed but pages gave "URL not found".

**Cause:**  
Forgot to add URL patterns for list/detail/create/edit/delete.

**Fix:**  
Added full URL config and connected to templates.