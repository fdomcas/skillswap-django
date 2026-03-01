# SkillSwap

<div align="center">

![SkillSwap Logo](./staticfiles/imgs/logo.png)

**Una plataforma colaborativa para intercambiar habilidades y conocimiento**

</div>

---

## 📋 Tabla de contenidos

- [Acerca de](#-acerca-de)
- [Funcionalidades](#-funcionalidades)
- [Pila tecnológica](#️-pila-tecnológica)
- [Instalación](#-instalación)
- [Configuración](#️-configuración)
- [Uso](#-uso)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Flujo de trabajo](#-flujo-de-trabajo)
- [Mapa de trazabilidad](#️-mapa-de-trazabilidad)

---

## 🎯 Acerca de

**SkillSwap** es una aplicación web que permite a los usuarios intercambiar habilidades y conocimientos con otros miembros de la comunidad. Ya sea que quieras aprender una nueva habilidad o enseñar algo que sabes, SkillSwap conecta personas con intereses compartidos y habilidades complementarias.

La plataforma permite a los usuarios:
- Crear publicaciones ofreciendo o solicitando habilidades específicas
- Buscar y filtrar publicaciones disponibles con filtros persistentes basados en sesión
- Gestionar un perfil de usuario personalizable con habilidades, biografía, zona horaria y disponibilidad
- Proponer, aceptar y gestionar acuerdos de intercambio de habilidades con ciclo de vida completo
- Programar y realizar un seguimiento de las sesiones dentro de cada acuerdo
- Mantener preferencias de tema (claro/oscuro) mediante cookies (establecidas vía formularios POST)
- Acceder a una API REST (restringida a administradores) para todos los recursos principales


---

## ✨ Funcionalidades

### Funcionalidades principales
- 🔐 **Autenticación de usuarios** — Registro e inicio de sesión seguros con soporte de nombre de usuario *o* correo electrónico, con bloqueo de dominios de email desechables
- 🚫 **Baneo de cuentas** — Los administradores pueden banear/desbanear usuarios; los baneados ven un mensaje de error claro al iniciar sesión
- 💬 **Publicaciones de habilidades** — Crea publicaciones de tipo *OFREZCO* o *BUSCO*, cada una vinculada a una habilidad específica
- 🔍 **Búsqueda y filtrado inteligente** — Búsqueda en lenguaje natural con consultas como `busco python`, `ofrezco django y busco react`, etc.
- 💾 **Filtros persistentes** — El estado de búsqueda se guarda en la sesión y se restaura en la siguiente visita; se limpia con un clic
- 👤 **Perfiles de usuario** — Biografía, zona horaria, disponibilidad y lista de habilidades personales; el perfil se crea automáticamente al registrarse mediante una señal de Django
- 🤝 **Acuerdos** — Propón un acuerdo de intercambio directamente desde el detalle de una publicación con semanas, duración de sesión y condiciones configurables; ciclo de vida completo: `PROPUESTO → ACEPTADO → EN CURSO → FINALIZADO / CANCELADO`
- 📅 **Sesiones** — Programa sesiones vinculadas a un acuerdo en curso con fecha y hora específicas; se genera automáticamente un enlace de videollamada Jitsi Meet al crear la sesión, que solo se activa durante la ventana temporal de la sesión; el resumen y la asistencia se rellenan después
- 📊 **Panel de estadísticas** — Restringido a moderadores y administradores; métricas agregadas sobre publicaciones, acuerdos, sesiones y usuarios
- 🎨 **Cambio de tema** — Alternancia entre modo claro/oscuro guardada en una cookie (validez de 1 año)
- 🛡️ **Middleware anti-spam** — Bloquea más de 3 creaciones de publicaciones por usuario en 24 horas
- 🔌 **API REST** — Endpoints CRUD completos para `Usuario`, `Publicacion`, `Acuerdo` y `Sesion`; restringidos a administradores; documentados automáticamente con Swagger UI en `/api/docs/`

---

## 🛠️ Pila tecnológica

### Backend
| Componente | Tecnología |
|-----------|------------|
| Framework | Django 6.0.2 |
| Lenguaje | Python 3.14 |
| Base de datos | PostgreSQL 16 |
| Servidor WSGI | Gunicorn |
| Archivos estáticos | WhiteNoise 6.7.0 |
| API REST | Django REST Framework ≥ 3.14 |
| Docs API | drf-spectacular ≥ 0.27 |
| Validación de email | disposable-email-domains |
| Variables de entorno | python-dotenv ≥ 1.0 |
| Videollamadas | Jitsi Meet (servidor propio) |

### Frontend
- **HTML5** y **CSS3**
- **Bootstrap 5** (rejilla responsiva, modales y componentes)
- **JavaScript (Vanilla)** — filtrado dinámico de habilidades, notificaciones toast, modales Bootstrap, navegación por historial

### DevOps
- **Docker** y **Docker Compose**
- **Cloudflare Tunnel** (opcional, solo producción)
- **pip** / `requirements.txt`

---

## 📦 Instalación

### Requisitos previos
- **Docker** y **Docker Compose** — recomendado para el inicio más rápido
- **Python 3.14+** y **PostgreSQL 16+** — si se ejecuta localmente sin Docker
- **Git**

### 1. Clonar el repositorio

```bash
git clone https://github.com/amahcan562-ies/skillswap-django.git
cd skillswap-django

# Añadir el remote upstream (repositorio original)
git remote add upstream https://github.com/jherhum1702/skillswap-django.git
```

### 2. Crear el archivo de entorno

```bash
cp .env.example .env
```

Edita `.env` con tus valores:

```dotenv
# Base de datos
DB_NAME=skillswap_db
DB_USER=django_user
DB_PASSWORD=tu_contraseña_segura
DB_HOST=localhost        # usa "db" al ejecutar con Docker
DB_PORT=5432

# Django
SECRET_KEY=tu_clave_secreta_django
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000

# Cloudflare Tunnel (opcional — solo producción)
TUNNEL_TOKEN=tu_token_aqui
```

Genera una `SECRET_KEY` si no tienes una:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 🐳 Configuración con Docker (Recomendado)

```bash
# Iniciar todos los servicios (web + PostgreSQL)
docker compose up -d

# Ver logs
docker compose logs -f web

# Detener servicios
docker compose down
```

La aplicación estará disponible en **http://localhost:8000**.

Docker automáticamente:
1. Aplica todas las migraciones (`python manage.py migrate`)
2. Pobla los datos de prueba (`python manage.py populate_test_data`)
3. Recopila archivos estáticos
4. Inicia Gunicorn en el puerto 8000

**Comandos Docker útiles:**

```bash
# Acceder al shell de la base de datos
docker compose exec db psql -U django_user -d skillswap_db

# Ejecutar cualquier comando de gestión de Django
docker compose exec web python manage.py <comando>

# Reinicio completo (elimina el volumen de la base de datos)
docker compose down -v && docker compose up -d
```

---

## 🖥️ Configuración de desarrollo local

### 1. Crear un entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar PostgreSQL

```sql
-- Conectarse como superusuario de postgres
sudo -u postgres psql

CREATE DATABASE skillswap_db;
CREATE USER django_user WITH PASSWORD 'tu_contraseña';
ALTER ROLE django_user SET client_encoding TO 'utf8';
ALTER ROLE django_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE django_user SET default_transaction_deferrable TO on;
ALTER ROLE django_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE skillswap_db TO django_user;
\q
```

### 4. Ejecutar migraciones

```bash
python manage.py migrate
```

### 5. Cargar datos de prueba (opcional)

```bash
python manage.py populate_test_data
```

### 6. Crear un superusuario

```bash
python manage.py createsuperuser
```

> Un superusuario es necesario para acceder a **`/admin/`** y a los endpoints de la API REST en **`/api/`**.

### 7. Recopilar archivos estáticos

```bash
python manage.py collectstatic --noinput
```

### 8. Iniciar el servidor de desarrollo

```bash
python manage.py runserver 0.0.0.0:8000
```

Visita **http://localhost:8000**.

---

## ⚙️ Configuración

### Variables de entorno

| Variable | Propósito | Ejemplo |
|----------|-----------|---------|
| `DB_NAME` | Nombre de la base de datos PostgreSQL | `skillswap_db` |
| `DB_USER` | Usuario de PostgreSQL | `django_user` |
| `DB_PASSWORD` | Contraseña de PostgreSQL | `contraseña_segura` |
| `DB_HOST` | Host de la base de datos | `localhost` / `db` (Docker) |
| `DB_PORT` | Puerto de la base de datos | `5432` |
| `DEBUG` | Modo debug de Django | `True` (solo desarrollo) |
| `SECRET_KEY` | Clave secreta de Django | Valor generado |
| `ALLOWED_HOSTS` | Hosts permitidos separados por comas | `localhost,127.0.0.1` |
| `CSRF_TRUSTED_ORIGINS` | Orígenes CSRF seguros (con esquema) | `http://localhost:8000` |
| `TUNNEL_TOKEN` | Token de Cloudflare Tunnel | Tu token |

### Archivos clave

| Archivo | Propósito |
|---------|-----------|
| `skillswap/settings.py` | Configuración principal de Django |
| `skillswap/urls.py` | Enrutamiento URL del proyecto + rutas de docs API |
| `core/urls.py` | Enrutamiento URL de la app y router DRF |
| `core/context_processors.py` | Preferencias de cookies inyectadas en todas las plantillas |
| `core/session_manager.py` | Helpers de filtros de búsqueda basados en sesión |
| `core/middleware/anti_spam.py` | Middleware de protección contra spam |
| `core/serializers.py` | Serializadores DRF para la API REST |
| `core/services/meet.py` | Generación de enlaces de videollamada Jitsi Meet |
| `.env` | Variables de entorno locales (nunca confirmar en git) |

---

## 🚀 Uso

### Credenciales de prueba

Tras ejecutar `populate_test_data`, hay **20 usuarios de prueba** disponibles. Todos tienen la contraseña **`1234`**. Algunos destacados:

| Usuario | Nombre | Descripción |
|---------|--------|-------------|
| `pacogamer30` | Paco Tester | Aprendiz de programación y gaming |
| `anadev` | Ana López | Desarrolladora frontend |
| `laurasan` | Laura Sánchez | Profesora de inglés aprendiendo programación |
| `carlosdev` | Carlos Ruiz | Desarrollador backend (Django / Docker) |
| `sofiahm` | Sofía Hernández | Diseñadora UX/UI |

> Para acceder a **`/admin/`** o a la **API REST**, necesitas un superusuario creado con `python manage.py createsuperuser`.

### Guía de funcionalidades

#### Búsqueda y filtros
- Escribe cualquier nombre de habilidad en la barra de búsqueda de la página principal
- Usa prefijos para búsquedas más precisas:
  - `busco python` → publicaciones BUSCO sobre Python
  - `ofrezco django` → publicaciones OFREZCO sobre Django
  - `busco react y ofrezco javascript` → filtro combinado
- Los filtros se guardan en tu sesión y se restauran en la siguiente visita
- Haz clic en **"Limpiar filtros"** para reiniciar

#### Acuerdos
1. Abre el detalle de cualquier publicación (`/posts/<id>`)
2. Haz clic en **"Proponer acuerdo"** para abrir el formulario de creación
3. Configura las semanas, la duración de sesión, las sesiones por semana y las condiciones
4. El autor de la publicación recibe la propuesta y puede **Aceptarla**
5. Una vez aceptado, cualquier participante puede **Iniciar** el acuerdo (→ `EN CURSO`)
6. Desde el detalle del acuerdo, los participantes pueden **crear sesiones**, **finalizar** o **cancelar** el acuerdo

#### Sesiones
- Las sesiones solo se pueden crear mientras el acuerdo está `EN CURSO`
- Al crear una sesión, establece la **fecha**, la **hora** y la **duración prevista** (60–240 min)
- Se genera automáticamente un **enlace de videollamada Jitsi Meet** y se guarda en la sesión al crearla
- El botón de unirse se activa únicamente durante la ventana temporal de la sesión (entre la hora de inicio y la de fin); antes aparece deshabilitado
- Una vez finalizada la sesión, cualquier participante puede rellenar el **resumen y la asistencia** mediante el formulario de edición
- Todas tus sesiones aparecen listadas en `/sessions/`

#### Tema
- Usa el botón **☀️/🌙** en la barra de navegación para alternar entre modo claro y oscuro
- La preferencia de tema se guarda en una cookie con validez de 1 año

#### Estadísticas (Moderadores / Administradores)
- Visita `/statistics/` — solo accesible para staff y usuarios del grupo `Moderador`
- Muestra recuento de publicaciones, estados de acuerdos, totales de sesiones, actividad reciente y la lista de moderadores

#### API REST (solo administradores)
- **URL base**: `/api/`
- **Recursos**: `usuarios`, `publicaciones`, `acuerdos`, `sesiones`
- **Docs interactivas (Swagger UI)**: `/api/docs/`
- **Esquema OpenAPI**: `/api/schema/`

---

## 📁 Estructura del proyecto

```
skillswap-django/
├── core/                            # Aplicación principal de Django
│   ├── management/commands/
│   │   └── populate_test_data.py   # Poblador de BD idempotente (20 usuarios, 36 habilidades, publicaciones, acuerdos, sesiones)
│   ├── middleware/
│   │   └── anti_spam.py            # Limita la creación de publicaciones a 3 por usuario cada 24 h
│   ├── services/
│   │   └── meet.py                 # Genera URLs únicas de sala Jitsi Meet (basadas en UUID)
│   ├── migrations/                  # Migraciones de base de datos
│   ├── static/imgs/                 # Archivos estáticos de la app
│   ├── templates/core/
│   │   ├── home.html               # Página principal con búsqueda
│   │   ├── search_results.html     # Resultados de búsqueda
│   │   ├── post_list.html          # Listado de todas las publicaciones
│   │   ├── post_detail.html        # Detalle de publicación + botón de proponer acuerdo
│   │   ├── postCreate.html         # Formulario de creación de publicación
│   │   ├── post_update.html        # Formulario de edición de publicación
│   │   ├── profile.html            # Vista del perfil de usuario
│   │   ├── profile_update.html     # Formulario de edición del perfil
│   │   ├── dealsCreate.html        # Formulario de propuesta de acuerdo
│   │   ├── dealslist.html          # Lista de acuerdos del usuario
│   │   ├── dealsDetail.html        # Detalle del acuerdo + creación de sesión
│   │   ├── sesioneslist.html       # Lista de sesiones del usuario (con botón Unirse en directo)
│   │   ├── sesionCreate.html       # Formulario de creación de sesión (fecha, hora, duración)
│   │   ├── sesion_detail.html      # Detalle de sesión con enlace Jitsi + asistencia
│   │   ├── sesion_edit.html        # Editar sesión tras finalizarla (resumen + asistencia)
│   │   └── statistics.html         # Panel de estadísticas para administradores/moderadores
│   ├── admin.py                    # Admin de Django (acciones de ban/desban)
│   ├── apps.py
│   ├── context_processors.py       # Lee cookie de tema → contexto de plantilla
│   ├── forms.py                    # Todos los formularios Django con lógica de validación
│   ├── models.py                   # Habilidad, Usuario, Perfil, Publicacion, Acuerdo, Sesion
│   ├── serializers.py              # Serializadores DRF
│   ├── session_manager.py          # Guardar/obtener/limpiar filtros de búsqueda en sesión
│   ├── urls.py                     # Todas las rutas de la app + router DRF
│   └── views.py                    # Todos los CBVs, FBVs y ViewSets DRF
│
├── skillswap/
│   ├── settings.py                 # Configuración del proyecto (basada en variables de entorno)
│   ├── urls.py                     # URL conf raíz + rutas de docs API
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── base.html                   # Plantilla base con tema, navbar y mensajes
│   └── registration/
│       ├── login.html
│       └── registration.html
│
├── staticfiles/                     # Archivos estáticos recopilados (producción)
├── locale/                          # Archivos de traducción i18n (es, en)
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── gunicorn.ctl
```

---

## 📊 Flujo de trabajo

### Estrategia Git

El equipo usó un flujo de trabajo inspirado en **Git Flow** con tres colaboradores trabajando en tres forks e integrando a través de un repositorio upstream compartido.

---

### 1. Estructura de ramas e integración

#### Ramas principales
| Rama | Propósito |
|------|-----------|
| `main` | Código estable y listo para producción |
| `develop` | Rama de integración — todas las funcionalidades se fusionan aquí primero |

#### Ramas de funcionalidades y correcciones
Todo el trabajo se realizó en ramas dedicadas creadas desde `develop` y fusionadas de vuelta mediante Pull Request.

**Funcionalidades:**
| Rama | Funcionalidad | Autor | PR |
|------|--------------|-------|----|
| `feature/cookies` | Preferencias de tema claro/oscuro e idioma (cookies + context processor) | amahcan562-ies | #51 ✅ |
| `feature/post_list` | Vista y plantilla de listado de publicaciones | fdomcas | #50 ✅ |
| `feature/populate_db` | Comando de gestión para poblar la base de datos | jherhum1702 | #41 ✅ |
| `feature/home-page` | Página principal con búsqueda inteligente (objetos Q) | jherhum1702 | #53 ✅ |
| `feature/Perfil_usuario` | Vista y edición del perfil de usuario | fdomcas | #56 → revertido #58 → reimplementado #61 ✅ |
| `feature/sessions` | Persistencia de filtros de búsqueda en sesión (`SessionManager`) | amahcan562-ies | ✅ Fusionado |
| `feature/deals` | Flujo completo de acuerdos — proponer, aceptar, iniciar, finalizar, cancelar | fdomcas | ✅ Fusionado |
| `feature/statistics` | Panel de estadísticas para moderadores/administradores | jherhum1702 | ✅ Fusionado |
| `feature/api` | API REST con DRF + documentación Swagger (drf-spectacular) | amahcan562-ies | ✅ Fusionado |
| `feature/sessions-model` | Modelo de sesión, formulario, vistas y plantillas | jherhum1702 / fdomcas | ✅ Fusionado |
| `feature/jitsi-meet` | Integración de videollamadas Jitsi Meet en sesiones | amahcan562-ies | ✅ Fusionado |

**Correcciones:**
| Rama | Error corregido | Autor | PR |
|------|----------------|-------|----|
| `bugfix/urls` | Problemas de enrutamiento de URLs tras la fusión del perfil | fdomcas | #59 ✅ |
| `bugfix/profile-base` | Página de perfil sin herencia de plantilla base | jherhum1702 | #62 ✅ |
| `bugfix/docker-expose-port` | Puerto Docker `8000:8000` no expuesto correctamente | amahcan562-ies | ✅ Fusionado |
| `bugfix/responsive-buttons-bug` | Alineación de botones en móvil en modo oscuro | amahcan562-ies | ✅ Fusionado |

#### Proceso de integración
1. Rama creada desde el último `develop`
2. Funcionalidad implementada localmente con commits descriptivos
3. Push al fork personal
4. Pull Request abierto hacia `develop` del upstream
5. Revisado por al menos otro miembro del equipo
6. Fusionado tras aprobación; rama eliminada
7. Todos los forks resincronizados: `git fetch upstream && git rebase upstream/develop`

---

### 2. Issues y distribución de tareas

Se usaron GitHub Issues para rastrear cada unidad de trabajo:

- **Feature Requests** — nuevas funcionalidades a construir
- **Bug Reports** — correcciones requeridas
- **Documentation** — actualizaciones de README y documentación inline

Los issues se asignaron según el área de responsabilidad de cada miembro. Los PRs referenciaban los issues con `Closes #X` en la descripción, cerrándolos automáticamente al fusionar.

**Matriz de responsabilidades:**

| Miembro | Área | Entregas principales |
|---------|------|---------------------|
| **jherhum1702** | Backend / Capa de datos | Modelos y migraciones, consultas ORM, comando populate, búsqueda en home, vista de estadísticas, corrección plantilla de perfil |
| **amahcan562-ies** | Infraestructura / Full Stack | Docker, variables de entorno, cookies, filtros de sesión, middleware anti-spam, API REST + Swagger, videollamadas Jitsi Meet, documentación |
| **fdomcas** | Flujos / Seguridad | Modelo de usuario personalizado, grupos y permisos, CRUD de publicaciones, flujo de acuerdos, seguimiento de sesiones, validación de formularios, login por email |

---

### 3. Proceso de revisión de código

Cada Pull Request fue revisado contra esta lista de comprobación:

- ✅ Buenas prácticas de Django seguidas (CBVs, formularios, métodos de modelo)
- ✅ Las migraciones se aplican sin errores
- ✅ Sin vulnerabilidades XSS en plantillas (auto-escape aplicado)
- ✅ Control de acceso verificado (LoginRequiredMixin, mixins de permisos, IsAdminUser)
- ✅ Sin cambios que rompan rutas o modelos existentes
- ✅ Código legible, documentado y que sigue las convenciones del proyecto

**Flujo de revisión:**
1. El autor abre un PR con una descripción y lista de cambios
2. Al menos un compañero revisa y deja comentarios si es necesario
3. El autor sube correcciones como commits adicionales
4. PR aprobado y fusionado a `develop`

**Ejemplo de mensaje de PR (feature/cookies):**
```
feat(cookies): Modo oscuro

- Añadido context_processors.py — inyecta `theme` en todas las plantillas
- Cookie con max_age=365*24*60*60 (1 año)
- Botón en navbar para ☀️/🌙
- CSS del modo oscuro aplicado mediante clase del body

Pruebas: migraciones aplicadas, tema persiste tras cerrar sesión, sin errores JS
Closes #XX
```

---

### 4. Resolución de conflictos

#### Conflicto #1 — `feature/Perfil_usuario`
- **Problema**: La funcionalidad del perfil se fusionó (PR #56) pero introdujo errores en la plantilla base y el enrutamiento de URLs.
- **Resolución**:
  - PR #58 revirtió la fusión a `develop`
  - La rama se rebaseó contra el `develop` actualizado
  - Los errores se corrigieron y se volvió a enviar como PR #61 → fusionado con éxito
- **Lección**: Siempre probar localmente contra el último `develop` antes de abrir un PR.

#### Conflicto #2 — `feature/sessions` vs `bugfix/responsive-buttons-bug`
- **Problema**: Ambas ramas modificaban estilos de botones en `base.html` y archivos de plantillas simultáneamente.
- **Resolución**:
  - `git fetch upstream && git rebase upstream/develop` en la rama desactualizada
  - Conflictos resueltos manualmente en el editor; reglas CSS unificadas
  - Probado en múltiples tamaños de pantalla antes de volver a hacer push
- **Prevención**: El equipo acordó comunicarse con antelación al tocar archivos compartidos como `base.html`.

#### Comandos estándar de resolución
```bash
git fetch upstream
git rebase upstream/develop
# Resuelve los conflictos en tu editor
git add .
git rebase --continue
git push origin <nombre-rama> --force-with-lease
```

---

### 5. Convención de commits

El equipo siguió [Conventional Commits](https://www.conventionalcommits.org/):

| Prefijo | Uso |
|---------|-----|
| `feat:` | Nueva funcionalidad |
| `fix:` | Corrección de errores |
| `docs:` | Solo documentación |
| `style:` | Formato, sin cambio de lógica |
| `refactor:` | Reestructuración de código |
| `chore:` | Cambios de build, config o herramientas |

**Ejemplos del proyecto:**
```
feat: context-processors implementation
feat: filter session implemented
feat: REST API with drf-spectacular swagger docs
feat: statistics view for moderators and admins
feat: agreements (deals) full lifecycle
feat: session model, views and templates
feat: jitsi meet integration for sessions
fix(docker): deleted double ports
fix: buttons separated and names in dark mode now appear
fix: profile base template inheritance
docs: complete README update
```

---

## 🗺️ Mapa de trazabilidad

Esta sección mapea cada requisito técnico al archivo exacto donde está implementado.

### Modelos y ORM

| Requisito | Implementación | Archivo |
|-----------|---------------|---------|
| Modelo de usuario personalizado | `class Usuario(AbstractUser)` | `core/models.py` |
| Perfil creado automáticamente al registrarse | Señal `@receiver(post_save, sender=Usuario)` | `core/models.py` |
| Many-to-many: perfil ↔ habilidades | `habilidades = ManyToManyField(Habilidad, ...)` | `core/models.py` |
| Restricción única en acuerdos activos | `UniqueConstraint(..., condition=Q(estado__in=[...]))` | `core/models.py` |
| Validación a nivel de modelo (`clean()`) | `Perfil.clean()`, `Acuerdo.clean()`, `Sesion.clean()` | `core/models.py` |
| Validador de fecha (hoy o posterior) | `validate_date_today_or_later()` | `core/models.py` |
| Objetos Q para consultas complejas | `HomeView.get_queryset()` — combina términos BUSCO/OFREZCO | `core/views.py` |
| Expresiones F y anotaciones | `DealsDetailView.get_queryset()` — `total_mins = F('semanas') * F(...)` | `core/views.py` |
| `annotate` + `Count` | `PostDetailview.get_object()` — `total_proposals=Count(...)` | `core/views.py` |
| `select_related` + `prefetch_related` | `HomeView.get_queryset()` — `.select_related(...).prefetch_related(...)` | `core/views.py` |
| `Case` / `When` para orden personalizado | `DealsListView.get_queryset()` — ordena acuerdos por prioridad de estado | `core/views.py` |
| Agregaciones para estadísticas | `StatisticsView.get_context_data()` — conteos, filtros, fragmentos recientes | `core/views.py` |

### Autenticación y permisos

| Requisito | Implementación | Archivo |
|-----------|---------------|---------|
| Formulario de registro con bloqueo de emails desechables | `CustomUserCreationForm` + `clean_email()` | `core/forms.py` |
| Login por nombre de usuario **o** email | `CustomloginForm.clean()` | `core/forms.py` |
| Usuario asignado al grupo `Usuario` al registrarse | `CustomRegisterView.form_valid()` | `core/views.py` |
| Banear/desbanear usuarios desde el admin | Acciones `banear_usuarios`, `desbanear_usuarios` | `core/admin.py` |
| Feedback al usuario baneado en el login | `CustomLogin.form_invalid()` — comprueba `is_active` | `core/views.py` |
| Login requerido en vistas protegidas | `LoginRequiredMixin` en todos los CBVs sensibles | `core/views.py` |
| Solo autor o moderador puede editar/eliminar | `AutorOModeradorMixin` | `core/views.py` |
| Solo participantes del acuerdo | `AcuerdoUpdateParticipant.ParticipanteAcuerdoMixin` | `core/views.py` |
| Estadísticas restringidas a moderadores/admins | `ModeradorOAdminMixin` | `core/views.py` |
| Panel de admin con redirección segura | Wrapper `secure_admin_login()` | `skillswap/urls.py` |

### Cookies y sesiones

| Requisito | Implementación | Archivo |
|-----------|---------------|---------|
| Preferencia de tema guardada en cookie | Vista `change_preference` — `response.set_cookie('theme', ...)` | `core/views.py` |
| Cookies inyectadas en todas las plantillas | Context processor `preferences()` | `core/context_processors.py` |
| Filtros de búsqueda persistidos en sesión | `SessionManager.save_filters()` / `get_filters()` | `core/session_manager.py` |
| Filtros restaurados en la siguiente visita | `HomeView.get_queryset()` — lee la sesión si no hay parámetro GET | `core/views.py` |
| Filtros limpiados bajo demanda | Vista `clear_filters` + `SessionManager.clear_filters()` | `core/views.py`, `core/session_manager.py` |

### Formularios y validación

| Requisito | Implementación | Archivo |
|-----------|---------------|---------|
| Creación de publicación — validar propiedad de habilidad para OFREZCO | `PostCreate.clean()` | `core/forms.py` |
| Acuerdo — validar que el participante tiene la habilidad requerida | `DealsPost.clean()` | `core/forms.py` |
| Sesión — solo creable en acuerdos `EN CURSO` | `Sesion.clean()` | `core/models.py` |
| Formulario de creación de sesión (fecha, hora, duración) | `SesionCreateForm` | `core/forms.py` |
| Formulario de edición de sesión (resumen + asistencia tras finalizar) | `SesionEditForm` | `core/forms.py` |
| Actualización de habilidades del perfil (entrada de texto libre) | `ProfileForm.save()` — `get_or_create` por token separado por coma | `core/forms.py` |
| Prevención de acuerdos duplicados | `IntegrityError` capturado en `DealsCreateView.form_valid()` | `core/views.py` |

### Videollamadas (Jitsi Meet)

| Requisito | Implementación | Archivo |
|-----------|---------------|---------|
| Generación de URL única de sala Jitsi Meet | `create_meet_link()` — nombre de sala basado en UUID bajo dominio propio | `core/services/meet.py` |
| `meet_link` almacenado en el modelo de sesión | `meet_link = models.URLField(blank=True, null=True)` | `core/models.py` |
| Enlace generado automáticamente al crear la sesión | `SesionCreateView.form_valid()` — llama a `create_meet_link()` y guarda | `core/views.py` |
| Propiedad de estado de sesión (próxima / en curso / finalizada) | `Sesion.ha_finalizado` — compara `fecha + hora + duracion_real` contra `now()` | `core/models.py` |
| Botón de unirse activo solo durante la ventana de la sesión | Condicional de plantilla sobre `session.ha_finalizado == 'ongoing'` | `core/templates/core/sesion_detail.html`, `sesioneslist.html` |
| Botón de unirse deshabilitado antes de que empiece | Condicional de plantilla sobre `session.ha_finalizado == 'upcoming'` | `core/templates/core/sesion_detail.html`, `sesioneslist.html` |
| Rellenar resumen y asistencia tras la sesión | `SesionEditView` + `SesionEditForm` en `sessions/<pk>/edit/` | `core/views.py`, `core/forms.py` |

### Middleware

| Requisito | Implementación | Archivo |
|-----------|---------------|---------|
| Anti-spam: máx. 3 publicaciones por usuario en 24 h | `SpamMiddleware.__call__()` | `core/middleware/anti_spam.py` |

### API REST

| Requisito | Implementación | Archivo |
|-----------|---------------|---------|
| ModelViewSet para todos los modelos principales | `UsuarioViewSet`, `PublicacionViewSet`, `AcuerdoViewSet`, `SesionViewSet` | `core/views.py` |
| Serializadores DRF | `UsuarioSerializer`, `PublicacionSerializer`, `AcuerdoSerializer`, `SesionSerializer` | `core/serializers.py` |
| API restringida a administradores | `permission_classes = [IsAdminUser]` en todos los ViewSets | `core/views.py` |
| Registro del router DRF | `router.register(...)` × 4 + `path('api/', include(router.urls))` | `core/urls.py` |
| Documentación automática Swagger / OpenAPI | `SpectacularAPIView`, `SpectacularSwaggerView` en `/api/docs/` | `skillswap/urls.py` |
| Acceso a la API con redirección segura | Wrapper `secure_api_view()` | `skillswap/urls.py` |

### Infraestructura y configuración

| Requisito | Implementación | Archivo |
|-----------|---------------|---------|
| Configuración multi-servicio con Docker | `docker-compose.yml` (web + db + perfil de tunnel opcional) | `docker-compose.yml` |
| Configuración de PostgreSQL | Diccionario `DATABASES` leyendo de `.env` | `skillswap/settings.py` |
| Configuración basada en variables de entorno | Todos los secretos via `os.getenv()` + `python-dotenv` | `skillswap/settings.py` |
| Archivos estáticos en producción | `WhiteNoiseMiddleware` + `STATIC_ROOT` | `skillswap/settings.py` |
| Servidor WSGI Gunicorn | `gunicorn skillswap.wsgi --bind 0.0.0.0:8000` | `docker-compose.yml` |
| Cloudflare Tunnel (opcional) | Servicio `tunnel` con `profiles: [production]` | `docker-compose.yml` |
| Poblador de datos de prueba idempotente | Comando `populate_test_data` usando `get_or_create` | `core/management/commands/populate_test_data.py` |



---

Hecho por José Antonio Hernández Humanes, Fabián Domínguez Casado y Andrés Mahindo Canalo.