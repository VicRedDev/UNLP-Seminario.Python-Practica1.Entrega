import random

categories = {
    "paises": [
        "argentina",
        "brazil",
        "uruguay",
        "chile",
        "paraguay",
        "peru",
        "ecuador",
        "canada",
    ],
    "programacion": [
        "variable",
        "funcion",
        "bucle",
        "cadena",
        "entero",
        "lista",
        "programa",
        "python",
        "frontend",
        "backend",
        "git",
        "servidor",
    ],
    "colores": [
        "rojo",
        "azul",
        "verde",
        # "violeta",
        # "magenta",
        # "amarillo",
        # "naranja",
        # "marron",
        # "turquesa",
        # "cian",
        # "celeste",
    ],
}

def menu(options: list[str]):
    while True:
        print("Elija una de las siguientes opciones")
        print()
        for i, opt in enumerate(options):
            print(f"{i}) {opt}")
        print()

        user_input = input("Opcion: ")
        print()

        if user_input in options:
            return user_input

        try:
            int_user_input = int(user_input)
            if (int_user_input >= 0) and (int_user_input < len(options)):
                return options[int_user_input]
            print("No existe la opcion ingresada")
        except:
            print("No existe la opcion ingresada")
        
        print()


print("¡Bienvenido al Ahorcado!")
print()

words = []

while True:
    if not len(words) > 0:
        selected_category = menu(list(categories.keys()))
        print(f"Elejiste la categoria {selected_category}")
        print()
        words = categories[selected_category].copy()
        random.shuffle(words)
        category_points = 0
        category_victories = 0

    word = words.pop()

    guessed = []
    attempts = 6
    points = 0

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "

        print(progress)

        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            points += 6
            category_victories += 1
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")

        if len(letter) > 1 or len(letter) == 0 or letter < 'A' or letter > 'z':
            print("Entrada no válida")
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            points -= 1
            attempts -= 1
            
        print("Esa letra no está en la palabra.")
        print()
    else:
        points = 0
        print(f"¡Perdiste! La palabra era: {word}")

    category_points += points

    print(f"Terminaste con {points} puntos!")
    print()

    if not len(words) > 0:
        print(f"Terminaste la categoria {selected_category} con {category_victories} victorias y {category_points} puntos!")
        print()

    print('Te gustaria jugar de nuevo?')
    play_again = menu(['si', 'no'])
    if play_again != 'si':
        print('Chau!')
        break
