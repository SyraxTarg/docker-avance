def cowsay(message: str):
    lines = message.split('\n')
    width = max(len(line) for line in lines)
    bubble_top = " " + "_" * (width + 2)
    bubble_bottom = " " + "-" * (width + 2)
    bubble_lines = [f"< {line.ljust(width)} >" for line in lines]

    # La "vache"
    cow = r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
    """

    # Affichage
    print(bubble_top)
    for line in bubble_lines:
        print(line)
    print(bubble_bottom)
    print(cow)

# Exemple d'utilisation
if __name__ == "__main__":
    cowsay("Salut, Docker !\nTu veux du fromage ? 🧀")
