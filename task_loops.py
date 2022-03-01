

ages = [5, 15, 64, 27, 84, 26]


odd_numbers = [number for number in ages if number % 2 != 0]
print(odd_numbers)

chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]

long_chicken_names = [names for names in chicken_names if len(names) > 10]
print(long_chicken_names)

h_names = [names for names in chicken_names if names.startswith("H")]
print(h_names)


words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

first_letter_list = [word[0].lower() for word in words]
print(first_letter_list)

