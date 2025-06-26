from pipotron.core import my_function

def test_examples():
    example_dict = {
        1: ['Je', 'Tu', 'Demain je'],
        2: ['mange', 'bois', 'vole', 'voles'],
        3: ['.', ' !', ' ?', '…']
    }

    assert my_function(3, example_dict, 'Je mange !') == True
    assert my_function(3, example_dict, 'Tu dors ?') != True
    assert my_function(3, example_dict, 'Demain je vole…') == True
    print(" Tous les tests passent.")

if __name__ == "__main__":
    test_examples()
