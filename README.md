# 🌸 Proyecto Django: Blog de Fantasía 📚

Este proyecto consiste en el desarrollo del **Backend** para un sistema de Blog, utilizando el framework **Django** y base de datos **PostgreSQL**. El sistema permite gestionar Autores y Artículos (Posts).

---

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.12
* **Framework:** Django
* **Base de Datos:** PostgreSQL
* **Librerías:** `psycopg2` (conector SQL)

---

## ✨ Pasos Seguidos para el Desarrollo

### 1. Configuración Inicial
* Creación del entorno virtual (`venv`) e instalación de dependencias (`django`, `psycopg2`).
* Inicialización del proyecto Django (`django-admin startproject`) y creación de la aplicación `core`.

### 2. Base de Datos (PostgreSQL) 🐘
* Creación de la base de datos local `db_blog_sandra` mediante **pgAdmin 4**.
* Configuración de la conexión en el archivo `settings.py`, reemplazando SQLite por PostgreSQL como motor de base de datos.

### 3. Definición de Modelos (ORM) 📝
En el archivo `core/models.py` se crearon dos entidades relacionadas:
* **Modelo Autor:** Almacena nombre, apellido, email y género literario favorito.
* **Modelo Artículo:** Almacena título, contenido y fecha.
* **Relación:** Se estableció una `ForeignKey` (1 a N) entre Artículo y Autor.

### 4. Migraciones
* Ejecución de `python manage.py makemigrations` para generar los archivos de cambio.
* Ejecución de `python manage.py migrate` para plasmar las tablas en PostgreSQL.

### 5. Consultas ORM (Shell) 🔍
Se utilizó la shell de Django (`python manage.py shell`) para realizar las siguientes pruebas (adjuntas en capturas):
1.  Creación de instancias de **Autores** (ej: Emily McIntire).
2.  Creación de **Artículos** asociados a dichos autores (ej: Reseñas de libros).
3.  Consultas de filtrado para listar todos los artículos de un autor específico.

---
**Autor:** Sandra 👩🏻‍💻
**Fecha:** Febrero 2026