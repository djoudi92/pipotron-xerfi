from pipotron.core import my_function

def test_examples():
    example_dict = {
        1: ['Je', 'Tu', 'Demain je'],
        2: ['mange', 'bois', 'vole', 'voles'],
        3: ['.', '!', '?', '…']
    }

    print("\nTest 1 : Phrase attendue valide → 'Je mange !'")
    result1 = my_function(3, example_dict, 'Je mange !')
    if result1 is not True:
        print(" Échec :", result1)
    else:
        print(" Réussi")

    print("\nTest 2 : Phrase attendue invalide → 'Tu dors ?'")
    result2 = my_function(3, example_dict, 'Tu dors ?')
    if result2 is not False:
        print(" Échec :", result2)
    else:
        print(" Réussi")
    print("\nTest 1 : Phrase attendue valide → 'Je mange !'")

    result3 = my_function(3, example_dict, 'Demain je vole…')
    if result3 is not True:
        print(" Échec :", result3)
    else:
        print(" Réussi")
if __name__ == "__main__":
    test_examples()
