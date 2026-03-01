# SkillSwap

<div align="center">

![SkillSwap Logo](./staticfiles/imgs/logo.png)

**Una plataforma colaborativa para intercambiar habilidades y conocimiento.**

[Funcionalidades](#features) • [Pila tecnológica](#tech-stack) • [Instalación](#installation) • [Flujo](#workflow) • [License](#license)

</div>

---

## 📋 Table of Contents

- [Acerca de](#about)
- [Funcionalidades](#features)
- [Pila tecnológica](#tech-stack)
- [Instalación](#installation)
- [Configuración](#configuration)
- [Uso](#usage)
- [Estructura del proyecto](#project-structure)
- [Flujo](#workflow)
- [Contributing](#contributing)
- [Team](#team)
- [License](#license)

---

## 🎯 Acerca de

**SkillSwap** es una aplicación web que permite a los usuarios intercambiar habilidades y conocimientos con otros miembros de la comunidad. Ya sea que quieras aprender una nueva habilidad o enseñar algo que sabes, SkillSwap conecta personas con intereses compartidos y habilidades complementarias.

La plataforma permite a los usuarios:
- Crear publicaciones ofreciendo o solicitando habilidades específicas
- Buscar y filtrar habilidades y usuarios disponibles
- Gestionar el perfil del usuario con preferencias e intereses
- Mantener preferencias de búsqueda y filtros persistentes a través de cookies y sesiones
- Disfrutar de una experiencia perfecta en temas claros y oscuros

### 👥 Contribuciones del Equipo

Este proyecto fue desarrollado colaborativamente con clara separación de roles:

**Capa de Datos y ORM** (*jherhum1702*)
- Modelos de base de datos y relaciones con restricciones apropiadas
- Consultas ORM avanzadas usando objetos Q, expresiones F, anotaciones y agregaciones
- Optimización de consultas con `select_related()` y `prefetch_related()`
- Migraciones de base de datos y diseño de esquema
- Población de datos de prueba y fixtures

**Flujos y Seguridad** (*fdomcas*)
- Modelo de usuario personalizado con funcionalidad extendida
- Grupos de usuarios, permisos y reglas de control de acceso
- Flujo completo de publicación (creación, modificación, gestión de estado)
- Seguimiento de acuerdos y sistema de seguimiento
- Validación de formularios y medidas de seguridad
- Protección contra XSS y defensa CSRF

**Infraestructura y Documentación** (*amahcan562-ies*)
- Containerización con Docker y orquestación docker-compose
- Configuración y gestión de base de datos PostgreSQL
- Configuración de variables de entorno y gestión de secretos
- Preferencias de usuario basadas en cookies (tema, idioma)
- Persistencia de estado basada en sesiones (filtros de búsqueda)
- Implementación de middleware anti-spam
- Documentación completa del proyecto y README

---

Este proyecto fue desarrollado como parte de un curso educativo enfocado en prácticas profesionales de desarrollo web incluyendo control de versiones, flujos de trabajo colaborativos, diseño de bases de datos, seguridad y desarrollo full-stack con Django.

---

## ✨ Features

### Core Features
- 🔐 **User Authentication**: Secure registration and login system
- 💬 **Skill Exchange**: Create posts to offer or request skills
- 🔍 **Advanced Search & Filtering**: Search by skill type, category, and status with persistent filters
- 👤 **User Profiles**: Customizable user profiles with timezone support
- 🌍 **Internationalization**: Multi-language support (Spanish/English)
- 🎨 **Theme Support**: Light and dark mode with user preference cookies
- 📱 **Responsive Design**: Mobile-friendly interface using Bootstrap
- 🛡️ **Anti-Spam Protection**: Middleware to prevent spam attacks
- 💾 **Session Management**: Persistent filters and preferences

### Technical Features
- Docker containerization for consistent deployment
- PostgreSQL database with migrations
- Gunicorn WSGI server
- Static file management with WhiteNoise
- Cloudflare Tunnel integration for external access

---

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 6.0.2
- **Language**: Python 3.14
- **Database**: PostgreSQL 16
- **Server**: Gunicorn
- **Static Files**: WhiteNoise 6.7.0

### Frontend
- **HTML5** & **CSS3**
- **Bootstrap 5** (responsive components)
- **JavaScript** (vanilla, for theme/language switching)

### DevOps
- **Containerization**: Docker & Docker Compose
- **Tunneling**: Cloudflare Tunnel
- **Package Management**: pip, requirements.txt

### Development Tools
- **Version Control**: Git & GitHub
- **Email Validation**: disposable-email-domains

---

## 📦 Installation

### Prerequisites
Before you begin, ensure you have installed:
- **Docker** and **Docker Compose** (recommended for production)
- **Python 3.14+**
- **PostgreSQL 16+** (if running locally without Docker)
- **Git**

### 1. Clone the Repository

```bash
# Clone from your fork
git clone https://github.com/amahcan562-ies/skillswap-django.git
cd skillswap-django

# Add upstream remote (original repository)
git remote add upstream https://github.com/jherhum1702/skillswap-django.git
```

### 2. Create Environment File

Copy the example environment file and configure it:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```dotenv
# Database Configuration
DB_NAME=skillswap_db
DB_USER=django_user
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=5432

# Django Settings
SECRET_KEY=your_django_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000

# Cloudflare Tunnel (optional, for production)
TUNNEL_TOKEN=your_tunnel_token_here
```

**Generate a Django SECRET_KEY** if you don't have one:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 🐳 Setup with Docker (Recommended)

### Quick Start

```bash
# Start all services
docker compose up -d

# Stop services
docker compose down

# View logs
docker compose logs -f web
```

The application will be available at `http://localhost:8000`

The Docker setup automatically:
- Creates the PostgreSQL database
- Runs migrations
- Populates test data
- Collects static files
- Starts the Gunicorn server

### Database Commands

```bash
# Access database shell inside Docker
docker compose exec db psql -U django_user -d skillswap_db

# View Django logs
docker compose logs web -f
```

---

## 🖥️ Local Development Setup

### 1. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure PostgreSQL Locally

```bash
# On Linux/Mac
sudo -u postgres psql

# Create database
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

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 8. Run Development Server

```bash
python manage.py runserver 0.0.0.0:8000
```

Access the application at `http://localhost:8000`

---

## 📁 Project Structure

```
skillswap-django/
├── core/                          # Main Django app
│   ├── management/commands/       # Custom management commands
│   │   └── populate_test_data.py # Load initial test data
│   ├── middleware/               # Custom middleware
│   │   └── anti_spam.py         # SPAM protection middleware
│   ├── migrations/               # Database migrations
│   ├── static/                   # App-level static files
│   │   └── imgs/
│   ├── templates/                # App-level templates
│   │   └── core/
│   │       ├── home.html        # Home page
│   │       ├── post_list.html   # Posts listing
│   │       ├── post_detail.html # Post details
│   │       ├── profile.html     # User profile
│   │       └── search_results.html # Search results
│   ├── admin.py                 # Django admin configuration
│   ├── apps.py                  # App configuration
│   ├── context_processors.py    # Template context processors (cookies, preferences)
│   ├── forms.py                 # Django forms
│   ├── models.py                # Database models
│   ├── session_manager.py       # Session management for filters
│   ├── urls.py                  # App URL routing
│   └── views.py                 # View logic
│
├── skillswap/                    # Django project settings
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Project URL routing
│   ├── asgi.py                  # ASGI configuration
│   └── wsgi.py                  # WSGI configuration
│
├── templates/                    # Project-level templates
│   ├── base.html               # Base template with theme support
│   └── registration/           # Authentication templates
│       ├── login.html
│       └── registration.html
│
├── staticfiles/                  # Collected static files (production)
│   └── admin/                   # Django admin static files
│
├── Dockerfile                    # Docker image definition
├── docker-compose.yml           # Docker Compose configuration
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── gunicorn.ctl                # Gunicorn control script
└── README.md                    # This file
```

---

## ⚙️ Configuration

### Environment Variables
The `.env` file controls all environment-dependent settings:

| Variable | Purpose | Example |
|----------|---------|---------|
| `DB_NAME` | PostgreSQL database name | `skillswap_db` |
| `DB_USER` | PostgreSQL user | `django_user` |
| `DB_PASSWORD` | PostgreSQL password | `secure_password` |
| `DB_HOST` | Database host (localhost or Docker service) | `localhost` or `db` |
| `DEBUG` | Django debug mode | `True` (development only) |
| `SECRET_KEY` | Django secret key (keep secure!) | Generated value |
| `ALLOWED_HOSTS` | Allowed host domains | `localhost,127.0.0.1` |
| `CSRF_TRUSTED_ORIGINS` | CSRF-safe origins (must have scheme) | `http://localhost:8000` |
| `TUNNEL_TOKEN` | Cloudflare Tunnel token (optional) | Your token |

### Key Settings Files
- **`skillswap/settings.py`**: Main Django configuration
- **`skillswap/urls.py`**: Project-level URL routing
- **`core/urls.py`**: App-level URL routing and views
- **`.env.example`**: Template for environment variables (copy and customize)

---

## 🚀 Usage

### Default Credentials (Test Data)

After running `populate_test_data`:
- **Username**: testuser
- **Password**: testpass123

### Features Guide

#### 1. **Search and Filter**
- Use the search bar to find skills or users
- Filters persist in your session automatically
- Use the "Clear Filters" button to reset

#### 2. **Theme Switching**
- Click the theme toggle (☀️/🌙) in the navigation bar
- Your preference is saved as a cookie
- Preference persists across sessions

#### 3. **Language Selection**
- Click the language toggle (EN/ES) in the navigation bar
- Changes interface language dynamically
- Preference is saved as a cookie

#### 4. **Create a Post**
- Log in to your account
- Navigate to create a post
- Choose "BUSCO" (I'm looking for) or "OFREZCO" (I'm offering)
- Select a skill and provide details
- Your post will be visible to other users

#### 5. **User Profile**
- Visit your profile to view and edit information
- Set your timezone
- Manage your skills and interests

---

## 📊 Workflow

### Git Strategy Implementation

Our team implemented a **Git Flow workflow** with GitHub collaboration, organizing work through branches, issues, and pull requests.

---

### 1. Branches Used and Integration

#### Main Branches
- **`main`**: Production-ready code
- **`develop`**: Integration branch for features (staging)

#### Work Branches
All work was done in dedicated branches created from `develop`:

**Features Implemented:**
| Branch | Feature | Contributors | Status |
|--------|---------|---------------|--------|
| `feature/cookies` | Light/Dark theme & Language preferences (cookies) | amahcan562-ies | ✅ Merged (PR #51) |
| `feature/post_list` | Post listing and display | fdomcas | ✅ Merged (PR #50) |
| `feature/populate_db` | Database population script | jherhum1702 | ✅ Merged (PR #41) |
| `feature/home-page` | Home page with search | jherhum1702 | ✅ Merged (PR #53) |
| `feature/Perfil_usuario` | User profile management | fdomcas | ✅ Merged (PR #56, then reverted & re-implemented #61) |
| `feature/sessions` | Session-based filter persistence | amahcan562-ies | ✅ Merged |

**Bugfixes:**
| Branch | Bug Fixed | Contributors | Status |
|--------|-----------|---------------|--------|
| `bugfix/urls` | URL routing issues | fdomcas | ✅ Merged (PR #59) |
| `bugfix/profile-base` | Profile base template fixes | jherhum1702 | ✅ Merged (PR #62) |
| `bugfix/docker-expose-port` | Docker port exposure (8000:8000) | In progress | 🔄 Feature branch |
| `bugfix/responsive-buttons-bug` | Mobile responsive button alignment | In progress | 🔄 Feature branch |

#### Integration Process
1. Each feature/bugfix created a branch from `develop`
2. Work completed locally with multiple commits
3. Push to personal fork
4. Create Pull Request to upstream `develop` branch
5. After approval → merge into `develop`
6. Delete feature branch after merge
7. `develop` branch regularly synced with forks

---

### 2. Issues and Task Distribution

**How Issues Were Organized:**

We used GitHub Issues to track work with these types:
- **Feature Requests**: New functionality to build
- **Bug Reports**: Issues to fix
- **Documentation**: README and docs updates

**Task Distribution:**
| Team Member | Primary Responsibilities | Features/Bugfixes |
|-------------|--------------------------|-------------------|
| **jherhum1702** | Project Lead, Backend architecture, Models, Views | Populate DB, Home page, Profile base fixes, More data |
| **amahcan562-ies** | Full Stack: Frontend styling, Cookies, Sessions | Cookies/Theme/Lang, Session filters, Responsive buttons |
| **fdomcas** | Frontend & Database features | Post list, User profile, URL bugfixes |

**Work Distribution Method:**
- Issues were created in the GitHub repository
- Assigned to team members based on expertise
- Linked to Pull Requests with "Closes #X" comments
- Progress tracked through PR comments and status updates

---

### 3. Code Review Process

**Pull Request Review Checklist:**

Before merging, each PR was reviewed for:
- ✅ **Django Best Practices**: Models, views, forms follow conventions
- ✅ **Database Migrations**: No errors, migrations apply successfully
- ✅ **Template Safety**: No XSS vulnerabilities, proper template usage
- ✅ **Code Quality**: Meaningful variable names, documentation
- ✅ **Functionality**: Feature works as described in PR
- ✅ **No Breaking Changes**: Backward compatibility maintained

**Review Workflow:**
1. Author creates PR with description, key changes, and testing checklist
2. Team members review code and suggest improvements
3. Author addresses feedback with additional commits
4. Approvers verify changes and approve
5. PR is merged to develop once approved

**Example PR (Feature/Cookies):**
```
Title: feat(cookies): Dark mode and language preferences
Description: Implemented cookie-based theme and language preferences
Key Changes:
- Added context_processors.py for template variables
- Created theme toggle and language toggle buttons
- Implemented CSS for dark mode
Testing: Migrations apply without errors, theme persists across sessions
Related Issues: Closes #X
```

---

### 4. Conflict Resolution

**Conflicts Encountered and Resolution:**

#### Conflict #1: Feature/Perfil_usuario
- **Issue**: Profile feature merged, then reverted due to bugs, then re-implemented
- **Solution**: 
  - First merge (PR #56) → Reverted (PR #58)
  - Fixed conflicts by rebasing with develop
  - Re-implemented with fixes (PR #61) → Successfully merged
- **Lesson**: Better testing before merging

#### Conflict #2: Feature/Sessions vs Bugfix/buttons
- **Issue**: Two branches modifying button styling simultaneously
- **Solution**:
  - Used `git rebase upstream/develop` to sync latest changes
  - Manually resolved CSS conflicts in templates
  - Tested responsive design thoroughly
- **Prevention**: Improved communication about which files each person modifies

#### Resolution Strategy Used:
```bash
# When conflicts occurred:
1. git fetch upstream
2. git rebase upstream/develop
3. # Resolve conflicts manually in editor
4. git add .
5. git rebase --continue
6. git push origin branch-name -f
```

**Conflict Markers Handled:**
- Template conflicts in `base.html`
- CSS styling conflicts in buttons
- URL routing conflicts in `urls.py`

**Prevention Measures:**
- Team communicated about areas being modified
- Small, focused branches to minimize overlap
- Frequent pulls from upstream develop
- Regular merges to avoid large divergences

---

### 5. Communication & Coordination

**Tools Used:**
- **GitHub Issues**: Feature/bug tracking and assignment
- **Pull Requests**: Code review and discussion
- **Commits**: Descriptive messages following conventional commits
  - `feat:` for features
  - `fix:` for bugfixes
  - `docs:` for documentation
  - `style:` for formatting

**Example Commits:**
```
- feat: context-processors implementation
- fix(docker): deleted double ports
- feat: filter session implemented
- fix: buttons separated and names in dark mode now appear
```

---

## 👥 Team

This project was developed collaboratively by:
- **jherhum1702** - Project Lead & Backend
- **amahcan562-ies** - Full Stack (Cookies, Sessions, Filters)
- **fdomcas** - Frontend & Features (Profile, Posts)
- **Other Contributors** - See commit history

---

## 📝 License

This project is licensed under the **MIT License** - see below for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---


## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/en/6.0/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Git Workflow Guide](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

## ❓ FAQ

**Q: How do I run the project locally without Docker?**
A: Follow the "Local Development Setup" section above. You'll need PostgreSQL installed locally.

**Q: How do I reset the database?**
A: 
```bash
# With Docker
docker compose down -v  # -v removes volumes
docker compose up -d

# Locally
python manage.py migrate zero  # Reverse all migrations
python manage.py migrate       # Re-apply migrations
```

**Q: How do I add a new dependency?**
A: 
```bash
pip install new-package
pip freeze > requirements.txt
git add requirements.txt
git commit -m "deps: add new-package"
```

**Q: How do I run Django commands in Docker?**
A:
```bash
docker compose exec web python manage.py [command]
```

---

**Last Updated**: February 27, 2026
**Status**: In Active Development 🚀

