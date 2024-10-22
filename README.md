# Tutorial: Despliegue de una aplicación Flask en Kubernetes (GCP)

**¿Qué es este repositorio?**

Este repositorio contiene todos los archivos y scripts necesarios para seguir el tutorial de despliegue de una aplicación Flask en un clúster de Kubernetes en Google Cloud Platform (GCP). A través de este proyecto, aprenderás a:

* **Crear un clúster de Kubernetes:** Provisionar un entorno de Kubernetes en GCP.
* **Configurar un repositorio de contenedores:** Utilizar Artifact Registry para almacenar las imágenes de Docker.
* **Desarrollar una aplicación Flask:** Crear una sencilla aplicación web con Python y Flask.
* **Crear una imagen de Docker:** Empaquetar la aplicación en un contenedor Docker.
* **Desplegar la aplicación en Kubernetes:** Utilizar Deployment para gestionar el despliegue de la aplicación.
* **Escalar horizontalmente:** Configurar el escalado automático de la aplicación.

**Estructura del proyecto:**

* **dockerfile:** Contiene las instrucciones para construir la imagen de Docker.
* **requirements.txt:** Lista las dependencias de la aplicación Flask.
* **app.py:** Código fuente de la aplicación Flask.
* **deployment.yaml:** Manifiesto de Kubernetes para desplegar la aplicación.
* **service.yaml:** Manifiesto de Kubernetes para exponer la aplicación.

**Cómo utilizar este repositorio:**

1. **Clona el repositorio:** `git clone https://github.com/PabloRioseco/hello-world-flask.git`
2. **Sigue las instrucciones del tutorial:** https://youtu.be/qS_4rPcYrG4 (El tutorial te guiará paso a paso en la creación del clúster, la construcción de la imagen, y el despliegue de la aplicación.)

**Tecnologías utilizadas:**

* **Kubernetes:** Plataforma de orquestación de contenedores.
* **Google Cloud Platform (GCP):** Proveedor de servicios en la nube.
* **Docker:** Plataforma para crear y ejecutar contenedores.
* **Python y Flask:** Lenguaje de programación y framework web para desarrollar la aplicación.

**Contribuciones:**

Las contribuciones son bienvenidas. Si encuentras algún error o tienes alguna sugerencia, por favor abre un issue o crea una pull request.

**Licencia:**

[MIT]

**Agradecimientos:**

Agradecemos a Generation Chile por la oportunidad de poder permitirnos aportar nuestro conocimiento a su programa "Adminitradores Cloud".