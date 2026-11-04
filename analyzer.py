log_file = "server.log"

total_requests = 0
error_counts = {}

print(f"--- Analyse du fichier {log_file} ---")

try:
    with open(log_file, "r") as file:
        for line in file:
            total_requests += 1
            parts = line.strip().split()
            if parts:
                status_code = parts[-1]
                error_counts[status_code] = error_counts.get(status_code, 0) + 1

    print(f"Nombre total de requêtes analysées : {total_requests}\n")
    print("Détail par code HTTP :")
    for code, count in error_counts.items():
        print(f"  - Code {code} : {count} fois")

except FileNotFoundError:
    print(f"Erreur : Le fichier {log_file} est introuvable.")
