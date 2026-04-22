"""Pointer color presets and terminal selection."""

COLOR_PRESETS = {
    "blue": {
        "display_name": "Blue",
        "hsv_ranges": [
            ((90, 80, 50), (130, 255, 255)),
        ],
        "pen_color": (255, 0, 0),
    },
    "green": {
        "display_name": "Green",
        "hsv_ranges": [
            ((35, 60, 50), (85, 255, 255)),
        ],
        "pen_color": (0, 255, 0),
    },
    "red": {
        "display_name": "Red",
        "hsv_ranges": [
            ((0, 120, 70), (10, 255, 255)),
            ((170, 120, 70), (180, 255, 255)),
        ],
        "pen_color": (0, 0, 255),
    },
}


def prompt_for_pointer_color():
    """Prompt for a valid pointer color in the terminal."""
    choices = ", ".join(COLOR_PRESETS)

    while True:
        response = input(f"Choose a pointer color ({choices}): ").strip().lower()
        if response in COLOR_PRESETS:
            return response, COLOR_PRESETS[response]

        print(f"Invalid choice. Please enter one of: {choices}")
