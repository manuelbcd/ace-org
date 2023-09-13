import json
import csv
import os

# Definir la ruta del archivo a procesar
# file_path = "1-helloworld-from-alpine-3.17.1/sources/snyk_result.json"
file_path = "2-crypto-from-alpine/sources/snyk_result.json"

# Obtener la ruta del archivo actual y añadir la ruta del archivo a procesar
folder_path = os.path.dirname(os.path.abspath(__file__))
full_file_path = os.path.join(folder_path, file_path)

# Abrir el archivo JSON y cargar los datos
with open(full_file_path) as f:
    data = json.load(f)

# Crear el archivo CSV y escribir la cabecera
csv_path = os.path.join(folder_path, "snyk_results.csv")
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "CVE", "packageName", "name", "version", "exploit", "nvd-severity"])

    # Iterar sobre los datos y escribir cada línea en el archivo CSV
    # Capa de OS
    for vuln in data["vulnerabilities"]:
        cve_id = vuln.get("identifiers", {}).get("CVE", "")
        package_name = vuln.get("packageName", "")
        name = vuln.get("title", "")
        version = vuln.get("version", "")
        exploit = vuln.get("exploit", "")
        nvd_severity = vuln.get("cvssScore", "")

        writer.writerow([vuln["id"], cve_id, package_name, name, version, exploit, nvd_severity])
    # Capa de aplicación
    for app in data["applications"]:
        for vuln in app["vulnerabilities"]:
            cve_id = vuln.get("identifiers", {}).get("CVE", "")
            package_name = vuln.get("packageName", "")
            name = vuln.get("title", "")
            version = vuln.get("version", "")
            exploit = vuln.get("exploit", "")
            nvd_severity = vuln.get("cvssScore", "")

            writer.writerow([vuln["id"], cve_id, package_name, name, version, exploit, nvd_severity])

print("Archivo CSV generado con éxito en: ", csv_path)
