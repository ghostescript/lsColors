import os
import sys

# Predefined colors
COLORS = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37",
}

ATTRIBUTES = {
    "normal": "00",
    "bold": "01",
    "underline": "04",
    "blink": "05",
    "reverse": "07",
}

def get_current_colors():
    """Reads the .dir_colors file and returns a dictionary of file types and their colors."""
    if not os.path.exists(".dir_colors"):
        os.system("dircolors -p > .dir_colors")

    colors = {}
    with open(".dir_colors", "r") as f:
        for line in f:
            if not line.startswith("#") and " " in line:
                parts = line.strip().split(" ", 1)
                if len(parts) == 2:
                    file_type, color_code = parts
                    colors[file_type] = color_code
    return colors

def update_dir_colors_file(colors):
    """Updates the .dir_colors file with the new color settings."""
    with open(".dir_colors", "w") as f:
        for file_type, color_code in colors.items():
            f.write(f"{file_type} {color_code}\n")

def print_help():
    """Prints the help message."""
    print("Usage: python set_ls_color.py <file_type> <color> <attribute>")
    print("       python set_ls_color.py <file_type> 256 <color_code> <attribute>")
    print("       python set_ls_color.py list-colors")
    print("       python set_ls_color.py -l")
    print("\nChanges the color of a file type for the 'ls' command.")
    print("\nArguments:")
    print("  <file_type>   The type of file to change the color of (e.g., DIR, .txt, .py)")
    print("  <color>         The new color for the file type (e.g., red, green, blue)")
    print("  <attribute>     The new attribute for the file type (e.g., normal, bold, underline)")
    print("  256             Use a 256-color code instead of a named color")
    print("  <color_code>    A number from 0 to 255 for the 256-color palette")
    print("  list-colors     List all 256 color codes")
    print("  -l              List available file types, colors, and attributes")

def list_available_options():
    """Lists available file types, colors, and attributes."""
    print("\nAvailable file types:")
    for file_type in get_current_colors().keys():
        print(f"- {file_type}")
    print("\nAvailable colors:")
    for color in COLORS.keys():
        print(f"- {color}")
    print("\nAvailable attributes:")
    for attribute in ATTRIBUTES.keys():
        print(f"- {attribute}")

def list_256_colors():
    """Lists all 256 color codes."""
    print("256 Color Palette:")
    for i in range(256):
        print(f"\033[38;5;{i}mColor {i}\033[0m", end="\t")
        if (i + 1) % 8 == 0:
            print()

def main():
    """Main function to handle user interaction."""
    if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print_help()
        return

    if len(sys.argv) == 2 and sys.argv[1] == "-l":
        list_available_options()
        return

    if len(sys.argv) == 2 and sys.argv[1] == "list-colors":
        list_256_colors()
        return

    if len(sys.argv) != 4 and len(sys.argv) != 5:
        print("Invalid number of arguments.")
        print_help()
        return

    file_type_to_change = sys.argv[1]
    new_color_code = ""

    if len(sys.argv) == 4:
        new_color_name = sys.argv[2]
        new_attribute_name = sys.argv[3]

        if new_color_name not in COLORS:
            print(f"Error: Color '{new_color_name}' not found.")
            list_available_options()
            return

        if new_attribute_name not in ATTRIBUTES:
            print(f"Error: Attribute '{new_attribute_name}' not found.")
            list_available_options()
            return

        new_color_code = f"{ATTRIBUTES[new_attribute_name]};{COLORS[new_color_name]}"

    elif len(sys.argv) == 5:
        if sys.argv[2] != "256":
            print("Invalid arguments for 256-color mode.")
            print_help()
            return

        try:
            color_code = int(sys.argv[3])
            if not (0 <= color_code <= 255):
                raise ValueError
        except ValueError:
            print("Error: Invalid color code. Please use a number from 0 to 255.")
            return

        new_attribute_name = sys.argv[4]
        if new_attribute_name not in ATTRIBUTES:
            print(f"Error: Attribute '{new_attribute_name}' not found.")
            list_available_options()
            return

        new_color_code = f"{ATTRIBUTES[new_attribute_name]};38;5;{color_code}"

    current_colors = get_current_colors()
    if file_type_to_change not in current_colors:
        # Allow adding new file types
        if not file_type_to_change.startswith("."):
            print(f"Error: File type '{file_type_to_change}' is not a valid file type.")
            print("File types must be one of the predefined types or a file extension starting with '.'")
            list_available_options()
            return

    current_colors[file_type_to_change] = new_color_code
    update_dir_colors_file(current_colors)

    print(f"Set {file_type_to_change} to color code {new_color_code}.")
    print("To apply the changes, run the following command in your shell:")
    print('eval "$(dircolors -b .dir_colors)"')

if __name__ == "__main__":
    main()
