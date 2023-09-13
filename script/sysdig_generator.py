import json
import csv
import os

# Nombre del archivo JSON a procesar
# file_path = "1-helloworld-from-alpine-3.17.1/sources/sysdig_result.json"
file_path = "2-crypto-from-alpine/sources/sysdig_result.json"

# Obtener la ruta completa del archivo
folder_path = os.path.dirname(os.path.abspath(__file__))
full_file_path = os.path.join(folder_path, file_path)

# Abrir el archivo JSON y cargar los datos
with open(full_file_path) as f:
    data = json.load(f)

# Crear el archivo CSV y escribir la cabecera
csv_path = os.path.join(folder_path, "sysdig_results.csv")
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["imageID", "CVE", "packageName", "null", "version", "exploitable", "nvd-severity"])

    # Iterar sobre la lista de packages y sus vulnerabilidades
    for package in data["packages"]["list"]:
        image_id = data["metadata"]["imageID"]
        package_name = package.get("name", "")
        package_version = package.get("version", "")

        for vulnerability in package.get("vulnerabilities", []):
            cve_id = vulnerability.get("name", "")
            exploitable = vulnerability.get("exploitable", "")
            nvd_severity = vulnerability.get("severity", "").get("label", "")

            writer.writerow([image_id, cve_id, package_name, "null", package_version, exploitable, nvd_severity])

print("Archivo CSV generado con éxito en:", csv_path)
