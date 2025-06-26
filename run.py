
from pipotron.core import my_function

def main():
    print("Bienvenue dans le vérificateur de Pipotron ")

    try:
        p_size = int(input("Nombre de composants (>=2) : "))
        if p_size < 2:
            raise ValueError("Le nombre de composants doit être au moins 2.")
    except ValueError as e:
        print("Entrée invalide :", e)
        return

    list_possibilities = {}
    for i in range(1, p_size + 1):
        comps = input(f"Entrées possibles pour la position {i} (séparées par '|') : ")
        list_possibilities[i] = [x.strip() for x in comps.split('|') if x.strip()]

    sentence = input("Phrase à tester : ")
    print("Note : les signes de ponctuation (ex. ., !, ?) ne doivent pas être précédés d’un espace.")

    case_sensitive_input = input("Respecter la casse ? (y/n) : ").strip().lower()
    case_sensitive = case_sensitive_input == 'y'

    result = my_function(p_size, list_possibilities, sentence, case_sensitive)
    print("\nRésultat :", " Valide (pipotron)" if result is True else result)

if __name__ == "__main__":
    main()
