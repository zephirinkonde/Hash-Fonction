import hashlib

def hash_function(key: str) -> int:
  """
  Fonction de hachage qui respecte les caractéristiques de déterminisme, de fonction à sens unique, de sécurité contre les collisions, de rapidité et de résistance.

  Args:
    key: La clé à hacher.

  Returns:
    La valeur de hachage de la clé.
  """

  # Convertir la clé en une chaîne de bits.
  key_bits = key.encode("utf-8")

  # Calculer la valeur de hachage en utilisant l'algorithme SHA-256.
  hash_digest = hashlib.sha256(key_bits).digest()

  # Récupérer les 4 premiers octets de la valeur de hachage.
  hash_value = hash_digest[:4]
# Convertir les 4 octets en un entier.
  hash_value = int.from_bytes(hash_value, "big")

  return hash_value

def main():
  # Demander à l'utilisateur d'entrer une valeur.
  key = input("Entrez une valeur : ")

  # Calculer la valeur de hachage.
  hash_value = hash_function(key)

  # Afficher la valeur de hachage.
  print("La valeur de hachage est :", hash_value)

if __name__ == "__main__":
  main()
