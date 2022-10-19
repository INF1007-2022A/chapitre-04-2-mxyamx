#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	first_part = name.split('-')[0]
	capitalized = first_part[0].upper() + first_part[1:].lower()
	return (f"Bonjour, {capitalized}")

def get_random_sentence(animals, adjectives, fruits):
	animals = random.choice(animals)
	adjectives = random.choice(adjectives)
	fruits = random.choice(fruits)
	return (f"Aujourd’hui, j’ai vu un {animals} s’emparer d’un panier {adjectives} plein de {fruits}. ")

def encrypt(text, shift):
	result = ""
	for letter in text:
		encrypted_letter = letter
		if letter.isalpha():
			index = ord(letter.upper()) - ord("A")
			encrypted_index = (index + shift) % 26
			encrypted_letter = chr(ord("A") + encrypted_index)
		result += encrypted_letter
	return result


def decrypt(encrypted_text, shift):
	return encrypt(encrypted_text, -shift)


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))

	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
