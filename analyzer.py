import argparse
from collections import Counter
import re


def analyser_logs(chemin_fichier):
  total_lignes = 0
  echecs_connexion = 0
  ips_suspectes = Counter()

  motif_echec = re.compile(r'Failed password for.*?from\s+([0-9.]+)')

  print(f'— Analyse du fichier : {chemin_fichier} —\n')

  try:
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
      for ligne in fichier:
        if not ligne.strip():
          continue

        total_lignes += 1

        # Vérification des échecs d'authentification
        if 'Failed password' in ligne:
          echecs_connexion += 1
          match = motif_echec.search(ligne)
          if match:
            ip = match.group(1)
            ips_suspectes[ip] += 1

    print(f'Nombre total de lignes analysées : {total_lignes}')
    print(f'Nombre total d’échecs de connexion : {echecs_connexion}\n')

    if ips_suspectes:
      print('Adresses IP sources des échecs :')
      for ip, count in ips_suspectes.most_common(5):
        print(f'  - {ip} : {count} tentative(s)')

  except FileNotFoundError:
    print(f"Erreur : Le fichier '{chemin_fichier}' est introuvable.")
  except PermissionError:
    print(
        f"Erreur : Permission refusée pour lire le fichier '{chemin_fichier}'."
    )


if __name__ == '__main__':
  parser = argparse.ArgumentParser(
      description='Analyseur de logs de sécurité pour le système.'
  )
  parser.add_argument(
      '-f',
      '--file',
      default='/var/log/auth.log',
      help='Chemin vers le fichier de log à analyser (par défaut : /var/log/auth.log)',
  )
  args = parser.parse_args()

  analyser_logs(args.file)
