# CRUD Newspaper Django

Un proyecto de ejemplo en Django para gestión de artículos con operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y registro de usuarios.

## 📌 Resumen del proyecto

- Aplicación principal: `newspaper`
- CRUD de artículos con vistas basadas en clases
- Autenticación de usuarios con registro y login
- Base de datos SQLite para desarrollo
- Plantillas personalizadas en `templates/`
- Archivos estáticos en `static/`

## 🚀 Funcionalidades principales

- Listado de artículos disponibles
- Detalle de artículo
- Crear artículo (requiere usuario autenticado)
- Editar artículo (requiere usuario autenticado)
- Eliminar artículo (requiere usuario autenticado)
- Registro de nuevos usuarios
- Login/Logout usando Django auth

## 🧱 Estructura del proyecto

```
crud_abr2026/
├── base_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── newspaper/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── signup/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── _base.html
│   ├── article-create.html
│   ├── article-delete.html
│   ├── article-detail.html
│   ├── article-update.html
│   ├── articles-list.html
│   └── registration/
│       ├── login.html
│       └── signup.html
├── static/
│   └── css/style.css
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## 📂 Rutas principales

- `http://localhost:8000/` → Lista de artículos
- `http://localhost:8000/articulos/<pk>/` → Ver detalle de un artículo
- `http://localhost:8000/articulos/nuevo/` → Crear nuevo artículo
- `http://localhost:8000/articulos/<pk>/editar/` → Editar artículo
- `http://localhost:8000/articulos/<pk>/eliminar/` → Eliminar artículo
- `http://localhost:8000/accounts/login/` → Iniciar sesión
- `http://localhost:8000/accounts/logout/` → Cerrar sesión
- `http://localhost:8000/accounts/signup/` → Registrar nuevo usuario

## 🧠 Modelos

### `newspaper.models.Article`

- `title` - `CharField(max_length=200)`
- `content` - `TextField()`
- `author` - `ForeignKey('auth.User', on_delete=models.CASCADE)`
- `created_at` - `DateField(auto_now_add=True)`
- `updated_at` - `DateTimeField(auto_now=True)`

El modelo también define `get_absolute_url()` para redirigir automáticamente a la vista de detalle tras crear o actualizar un artículo.

## 🧩 Vistas

### `newspaper.views`

- `ArticleListView` - lista todos los artículos
- `ArticleDetailView` - muestra un artículo individual
- `ArticleCreateView` - formulario de creación de artículo
- `ArticleUpdateView` - formulario de edición de artículo
- `ArticleDeleteView` - confirmación de borrado

Las vistas de creación, actualización y eliminación requieren usuario autenticado gracias a `LoginRequiredMixin`.

### `signup.views`

- `SignUpView` - formulario de registro basado en `UserCreationForm`

## ⚙️ Configuración de Django

- `ROOT_URLCONF`: `base_project.urls`
- `TEMPLATES`: directorio `templates/`
- `STATICFILES_DIRS`: directorio `static/`
- `DATABASES`: SQLite (`db.sqlite3`)
- `LOGIN_REDIRECT_URL`: `articles_list`
- `LOGOUT_REDIRECT_URL`: `articles_list`

## 📥 Dependencias

El archivo `requirements.txt` incluye:

- `asgiref==3.11.1`
- `Django==6.0.4`
- `sqlparse==0.5.5`
- `tzdata==2026.1`

## 🛠️ Instalación y ejecución

1. Crear y activar entorno virtual (recomendado):

```bash
python -m venv venv
venv\Scripts\activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Aplicar migraciones:

```bash
python manage.py migrate
```

4. Ejecutar servidor de desarrollo:

```bash
python manage.py runserver
```

5. Abrir en el navegador:

```text
http://localhost:8000/
```

## 💡 Uso rápido

- Crear superusuario (opcional):

```bash
python manage.py createsuperuser
```

- Acceder al panel admin:

```text
http://localhost:8000/admin/
```

## 🎨 Plantillas

- `articles-list.html` → listado de artículos
- `article-detail.html` → detalle del artículo
- `article-create.html` → formulario de creación
- `article-update.html` → formulario de edición
- `article-delete.html` → confirmación de borrado
- `registration/login.html` → inicio de sesión
- `registration/signup.html` → registro de usuario

## 📌 Notas adicionales

- La aplicación principal registrada en `INSTALLED_APPS` es `newspaper`.
- El registro de usuario usa la vista `SignUpView` de `signup.views` y la URL `accounts/signup/`.
- Las operaciones de edición y eliminación solo están disponibles para usuarios autenticados.

## 🧪 Recomendaciones

- Para producción, deshabilitar `DEBUG` y configurar `ALLOWED_HOSTS`.
- Cambiar `SECRET_KEY` a una variable segura.
- Usar una base de datos más robusta en entornos reales.
