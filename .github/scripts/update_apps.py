import os
import json
import re
from datetime import datetime

def parse_issue(body):
    app_data = {}
    
    # Expresiones regulares para leer el formato que genera GitHub automáticamente
    fields = {
        "id": r"### ID de la App\s+([^\n]+)",
        "name": r"### Nombre de la App\s+([^\n]+)",
        "developer": r"### Desarrollador\s+([^\n]+)",
        "short_desc": r"### Descripción Corta\s+([^\n]+)",
        "description": r"### Descripción\s+(.*?)(?=###|$)",
        "icon_url": r"### URL del Icono\s+([^\n]+)",
        "category": r"### Categoría\s+([^\n]+)",
        "version": r"### Versión\s+([^\n]+)",
        "size": r"### Tamaño\s+([^\n]+)",
        "license": r"### Licencia\s+([^\n]+)",
        "download_url": r"### URL de Descarga\s+([^\n]+)",
        "repo_url": r"### URL del Repositorio\s+([^\n]+)"
    }

    for key, pattern in fields.items():
        match = re.search(pattern, body, re.DOTALL)
        if match:
            value = match.group(1).strip()
            # Omitimos campos vacíos marcados por defecto por GitHub
            if value != "_No response_": 
                app_data[key] = value

    # Generar la fecha de subida automáticamente
    app_data["timestamp"] = datetime.utcnow().isoformat() + "Z"
    return app_data

if __name__ == "__main__":
    # Leer el texto del Issue
    issue_body = os.environ.get("ISSUE_BODY", "")
    new_app = parse_issue(issue_body)

    if "id" not in new_app or "name" not in new_app:
        print("Faltan datos obligatorios. Se cancela.")
        exit(1)

    # Cargar el archivo apps.json existente
    try:
        with open("apps.json", "r", encoding="utf-8") as f:
            apps = json.load(f)
    except Exception:
        apps = [] # Si no existe, creamos una lista vacía

    # Actualizar si ya existe, o añadirla al principio si es nueva
    existing_index = next((i for i, a in enumerate(apps) if a.get("id") == new_app["id"]), None)
    
    if existing_index is not None:
        apps[existing_index].update(new_app)
    else:
        apps.insert(0, new_app)

    # Guardar de vuelta en apps.json
    with open("apps.json", "w", encoding="utf-8") as f:
        json.dump(apps, f, indent=4, ensure_ascii=False)
    
    print(f"App {new_app['name']} procesada correctamente.")
