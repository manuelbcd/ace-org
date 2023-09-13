import json
import csv
import os

# Define el path al archivo JSON
# json_file = "1-helloworld-from-alpine-3.17.1/sources/trivy_result.json"
json_file = "2-crypto-from-alpine/sources/trivy_result.json"

# Abre el archivo JSON y carga los datos
with open(json_file, "r") as f:
    data = json.load(f)

# Crea la lista de resultados
results = data["Results"]

# Define los campos que se incluirán en el CSV
fields = ["id", "CVE", "packageName", "name", "version", "exploit", "nvd-severity"]

# Crea el archivo CSV y escribe los encabezados
csv_file = "trivy_results.csv"
with open(csv_file, "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()

    # Escribe cada fila en el archivo CSV
    for result in results:
        vulnerabilities = result["Vulnerabilities"]
        for vuln in vulnerabilities:
            writer.writerow({
                "id": data["Metadata"]["ImageID"],
                "CVE": vuln["VulnerabilityID"],
                "packageName": vuln["PkgName"],
                "name": vuln["Title"],
                "version": vuln["InstalledVersion"],
                "exploit": "null",
                "nvd-severity": vuln["Severity"]
            })

print("El archivo CSV se ha creado exitosamente!")
