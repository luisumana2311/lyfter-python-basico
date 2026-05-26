import json


def load_pokemon_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def get_new_pokemon():
    print("\nEnter the new Pokémon information:")

    name = input("Name: ")
    pokemon_type = input("Type: ")
    level = int(input("Level: "))
    hp = int(input("HP: "))

    new_pokemon = {
        "name": name,
        "type": pokemon_type,
        "level": level,
        "hp": hp
    }

    return new_pokemon


def save_pokemon_file(filename, pokemon_list):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(pokemon_list, file, indent=4)


def main():
    filename = "pokemon.json"

    pokemon_list = load_pokemon_file(filename)

    new_pokemon = get_new_pokemon()

    pokemon_list.append(new_pokemon)

    save_pokemon_file(filename, pokemon_list)

    print("\nThe new Pokémon was added successfully!")


main()