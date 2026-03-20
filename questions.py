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
        "violeta",
        "magenta",
        "amarillo",
        "naranja",
        "marron",
        "turquesa",
        "cian",
        "celeste",
    ],
}

selected_category = False
words = False
while not words:
    print("Elija una de las categorias")
    for i, cat in enumerate(categories.keys()):
        print(f"{i}) {cat}")

    user_category_input = input("Categoria: ")

    if user_category_input in categories.keys():
        selected_category = user_category_input
        words = categories[user_category_input]
        break

    try:
        int_user_category_input = int(user_category_input)
        if (int_user_category_input >= 0) and (int_user_category_input < len(categories.keys())):
            selected_category = [c for c in categories.keys()][int_user_category_input]
            words = categories[selected_category]
            break
        print("No existe la categoria ingresada")
    except:
        print("No existe la categoria ingresada")

print(f"Elejiste la categoria {selected_category}")

word = random.choice(words)
guessed = []
attempts = 6
points = 0

print("¡Bienvenido al Ahorcado!")
print()

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

print(f"Terminaste con {points} puntos!")