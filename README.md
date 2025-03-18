# JobMatch AI

**JobMatch AI** es una plataforma diseñada para automatizar la creación y gestión de campañas publicitarias en diversas redes sociales de manera simultánea. Facilita la creación de anuncios, la selección de plataformas, la gestión de presupuestos y la programación de publicaciones, todo desde una única interfaz.

## Descripción

Este proyecto tiene como objetivo simplificar la tarea de crear y publicar anuncios en varias plataformas de redes sociales como **Facebook**, **Instagram** y **TikTok**. Los usuarios pueden crear campañas publicitarias, subir contenido multimedia, establecer presupuestos, y definir horarios de publicación sin necesidad de acceder a cada plataforma por separado.

### Características

- **Interfaz fácil de usar**: Un panel de control donde los usuarios pueden ver estadísticas de sus campañas y gestionar anuncios.
- **Plataformas integradas**: Capacidad de publicar anuncios automáticamente en plataformas como Facebook, Instagram y TikTok.
- **Automatización de la gestión de campañas**: Los usuarios pueden programar sus anuncios para que se publiquen automáticamente en el momento seleccionado.
- **Gestión de contenido multimedia**: Subida de archivos de manera sencilla para incluir imágenes, videos y otros archivos en los anuncios.
- **Panel de control**: Un dashboard donde los usuarios pueden ver estadísticas de sus campañas activas, incluyendo gasto mensual, clics y más.

## Instalación

### Requisitos previos

- Python 3.x
- Django (para backend)
- HTML/CSS/JavaScript (para frontend)
- Base de datos relacional (por ejemplo, PostgreSQL, MySQL)
  
### Pasos de instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/alexahurtado08/Reto_Ingenieria_de_Software/
   ```

2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configurar la base de datos y realizar las migraciones:
   ```bash
   python manage.py migrate
   ```

4. Iniciar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

5. Accede a la aplicación desde el navegador en `http://localhost:8000/dashboard`.

## Uso

1. **Panel de control**: El panel principal ofrece una visión general del rendimiento de tus campañas, mostrando estadísticas como el gasto mensual, clics y formularios nuevos.
2. **Crear campaña**: Accede a la sección "Crear Campaña" para configurar los anuncios. Puedes seleccionar las plataformas donde deseas publicar, definir el presupuesto y subir contenido multimedia.
3. **Administrar campañas activas**: Visualiza las campañas en curso y realiza ajustes según sea necesario.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
