# SkillSwap

<div align="center">

![SkillSwap Logo](./staticfiles/imgs/logo.png)

**A collaborative platform for exchanging skills and knowledge**

</div>

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Workflow](#workflow)
- [Development Team](#development-team)

---

## 🎯 About

**SkillSwap** is a web application that allows users to exchange skills and knowledge with other members of the community. Whether you want to learn a new skill or teach something you know, SkillSwap connects people with shared interests and complementary abilities.

The platform enables users to:
- Create posts offering or requesting specific skills
- Search and filter available skills and users
- Manage their user profile with preferences and interests
- Reach agreements for skill exchange and track their status
- Maintain persistent search preferences and filters across cookies & sessions

### 👥 Team Roles

This project was developed collaboratively with clear role separation:

**Data & ORM Layer** (*José Antonio Hernández Humanes*)
- Models, relations, restrictions, and migrations
- Functionalities that require Q/F/annotate/aggregate and optimization with select/prefetch
- Middleware for SPAM protection and session management

**Workflows & Security** (*Fabián Domínguez Casado*)
- Custom user model, group permissions, and access rules.
- Flows for creating posts, agreements, follow up and form validation.

**Infrastructure & Documentation** (*Andrés Mahindo Canalo*)
- Docker containerization, PostgreSQL setup, and environment variables.
- Cookie-based user preferences and Session-based state persistence.
- Complete project documentation and traceability map.

---

## ✨ Features

### Core Features
- 🔐 **User Authentication**: Secure registration and login system
- 💬 **Skill Exchange**: Create posts to offer or request skills
- 🔍 **Filtering**: Filter by skill name and user preference
- 👤 **User Profiles**: Customizable user profiles with habilities and timezone setting
- 🎨 **Customization**: Cookie based theme and language preferences
- 🤝 **Agreements**: Section to manage skill exchange agreements and their status
- 🛡️ **Anti-Spam Protection**: Middleware to prevent spam attacks
- 💾 **Session Management**: Persistent filters and preferences


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

## 👥 Development Team

This project was developed collaboratively by:
- **José Antonio Hernández Humanes**
- **Fabián Domínguez Casado** 
- **Andrés Mahindo Canalo** 

---


## 📚  Resources

- [Django Documentation](https://docs.djangoproject.com/en/6.0/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Git Workflow Guide](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows)
- [Conventional Commits](https://www.conventionalcommits.org/)



