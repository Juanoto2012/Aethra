# 📜 Política de Inclusión de Aplicaciones (Aethra)

Bienvenido a **Aethra**. Nuestra misión es proporcionar un catálogo moderno, seguro y sin fricciones de aplicaciones de código abierto para Android. 

A diferencia de otros repositorios tradicionales que tienen reglas extremadamente estrictas sobre qué constituye una app "pura" o que exigen compilar todo desde cero, nosotros adoptamos un enfoque **pragmático**. Creemos en el software libre, pero también en las tecnologías modernas.

A continuación, detallamos nuestros criterios para aceptar una app en Aura Repo:

## ✅ 1. Código Abierto (Open Source)
La aplicación **debe** tener su código fuente publicado bajo una licencia libre o de código abierto reconocida (GPL, MIT, Apache, etc.). El repositorio debe ser accesible al público (por ejemplo, en GitHub o GitLab).

## 🤖 2. IA y APIs Externas ¡Son Bienvenidas!
Entendemos que el software moderno se conecta con el mundo. 
- **Sí permitimos** aplicaciones que utilicen APIs de terceros (tanto gratuitas como comerciales).
- **Sí permitimos** aplicaciones basadas en Inteligencia Artificial (clientes de LLMs, generadores de imágenes, integraciones con servicios en la nube, etc.).
No marcaremos tu app como "Anti-Feature" por conectarse a servicios de red no libres. ¡Abrazamos la innovación!

## 📦 3. Extracción de APKs (GitHub Releases)
Para mantener las actualizaciones rápidas y respetar el trabajo del desarrollador, **no compilamos las aplicaciones desde el código fuente**. 
- Tomamos los archivos `.apk` pre-compilados directamente de la sección de **Releases** de tu repositorio.
- Asegúrate de subir tus APKs allí. Si tu app no proporciona APKs en los releases, no podremos incluirla automáticamente.

## 🛡️ 4. Seguridad y Análisis (VirusTotal)
La libertad no está reñida con la seguridad. Para proteger a nuestros usuarios:
- Cada APK indexado en Aura Repo será escaneado utilizando la API de **VirusTotal**.
- Si el análisis detecta un comportamiento consistentemente malicioso (malware, troyanos, spyware real), la aplicación será rechazada o eliminada del repositorio de forma inmediata.
- Falsos positivos de un par de motores menores pueden ser revisados manualmente, pero nos reservamos el derecho de no incluir aplicaciones sospechosas.

## 🚫 5. Lo que NO permitimos
Aunque somos muy flexibles, hay límites lógicos. No se aceptarán aplicaciones que:
- Contengan o promuevan malware, phishing o robo de datos.
- Estén diseñadas explícitamente para actividades ilegales o piratería directa que ponga en riesgo legal al repositorio.
- Sean repositorios vacíos o aplicaciones sin funcionalidad real (spam).

## 🔄 Proceso de actualización
Las actualizaciones se reflejarán en Aura Repo rastreando los nuevos *Releases* de tu repositorio. Solo asegúrate de etiquetar correctamente tus versiones en GitHub y nosotros haremos el resto.

---

¿Tu app cumple con estos puntos simples? ¡Entonces estamos deseando tenerla!
Ve a la sección de [Issues](../../issues) y abre una nueva **Solicitud de Inclusión de App (RFP)**.
