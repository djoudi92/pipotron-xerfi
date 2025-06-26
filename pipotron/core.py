
from typing import Dict, List, Union
from itertools import product
import random
import re

# Signe AVEC espace avant
SIGNS_WITH_SPACE_BEFORE = {'!', '?', ':', ';', '»','«', '(', '[', '{', '«', '»'}

# Signe SANS espace avant
SIGNS_WITHOUT_SPACE_BEFORE = {'.', ',', '...', ')', ']', '"', '}', '…', '–', '-', '—', '—', '…'}

ALL_PUNCTUATION = SIGNS_WITH_SPACE_BEFORE.union(SIGNS_WITHOUT_SPACE_BEFORE)

def validate_spacing(sentence: str) -> bool:
    if not sentence:
        return False

    if sentence[-1] not in ALL_PUNCTUATION:
        return False

    for sign in SIGNS_WITH_SPACE_BEFORE:
        if sign in sentence and f" {sign}" not in sentence:
            return False

    for sign in SIGNS_WITHOUT_SPACE_BEFORE:
        if f" {sign}" in sentence:
            return False

    return True

def reconstruct_phrase(combination: List[str]) -> str:
    """
    Recompose une phrase en tenant compte des règles de ponctuation interne.
    """
    phrase = combination[0]
    for word in combination[1:]:
        if word in SIGNS_WITHOUT_SPACE_BEFORE:
            phrase += word
        elif word in SIGNS_WITH_SPACE_BEFORE:
            phrase += ' ' + word
        else:
            phrase += ' ' + word
    return phrase

def my_function(
    p_size: int,
    list_possibilities: Dict[int, List[str]],
    sentence: str,
    case_sensitive: bool = True
) -> Union[bool, str]:
    if not case_sensitive:
        sentence = sentence.lower()
        list_possibilities = {
            k: [val.lower() for val in v]
            for k, v in list_possibilities.items()
        }

    for i in range(1, p_size + 1):
        if i not in list_possibilities or not list_possibilities[i]:
            return f"Composant {i} manquant ou vide dans le dictionnaire."

    if not validate_spacing(sentence):
        return "Erreur de ponctuation : espace incorrect autour d’un signe, ou phrase non terminée par une ponctuation."

    all_combinations = product(
        *[list_possibilities[i] for i in range(1, p_size + 1)]
    )

    for combinaison in all_combinations:
        candidate = reconstruct_phrase(list(combinaison))
        if candidate == sentence:
            return True

    return "Phrase invalide : aucune combinaison possible ne correspond."


def generate_random_phrase(
    p_size: int,
    list_possibilities: Dict[int, List[str]]
) -> str:
    try:
        mots = [random.choice(list_possibilities[i]) for i in range(1, p_size + 1)]
        return reconstruct_phrase(mots)
    except KeyError:
        return "Erreur : dictionnaire incomplet pour générer une phrase."
