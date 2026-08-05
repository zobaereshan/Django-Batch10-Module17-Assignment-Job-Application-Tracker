# Job Application Tracker

A Django web app for tracking job applications — built to practice Forms, CRUD
operations, template inheritance, and custom middleware.

## Features

- **Home dashboard** with total application count and a breakdown by status
  (Applied, Interview, Offer, Accepted, Rejected).
- **Full CRUD** for job applications: create, list (with search/filter), view
  detail, update, and delete (with a confirmation page).
- **Django ModelForm** validation:
  - Company name is required.
  - Position is required.
  - Salary cannot be negative.
  - Deadline cannot be earlier than the application date.
  - Notes cannot exceed 500 characters.
  - Errors are displayed inline, below each field.
- **Template inheritance**: `base.html` is extended by every page; `navbar.html`
  and `footer.html` are included as partials.
- **Bootstrap 5** styling with a small custom stylesheet (`static/css/style.css`).
- **Success messages** (Django messages framework) after Create, Update, and
  Delete.
- **Custom middleware** (`jobs/middleware/RequestLoggerMiddleware`) that logs
  the timestamp, HTTP method, and path of every request to the console.

## Project Structure

```
job_tracker/
├── job_tracker/          # Project settings, URLs, WSGI/ASGI
├── jobs/                 # App: models, forms, views, urls, middleware, admin
├── templates/
│   ├── base.html
│   ├── navbar.html
│   ├── footer.html
│   ├── home.html
│   └── jobs/
│       ├── list.html
│       ├── create.html
│       ├── update.html
│       ├── delete.html
│       ├── detail.html
│       └── _form_fields.html   # shared form-field partial (create/update)
├── static/
│   └── css/style.css
├── manage.py
└── requirements.txt
```

## URL Structure

| URL                    | View          | Description                      |
|-------------------------|---------------|-----------------------------------|
| `/`                     | `home`        | Dashboard with summary cards      |
| `/jobs/`                | `job_list`    | Table of all applications         |
| `/jobs/add/`            | `job_create`  | Add a new application             |
| `/jobs/<id>/`           | `job_detail`  | View a single application         |
| `/jobs/<id>/edit/`      | `job_update`  | Edit an application                |
| `/jobs/<id>/delete/`    | `job_delete`  | Confirm & delete an application    |

## Getting Started

1. **Clone the repository and enter the project folder**
   ```bash
   git clone <your-repo-url>
   cd job_tracker
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **(Optional) Create a superuser to use the Django admin**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. Visit `http://127.0.0.1:8000/` in your browser.

## Middleware Log Output

Every request logs to the console in the following format:

```
---------------------------------
Time   : 2026-07-22 10:45 AM
Method : GET
Path   : /jobs/
---------------------------------
```

## Model

`JobApplication` (`jobs/models.py`):

| Field             | Type          |
|-------------------|---------------|
| company_name      | CharField     |
| position          | CharField     |
| job_location       | CharField     |
| salary (optional) | DecimalField  |
| status            | CharField (choices) |
| application_date  | DateField     |
| deadline          | DateField     |
| notes             | TextField     |
| created_at        | DateTimeField (auto) |
| updated_at        | DateTimeField (auto) |

Status choices: `Applied`, `Interview`, `Offer`, `Accepted`, `Rejected`.
