# ¡Bienvenido a Web Playground! 🚀

Web Playground es una increíble aplicación web construida con Django que te permitirá explorar y aprender conceptos clave mientras te diviertes construyendo aplicaciones. 💡🎉

## Características Principales ✨

A lo largo del proyecto Web Playground, podrás disfrutar de las siguientes características:

- 🎮 **Vistas basadas en clases (CBV):** ¡No te preocupes por las complicadas vistas basadas en funciones! Aquí utilizamos las vistas basadas en clases para simplificar tu experiencia.

- 📝 **Generación automágica de CRUD:** Olvídate de escribir código repetitivo para crear, leer, actualizar y borrar (CRUD) datos. Nuestro generador mágico se encargará de eso por ti.

- 🔐 **Sistema de autenticación de usuarios:** Asegura tu aplicación con nuestro poderoso sistema de autenticación. ¡Protege tus datos y mantén a los intrusos fuera!

- 🎉 **Registro de usuarios sin complicaciones:** Nuestro sencillo sistema de registro de usuarios te permitirá dar la bienvenida a nuevos usuarios sin problemas. ¡Únete a la fiesta!

- 🌟 **Perfiles de usuarios personalizables:** Da vida a tus usuarios con perfiles personalizables. Agrega avatares, biografías e incluso enlaces a redes sociales. ¡Deja que brillen!

- 📨 **Restauración de contraseña por correo electrónico:** ¿Olvidaste tu contraseña? ¡No te preocupes! Te enviaremos instrucciones mágicas por correo electrónico para restaurarla. 📧✨

- 🚀 **Aplicaciones adicionales para explorar:** ¡No te conformes solo con las funcionalidades básicas! Explora nuestras aplicaciones adicionales para perfiles públicos y mensajería privada. ¡La diversión nunca termina!

## Instrucciones para la ejecución 🛠️

¡Prepárate para la diversión! Sigue estos pasos para ejecutar Web Playground en tu entorno local:

1. 🔽 Clona este repositorio en tu máquina local:

```
git clone https://github.com/tu_usuario/web-playground.git
```

2. 🚀 Accede al directorio del proyecto:

```
cd web-playground
```

3. 🐍 Asegúrate de tener Python 3 instalado en tu sistema. Si aún no lo tienes, ¡no te preocupes! Solo necesitas unas pocas pociones mágicas para instalarlo.

4. 🌌 Crea y activa un entorno virtual para evitar conflictos con otras aplicaciones mágicas:

```
pipenv shell
```

5. 📦 Instala las dependencias necesarias usando el poderoso `pipenv`:

```
pipenv install --ignore-pipfile
```

6. ⚙️ Antes de ejecutar el proyecto, asegúrate de configurar las variables de entorno adecuadas. Crea un archivo `.env` en el directorio raíz del proyecto y define las siguientes variables:

```
DEBUG=True
SECRET_KEY=CLAVE SECRETA
DATABASE_URL=sqlite:///db.sqlite3
SECRET_KEY=mi_clave_secreta
DEBUG=True
EMAIL_HOST=mi_servidor_smtp
EMAIL_PORT=mi_puerto_smtp
EMAIL_HOST_USER=mi_usuario_smtp
EMAIL_HOST_PASSWORD=mi_contraseña_smtp
```

¡No olvides reemplazar los valores mágicos con los tuyos propios!


7. 🧙 Realiza las migraciones de la base de datos para crear las tablas necesarias:

```
python manage.py migrate
```

8. 🌟 Crea un superusuario para acceder al panel de administración mágico:

```
python manage.py createsuperuser
```

Sigue las indicaciones para proporcionar un nombre de usuario, correo electrónico y contraseña para el superusuario.

9. 🚀 ¡Hora de encender los motores! Inicia el servidor de desarrollo:

```
python manage.py runserver
```

La aplicación Web Playground estará disponible en `http://localhost:8000/`. Podrás acceder al panel de administración de Django en `http://localhost:8000/admin/` utilizando las credenciales del superusuario que creaste.

**Nota:** Asegúrate de que los puertos necesarios estén disponibles y no estén bloqueados por firewalls u otros servicios en tu máquina.

10. 👀 Una vez que el servidor de desarrollo esté en marcha, abre tu navegador web y visita `http://localhost:8000` para acceder a la página principal de Web Playground.

11. 🎉 ¡Explora y diviértete! Podrás experimentar con todas las increíbles funcionalidades y conceptos que ofrece el proyecto. Sigue las instrucciones y consulta la documentación para comprender cómo utilizar cada característica.

12. 🤝 Si deseas probar la funcionalidad de autenticación de usuarios, puedes registrarte como un nuevo usuario haciendo clic en el enlace "Registrarse" en la esquina superior derecha de la página. Completa el formulario de registro con la información requerida y haz clic en "Registrarse". Después de registrarte, podrás iniciar sesión utilizando tus credenciales.

13. ⚡ Además, puedes acceder al panel de administración de Django en `http://localhost:8000/admin/` utilizando las credenciales del superusuario que creaste en el paso 8. Desde el panel de administración, podrás gestionar los modelos de la aplicación y realizar tareas administrativas.

14. 🌈 Si deseas explorar y utilizar alguna de las aplicaciones individuales desarrolladas como parte del proyecto (por ejemplo, la aplicación de perfiles públicos o la aplicación de mensajería privada), podrás acceder a ellas siguiendo las URLs proporcionadas en la documentación del proyecto.

¡Disfruta explorando y aprendiendo con Web Playground! Si tienes alguna pregunta o encuentras algún problema, consulta la documentación o visita el repositorio en GitHub para obtener más información.

¡Feliz codificación! 🎉🚀
