#TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as letter:
    with open("./Input/Names/invited_names.txt") as names:
        salutations = letter.readlines()
        for name in names.readlines():
            with open(f"./Output/{name.strip()}.txt", "w") as new_letter:
                bones = salutations[0].replace("[name]", name)
                letter = ""
                letter += bones
                for salut in salutations[2::2]:
                    letter += salut
                new_letter.write(letter)
