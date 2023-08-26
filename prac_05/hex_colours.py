COLORS = {"amber": "#ffbf00", "aqua": "#00ffff", "beige": "#f5f5dc", "black": "#000000", "blue": "#0000ff",
          "coffee": "#6f4e37", "dandelion": "#f0e130", "gold": "#ffd700", "iris": "#5a4fcf", "pink": "#ffb5c5"}


def main():
    color_name = input("Enter a color name: ").strip().lower()

    while color_name != "":
        if color_name in COLORS:
            hex_code = COLORS[color_name]
            print(f"The hexadecimal code for {color_name.capitalize()} is {hex_code}")
        else:
            print("Invalid color name.")

        color_name = input("Enter a color name: ").strip().lower()


main()
