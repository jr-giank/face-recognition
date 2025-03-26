# Instalación y Configuración

## Requisitos Previos

Antes de instalar el proyecto, asegúrese de contar con los siguientes requisitos:

- Python 3.8 o superior
- Pip (gestor de paquetes de Python)
- Visual Studio con las herramientas de compilación necesarias para `dlib` (Windows)
- CMake y Boost para `dlib` (Linux y MacOS)

## Instalación de Dependencias

### 1. Crear y activar un entorno virtual (Correr en la terminal)

```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En MacOS/Linux
source venv/bin/activate
```

### 2. Instalar las dependencias del proyecto

```bash
pip install -r requirements.txt
```

```bash
pip freeze  # Comprueba la instalación de los paquetes.
```

Si experimenta problemas con face-recognition, asegúrese de que dlib esté correctamente instalado. Para su instalación podria necesitar algunas dependencias de Windows que puedes instalar a traves de Visual Studio.

#### Instalar:

- C++ CMake Tools for Windows
- MSVC v142
- Windows 10/11 SDK
- C++ CMake Toolset
- C++ Clang Compiler
- C++ CMake Build Tools

## Configuración del Proyecto

### 1. Crear un archivo .env en la raíz del proyecto

```bash
SECRET_KEY=clave_secreta
```

Para generar una clave secreta en Django:

```bash
python manage.py shell
```

```bash
from django.core.management.utils import get_random_secret_key 
get_random_secret_key()
```
Agregar esta llave secreta a la variable SECRET_KEY en el archivo .env.

## Ejecución del Proyecto

### 1. Aplicar migraciones

```bash
python manage.py migrate
```

### 2.Ejecutar el servidor

```bash
python manage.py runserver
```
El servidor iniciará en http://127.0.0.1:8000/

## Iniciar el frontend

### 1. Abrir una nueva terminal y entrar al directorio de frontend

desde el directorio del proyecto hacer:
cd frontend

### 2. Ejecutar el servidor de frontend

python -m http.server 8080

El servidor estara disponible en http://127.0.0.1:8080/

## Peticiones al servidor

### 1. Subir imagenes a la BD

```bash
POST api/upload-image/
```

- Headers:

```bash
Content-Type: multipart/form-data
```

- Body:

```json
{
  "name": "nombre",
  "image": "data:image" 
}
```

### 2. Comparar caras

```bash
POST api/compare-faces/
```

- Headers:

```bash
Content-Type: multipart/form-data
```

- Body:

```json
{
  "image": "data:image" 
}
```