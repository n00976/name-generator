#- Konieczność użycia modułu `random`.
import random
#- Program generuje wymawialne(!) imię o zadanej długości (7) i dodaje do niego przydomek (opcjonalnie również tytuł i liczebnik).

string_VOWEL = 'aeiouy'
string_CONSONANT = "bcdfghjklmnpqrstvwxz"

def generate_name():
    name_letters = [first_letter]
    letters = 0
    while letters < name_length:
        if name_letters[letters] in string_vowel:
            add_letter = random.choice(string_consonant)
            name_letters.append(add_letter)
            letters = letters + 1
        else:
            add_letter = random.choice(string_vowel)
            name_letters.append(add_letter)
            letters = letters + 1
    name = "".join(name_letters)
    name = name.capitalize()
    return name


first_letter = input("Podaj pierwszą literę imienia bohatera:")
name_length = int(input("Podaj długość imienia bohatera:"))

created_name = generate_name()

number_list = ["I", "II", "III", "IV", "V"]
number = random.choice(number_list)
title_list = ["Pazerny", "Grabieżca", "Nieustraszony", "Parszywy"]
title = random.choice(title_list)


print(created_name + " " + number + " " + title)
