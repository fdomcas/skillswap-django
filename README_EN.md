# SkillSwap

<div align="center">

![SkillSwap Logo](./staticfiles/imgs/logo.png)

**A collaborative platform for exchanging skills and knowledge**

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Workflow](#-workflow)
- [Traceability Map](#-traceability-map)

---

## 🎯 About

**SkillSwap** is a web application that allows users to exchange skills and knowledge with other members of the community. Whether you want to learn a new skill or teach something you know, SkillSwap connects people with shared interests and complementary abilities.

The platform enables users to:
- Create posts offering or requesting specific skills
- Search and filter available posts with persistent session-based filters
- Manage a customizable user profile with skills, bio, timezone, and availability
- Propose, accept, and manage skill-exchange agreements through a full lifecycle
- Schedule and track sessions within each agreement
- Maintain theme (light/dark) preference via cookie (set via POST form)
- Access a REST API (admin-restricted) for all core resources

---

## ✨ Features

### Core Features
- 🔐 **User Authentication** — Secure registration and login supporting username *or* e-mail, with disposable-email domain blocking
- 🚫 **Account Banning** — Admins can ban/unban users; banned users see a clear error message on login
- 💬 **Skill Posts** — Create posts of type *OFREZCO* (I offer) or *BUSCO* (I'm looking for), each linked to a specific skill
- 🔍 **Smart Search & Filtering** — Natural-language search supporting queries like `busco python`, `ofrezco django y busco react`, etc.
- 💾 **Persistent Filters** — Search state is stored in the session and restored on the next visit; cleared with one click
- 👤 **User Profiles** — Bio, timezone, availability, and a personal skill list; profile is auto-created on registration via a Django signal
- 🤝 **Agreements (Deals)** — Propose a skill-swap agreement directly from a post detail page with configurable weeks, session duration, and conditions; full status lifecycle: `PROPUESTO → ACEPTADO → EN CURSO → FINALIZADO / CANCELADO`
- 📅 **Sessions** — Schedule sessions linked to an ongoing agreement with a specific date and time; a Jitsi Meet video-call link is automatically generated on creation and becomes active only during the session window; summary and attendance are filled in afterwards
- 📊 **Statistics Dashboard** — Restricted to moderators and admins; aggregated metrics on posts, agreements, sessions, and users
- 🎨 **Theme Switching** — Light / Dark mode toggle stored in a cookie (1-year expiry)
- 🛡️ **Anti-Spam Middleware** — Blocks more than 3 post creations per user within 24 hours
- 🔌 **REST API** — Full CRUD endpoints for `Usuario`, `Publicacion`, `Acuerdo`, and `Sesion`; restricted to admin users; auto-documented with Swagger UI at `/api/docs/`


---

## 🛠️ Tech Stack

### Backend
| Component | Technology |
|-----------|------------|
| Framework | Django 6.0.2 |
| Language | Python 3.14 |
| Database | PostgreSQL 16 |
| WSGI Server | Gunicorn |
| Static Files | WhiteNoise 6.7.0 |
| REST API | Django REST Framework ≥ 3.14 |
| API Docs | drf-spectacular ≥ 0.27 |
| Email Validation | disposable-email-domains |
| Env Management | python-dotenv ≥ 1.0 |
| Video Calls | Jitsi Meet (self-hosted) |

### Frontend
- **HTML5** & **CSS3**
- **Bootstrap 5** (responsive grid, modals, and components)
- **JavaScript (Vanilla)** — dynamic skill filtering, toast notifications, Bootstrap modals, history navigation

### DevOps
- **Docker** & **Docker Compose**
- **Cloudflare Tunnel** (optional, production only)
- **pip** / `requirements.txt`

---

## 📦 Installation

### Prerequisites
- **Docker** and **Docker Compose** — recommended for the quickest start
- **Python 3.14+** and **PostgreSQL 16+** — if running locally without Docker
- **Git**

### 1. Clone the Repository

```bash
git clone https://github.com/amahcan562-ies/skillswap-django.git
cd skillswap-django

# Add upstream remote (original repository)
git remote add upstream https://github.com/jherhum1702/skillswap-django.git
```

### 2. Create the Environment File

```bash
cp .env.example .env
```

Edit `.env` with your values:

```dotenv
# Database
DB_NAME=skillswap_db
DB_USER=django_user
DB_PASSWORD=your_secure_password
DB_HOST=localhost        # use "db" when running with Docker
DB_PORT=5432

# Django
SECRET_KEY=your_django_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000

# Cloudflare Tunnel (optional — production only)
TUNNEL_TOKEN=your_tunnel_token_here
```

Generate a `SECRET_KEY` if you don't have one:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 🐳 Docker Setup (Recommended)

```bash
# Start all services (web + PostgreSQL)
docker compose up -d

# View logs
docker compose logs -f web

# Stop services
docker compose down
```

The application will be available at **http://localhost:8000**.

Docker automatically:
1. Applies all migrations (`python manage.py migrate`)
2. Populates test data (`python manage.py populate_test_data`)
3. Collects static files
4. Starts Gunicorn on port 8000

**Useful Docker commands:**

```bash
# Access the database shell
docker compose exec db psql -U django_user -d skillswap_db

# Run any Django management command
docker compose exec web python manage.py <command>

# Full reset (removes the database volume)
docker compose down -v && docker compose up -d
```

---

## 🖥️ Local Development Setup

### 1. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure PostgreSQL

```sql
-- Connect as the postgres superuser
sudo -u postgres psql

CREATE DATABASE skillswap_db;
CREATE USER django_user WITH PASSWORD 'your_password';
ALTER ROLE django_user SET client_encoding TO 'utf8';
ALTER ROLE django_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE django_user SET default_transaction_deferrable TO on;
ALTER ROLE django_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE skillswap_db TO django_user;
\q
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Load Test Data (Optional)

```bash
python manage.py populate_test_data
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

> A superuser is required to access `/admin/` and the REST API endpoints at `/api/`.

### 7. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 8. Start the Development Server

```bash
python manage.py runserver 0.0.0.0:8000
```

Visit **http://localhost:8000**.

---

## ⚙️ Configuration

### Environment Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `DB_NAME` | PostgreSQL database name | `skillswap_db` |
| `DB_USER` | PostgreSQL user | `django_user` |
| `DB_PASSWORD` | PostgreSQL password | `secure_password` |
| `DB_HOST` | Database host | `localhost` / `db` (Docker) |
| `DB_PORT` | Database port | `5432` |
| `DEBUG` | Django debug mode | `True` (dev only) |
| `SECRET_KEY` | Django secret key | Generated value |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | `localhost,127.0.0.1` |
| `CSRF_TRUSTED_ORIGINS` | CSRF-safe origins (with scheme) | `http://localhost:8000` |
| `TUNNEL_TOKEN` | Cloudflare Tunnel token | Your token |

### Key Files

| File | Purpose |
|------|---------|
| `skillswap/settings.py` | Main Django settings |
| `skillswap/urls.py` | Project-level URL routing + API doc routes |
| `core/urls.py` | App-level URL routing and DRF router |
| `core/context_processors.py` | Cookie theme preference injected into every template |
| `core/session_manager.py` | Session-based search filter helpers |
| `core/middleware/anti_spam.py` | Spam protection middleware |
| `core/serializers.py` | DRF serializers for the REST API |
| `.env` | Local environment variables (never commit) |

---

## 🚀 Usage

### Test Credentials

After running `populate_test_data`, **20 test users** are available. Every test user has the password **`1234`**. A few notable ones:

| Username | Name | Description |
|----------|------|-------------|
| `pacogamer30` | Paco Tester | Gaming & programming learner |
| `anadev` | Ana López | Frontend developer |
| `laurasan` | Laura Sánchez | English teacher learning programming |
| `carlosdev` | Carlos Ruiz | Backend developer (Django / Docker) |
| `sofiahm` | Sofía Hernández | UX/UI designer |

> To access **`/admin/`** or the **REST API**, you need a superuser created with `python manage.py createsuperuser`.

### Feature Guide

#### Search & Filter
- Type any skill name in the home-page search bar
- Use prefixes for targeted searches:
  - `busco python` → BUSCO posts about Python
  - `ofrezco django` → OFREZCO posts about Django
  - `busco react y ofrezco javascript` → combined filter
- Filters are saved in your session and restored on the next visit
- Click **"Clear filters"** to reset

#### Agreements (Deals)
1. Open any post detail page (`/posts/<id>`)
2. Click **"Propose Agreement"** to open the deal creation form
3. Configure weeks, session duration, sessions per week, and conditions
4. The post author receives the proposal and can **Accept** it
5. Once accepted, either participant can **Start** the agreement (→ `EN CURSO`)
6. From the deal detail page, participants can **create sessions**, **finish**, or **cancel** the agreement

#### Sessions
- Sessions can only be created while the agreement is `EN CURSO`
- When creating a session, set the **date**, **time**, and **planned duration** (60–240 min)
- A **Jitsi Meet video-call link** is automatically generated and saved to the session on creation
- The join button becomes active only during the session window (between start time and end time); before that it shows as disabled
- Once the session has passed, either participant can fill in the **summary and attendance** via the edit form
- All your sessions are listed at `/sessions/`

#### Theme
- Use the **☀️/🌙** toggle in the navbar to switch between light and dark mode
- The theme preference is stored in a cookie and persists for 1 year

#### Statistics (Moderators / Admins)
- Visit `/statistics/` — only accessible to staff and users in the `Moderador` group
- Shows post counts, agreement states, session totals, recent activity, and the moderator list

#### REST API (Admins only)
- **Base URL**: `/api/`
- **Resources**: `usuarios`, `publicaciones`, `acuerdos`, `sesiones`
- **Interactive docs (Swagger UI)**: `/api/docs/`
- **OpenAPI schema**: `/api/schema/`

---

## 📁 Project Structure

```
skillswap-django/
├── core/                            # Main Django application
│   ├── management/commands/
│   │   └── populate_test_data.py   # Idempotent DB seeder (20 users, 36 skills, posts, deals, sessions)
│   ├── middleware/
│   │   └── anti_spam.py            # Limits post creation to 3 per 24 h per user
│   ├── services/
│   │   └── meet.py                 # Generates unique Jitsi Meet room URLs (UUID-based)
│   ├── migrations/                  # Database migrations
│   ├── static/imgs/                 # App-level static files
│   ├── templates/core/
│   │   ├── home.html               # Home page with search
│   │   ├── search_results.html     # Search results
│   │   ├── post_list.html          # All posts listing
│   │   ├── post_detail.html        # Single post + agreement proposal button
│   │   ├── postCreate.html         # Create post form
│   │   ├── post_update.html        # Edit post form
│   │   ├── profile.html            # User profile view
│   │   ├── profile_update.html     # Edit profile form
│   │   ├── dealsCreate.html        # Propose agreement form
│   │   ├── dealslist.html          # List of user's agreements
│   │   ├── dealsDetail.html        # Agreement detail + session creation
│   │   ├── sesioneslist.html       # List of user's sessions (with live Join button)
│   │   ├── sesionCreate.html       # Create session form (date, time, duration)
│   │   ├── sesion_detail.html      # Session detail view with Jitsi link + attendance
│   │   ├── sesion_edit.html        # Edit session after it ends (summary + attendance)
│   │   └── statistics.html         # Admin/Moderator statistics dashboard
│   ├── admin.py                    # Django admin (ban/unban actions)
│   ├── apps.py
│   ├── context_processors.py       # Reads theme cookie → template context
│   ├── forms.py                    # All Django forms with validation logic
│   ├── models.py                   # Habilidad, Usuario, Perfil, Publicacion, Acuerdo, Sesion
│   ├── serializers.py              # DRF serializers
│   ├── session_manager.py          # Save/get/clear search filters in session
│   ├── urls.py                     # All app routes + DRF router
│   └── views.py                    # All CBVs, FBVs, and DRF ViewSets
│
├── skillswap/
│   ├── settings.py                 # Project settings (env-based config)
│   ├── urls.py                     # Root URL conf + API doc routes
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── base.html                   # Base template with theme, navbar, messages
│   └── registration/
│       ├── login.html
│       └── registration.html
│
├── staticfiles/                     # Collected static files (production)
├── locale/                          # i18n translation files (es, en)
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── gunicorn.ctl
```

---

## 📊 Workflow

### Git Strategy

The team used a **Git Flow**-inspired workflow with three contributors working across three forks and integrating through a shared upstream repository.

---

### 1. Branch Structure and Integration

#### Main Branches
| Branch | Purpose |
|--------|---------|
| `main` | Production-ready, stable code |
| `develop` | Integration branch — all features merge here first |

#### Feature and Bugfix Branches
All work was done in dedicated branches created from `develop` and merged back via Pull Request.

**Features:**
| Branch | Feature | Author | PR |
|--------|---------|--------|----|
| `feature/cookies` | Light/Dark theme preference (cookie + context processor) | amahcan562-ies | #51 ✅ |
| `feature/post_list` | Post listing view and template | fdomcas | #50 ✅ |
| `feature/populate_db` | Database population management command | jherhum1702 | #41 ✅ |
| `feature/home-page` | Home page with smart search (Q objects) | jherhum1702 | #53 ✅ |
| `feature/Perfil_usuario` | User profile view and edit | fdomcas | #56 → reverted #58 → re-implemented #61 ✅ |
| `feature/sessions` | Session-based search filter persistence (`SessionManager`) | amahcan562-ies | ✅ Merged |
| `feature/deals` | Full agreements flow — propose, accept, start, finish, cancel | fdomcas | ✅ Merged |
| `feature/statistics` | Moderator/admin statistics dashboard | jherhum1702 | ✅ Merged |
| `feature/api` | REST API with DRF + Swagger docs (drf-spectacular) | amahcan562-ies | ✅ Merged |
| `feature/sessions-model` | Session model, form, views, and templates | jherhum1702 / fdomcas | ✅ Merged |

**Bugfixes:**
| Branch | Bug Fixed | Author | PR |
|--------|-----------|--------|----|
| `bugfix/urls` | URL routing issues after profile merge | fdomcas | #59 ✅ |
| `bugfix/profile-base` | Profile page missing base template inheritance | jherhum1702 | #62 ✅ |
| `bugfix/docker-expose-port` | Docker port `8000:8000` not exposed correctly | amahcan562-ies | ✅ Merged |
| `bugfix/responsive-buttons-bug` | Mobile button alignment in dark mode | amahcan562-ies | ✅ Merged |

#### Integration Process
1. Branch created from the latest `develop`
2. Feature implemented locally with descriptive commits
3. Pushed to personal fork
4. Pull Request opened targeting upstream `develop`
5. Reviewed by at least one other team member
6. Merged after approval; branch deleted
7. All forks re-synced: `git fetch upstream && git rebase upstream/develop`

---

### 2. Issues and Task Distribution

GitHub Issues were used to track every unit of work:

- **Feature Requests** — new functionality to build
- **Bug Reports** — fixes required
- **Documentation** — README and inline doc updates

Issues were assigned based on each member's area of ownership. PRs referenced issues with `Closes #X` in the description, automatically closing them on merge.

**Responsibility matrix:**

| Team Member | Area | Key Deliverables |
|-------------|------|-----------------|
| **jherhum1702** | Backend / Data Layer | Models & migrations, ORM queries, populate command, home search, statistics view, profile template fix |
| **amahcan562-ies** | Infrastructure / Full Stack | Docker, env vars, cookies, session filters, anti-spam middleware, REST API + Swagger, documentation |
| **fdomcas** | Workflows / Security | Custom user model, groups & permissions, posts CRUD, agreements flow, session tracking, form validation, login by email |

---

### 3. Code Review Process

Each Pull Request was reviewed against this checklist:

- ✅ Django best practices followed (CBVs, forms, model methods)
- ✅ Migrations apply cleanly without errors
- ✅ No XSS vulnerabilities in templates (auto-escaping enforced)
- ✅ Access control verified (LoginRequiredMixin, permission mixins, IsAdminUser)
- ✅ No breaking changes to existing routes or models
- ✅ Code is readable, documented, and follows project conventions

**Review workflow:**
1. Author opens PR with a description and list of changes
2. At least one teammate reviews and leaves comments if needed
3. Author pushes fixes as additional commits
4. PR approved and merged to `develop`

**Example PR message (feature/cookies):**
```
feat(cookies): Dark mode preference

- Added context_processors.py — injects `theme` into every template
- Cookie set with max_age=365*24*60*60 (1 year)
- Navbar toggle for ☀️/🌙
- Dark mode CSS applied via body class

Testing: migrations apply, theme persists after logout, no JS errors
Closes #XX
```

---

### 4. Conflict Resolution

#### Conflict #1 — `feature/Perfil_usuario`
- **Problem**: Profile feature was merged (PR #56) but introduced bugs in the base template and URL routing.
- **Resolution**:
  - PR #58 reverted the merge to `develop`
  - Branch rebased against the updated `develop`
  - Bugs fixed and re-submitted as PR #61 → merged successfully
- **Lesson**: Always test locally against the latest `develop` before opening a PR.

#### Conflict #2 — `feature/sessions` vs `bugfix/responsive-buttons-bug`
- **Problem**: Both branches modified button styles inside `base.html` and template files simultaneously.
- **Resolution**:
  - `git fetch upstream && git rebase upstream/develop` on the lagging branch
  - Conflicts resolved manually in the editor; CSS rules unified
  - Tested on multiple screen sizes before re-pushing
- **Prevention**: The team agreed to communicate in advance when touching shared files like `base.html`.

#### Standard Resolution Commands
```bash
git fetch upstream
git rebase upstream/develop
# Resolve conflicts in your editor
git add .
git rebase --continue
git push origin <branch-name> --force-with-lease
```

---

### 5. Commit Convention

The team followed [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | Usage |
|--------|-------|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation only |
| `style:` | Formatting, no logic change |
| `refactor:` | Code restructuring |
| `chore:` | Build, config, or tooling change |

**Examples from the project:**
```
feat: context-processors implementation
feat: filter session implemented
feat: REST API with drf-spectacular swagger docs
feat: statistics view for moderators and admins
feat: agreements (deals) full lifecycle
feat: session model, views and templates
fix(docker): deleted double ports
fix: buttons separated and names in dark mode now appear
fix: profile base template inheritance
docs: complete README update
```

---

## 🗺️ Traceability Map

This section maps each technical requirement to the exact file(s) where it is implemented.

### Models & ORM

| Requirement | Implementation | File |
|-------------|---------------|------|
| Custom user model | `class Usuario(AbstractUser)` | `core/models.py` |
| Profile auto-created on registration | `@receiver(post_save, sender=Usuario)` signal | `core/models.py` |
| Many-to-many: profile ↔ skills | `habilidades = ManyToManyField(Habilidad, ...)` | `core/models.py` |
| Unique constraint on active agreements | `UniqueConstraint(..., condition=Q(estado__in=[...]))` | `core/models.py` |
| Model-level validation (`clean()`) | `Perfil.clean()`, `Acuerdo.clean()`, `Sesion.clean()` | `core/models.py` |
| Date validator (today or later) | `validate_date_today_or_later()` | `core/models.py` |
| Q objects for complex queries | `HomeView.get_queryset()` — combines BUSCO/OFREZCO terms | `core/views.py` |
| F expressions & annotations | `DealsDetailView.get_queryset()` — `total_mins = F('semanas') * F(...)` | `core/views.py` |
| `annotate` + `Count` | `PostDetailview.get_object()` — `total_proposals=Count(...)` | `core/views.py` |
| `select_related` + `prefetch_related` | `HomeView.get_queryset()` — `.select_related(...).prefetch_related(...)` | `core/views.py` |
| `Case` / `When` for custom ordering | `DealsListView.get_queryset()` — orders deals by status priority | `core/views.py` |
| Statistics aggregations | `StatisticsView.get_context_data()` — counts, filters, recent slices | `core/views.py` |

### Authentication & Permissions

| Requirement | Implementation | File |
|-------------|---------------|------|
| Custom registration form with email blocklist | `CustomUserCreationForm` + `clean_email()` | `core/forms.py` |
| Login by username **or** e-mail | `CustomloginForm.clean()` | `core/forms.py` |
| User assigned to `Usuario` group on register | `CustomRegisterView.form_valid()` | `core/views.py` |
| Ban/unban users from admin | `banear_usuarios`, `desbanear_usuarios` actions | `core/admin.py` |
| Banned user feedback on login | `CustomLogin.form_invalid()` — checks `is_active` | `core/views.py` |
| Login required for protected views | `LoginRequiredMixin` on all sensitive CBVs | `core/views.py` |
| Author or moderator only edit/delete | `AutorOModeradorMixin` | `core/views.py` |
| Agreement participants only | `AcuerdoUpdateParticipant.ParticipanteAcuerdoMixin` | `core/views.py` |
| Statistics restricted to moderators/admins | `ModeradorOAdminMixin` | `core/views.py` |
| Admin panel secured redirect | `secure_admin_login()` wrapper | `skillswap/urls.py` |

### Cookies & Sessions

| Requirement | Implementation | File |
|-------------|---------------|------|
| Theme preference stored in cookie | `change_preference` view — `response.set_cookie('theme', ...)` | `core/views.py` |
| Cookie injected into all templates | `preferences()` context processor | `core/context_processors.py` |
| Search filters persisted in session | `SessionManager.save_filters()` / `get_filters()` | `core/session_manager.py` |
| Filters restored on next visit | `HomeView.get_queryset()` — reads session if no GET param | `core/views.py` |
| Filters cleared on demand | `clear_filters` view + `SessionManager.clear_filters()` | `core/views.py`, `core/session_manager.py` |

### Forms & Validation

| Requirement | Implementation | File |
|-------------|---------------|------|
| Post creation — validate skill ownership for OFREZCO | `PostCreate.clean()` | `core/forms.py` |
| Agreement — validate participant has required skill | `DealsPost.clean()` | `core/forms.py` |
| Session — only creatable on `EN CURSO` agreements | `Sesion.clean()` | `core/models.py` |
| Session creation form (date, time, duration only) | `SesionCreateForm` | `core/forms.py` |
| Session edit form (summary + attendance after session ends) | `SesionEditForm` | `core/forms.py` |
| Profile skill update (free-text comma input) | `ProfileForm.save()` — `get_or_create` per comma-split token | `core/forms.py` |
| Duplicate agreement prevention | `IntegrityError` caught in `DealsCreateView.form_valid()` | `core/views.py` |

### Video Calls (Jitsi Meet)

| Requirement | Implementation | File |
|-------------|---------------|------|
| Unique Jitsi Meet room URL generation | `create_meet_link()` — UUID-based room name under self-hosted domain | `core/services/meet.py` |
| `meet_link` stored on the session model | `meet_link = models.URLField(blank=True, null=True)` | `core/models.py` |
| Link auto-generated on session creation | `SesionCreateView.form_valid()` — calls `create_meet_link()` and saves | `core/views.py` |
| Session status property (upcoming / ongoing / finished) | `Sesion.ha_finalizado` — compares `fecha + hora + duracion_real` against `now()` | `core/models.py` |
| Join button active only during session window | Template conditional on `session.ha_finalizado == 'ongoing'` | `core/templates/core/sesion_detail.html`, `sesioneslist.html` |
| Disabled join button before session starts | Template conditional on `session.ha_finalizado == 'upcoming'` | `core/templates/core/sesion_detail.html`, `sesioneslist.html` |
| Fill in summary & attendance after session | `SesionEditView` + `SesionEditForm` at `sessions/<pk>/edit/` | `core/views.py`, `core/forms.py` |

### Middleware

| Requirement | Implementation | File |
|-------------|---------------|------|
| Anti-spam: max 3 posts per 24 h per user | `SpamMiddleware.__call__()` | `core/middleware/anti_spam.py` |

### REST API

| Requirement | Implementation | File |
|-------------|---------------|------|
| ModelViewSet for all core models | `UsuarioViewSet`, `PublicacionViewSet`, `AcuerdoViewSet`, `SesionViewSet` | `core/views.py` |
| DRF serializers | `UsuarioSerializer`, `PublicacionSerializer`, `AcuerdoSerializer`, `SesionSerializer` | `core/serializers.py` |
| API restricted to admin users | `permission_classes = [IsAdminUser]` on all ViewSets | `core/views.py` |
| DRF router registration | `router.register(...)` × 4 + `path('api/', include(router.urls))` | `core/urls.py` |
| Swagger / OpenAPI auto-documentation | `SpectacularAPIView`, `SpectacularSwaggerView` at `/api/docs/` | `skillswap/urls.py` |
| API access secured by login redirect | `secure_api_view()` wrapper | `skillswap/urls.py` |

### Infrastructure & Configuration

| Requirement | Implementation | File |
|-------------|---------------|------|
| Docker multi-service setup | `docker-compose.yml` (web + db + optional tunnel profile) | `docker-compose.yml` |
| PostgreSQL configuration | `DATABASES` dict reading from `.env` | `skillswap/settings.py` |
| Environment-based settings | All secrets via `os.getenv()` + `python-dotenv` | `skillswap/settings.py` |
| Static files in production | `WhiteNoiseMiddleware` + `STATIC_ROOT` | `skillswap/settings.py` |
| Gunicorn WSGI server | `gunicorn skillswap.wsgi --bind 0.0.0.0:8000` | `docker-compose.yml` |
| Cloudflare Tunnel (optional) | `tunnel` service with `profiles: [production]` | `docker-compose.yml` |
| Idempotent test data seeder | `populate_test_data` command using `get_or_create` | `core/management/commands/populate_test_data.py` |


---

Made by José Antonio Hernández Humanes, Fabián Domínguez Casado and Andrés Mahindo Canalo.
