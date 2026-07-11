from tabulate import tabulate


def print_terminal_report(results):
    """Muestra el reporte formateado en la terminal como tabla."""
    if not results:
        print("\n--- LINUX PRIVILEGED ACCESS REVIEW ---")
        print("No se encontraron usuarios de riesgo.")
        return

    print("\n--- LINUX PRIVILEGED ACCESS REVIEW ---\n")
    
    table_data = []
    for entry in results:
        reasons = "\n".join(entry['risk']['reasons'])
        table_data.append([
            entry['username'],
            entry['risk']['level'],
            entry['risk']['score'],
            reasons
        ])
    
    headers = ["Usuario", "Nivel", "Score", "Razones"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    print(f"\nTotal usuarios revisados: {len(results)}")


def export_json_report(results, filename="report.json"):
    """Exporta resultados a JSON para auditorías."""
    import json
    with open(filename, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n[+] Reporte exportado a {filename}")
